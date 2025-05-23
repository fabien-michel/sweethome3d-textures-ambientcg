import argparse
from datetime import timedelta
import multiprocessing
from time import sleep, strftime
import tomlkit
import zipfile
from functools import partial
from io import BytesIO
from itertools import product
from pathlib import Path

import requests
import requests_cache
from jinja2 import Environment, FileSystemLoader, select_autoescape
from PIL import Image, ImageOps

from excluded_categories import EXCLUDED_CATEGORIES
from make_preview import make_preview

Image.MAX_IMAGE_PIXELS = 200000000

SIZES = (1024, 512, 256)
DOWNLOAD_URLS = {
    1024: "https://murena.io/s/KQ7z5jzbcSdFNgJ",
    512: "https://murena.io/s/m4RiteG3QyPFgb7",
    256: "https://murena.io/s/Tyrz7MK4FeJYb4o",
}
TOTAL_LIMIT = None

JSON_BATCH_SIZE = 100
BASE_URL = "https://ambientcg.com/api/v2/full_json"
ORIGINAL_IMAGES_PATH = Path("ambientcg_originals")
RESIZED_IMAGE_BASE_PATH = Path("ambientcg")
IN_ZIP_IMAGE_PATH = "ambientcg"
ZIP_DOWNLOAD_RETRY = 5
SH3T_PACKAGE_BASE_PATH = Path("ambientcg.sh3t")
CATALOG_FILE_PATH = Path("PluginTexturesCatalog.properties")
PYPROJECT_PATH = Path("pyproject.toml")

ORIGINAL_IMAGES_PATH.mkdir(exist_ok=True)

def get_version(options):
    """
    return today version
    """
    if options.no_version:
        pyproject_toml = tomlkit.parse(PYPROJECT_PATH.read_text(encoding="UTF-8"))
        return pyproject_toml["tool"]["poetry"]["version"]

    return strftime("%Y.%m.%d")

def write_version(version):
    print(f"Version: {version}")
    pyproject_toml = tomlkit.parse(PYPROJECT_PATH.read_text(encoding="UTF-8"))
    pyproject_toml["tool"]["poetry"]["version"] = version
    PYPROJECT_PATH.write_text(tomlkit.dumps(pyproject_toml), encoding="UTF-8")


def check_file(zip_content, endswith_strings):
    """
    Return JSON zipContent item end with one of endsWith string
    """
    for filename, endswith_string in product(zip_content, endswith_strings):
        if filename.endswith(endswith_string):
            return filename
    return None


def get_asset_zip_url(asset, quality=1):
    """
    From JSON "asset" data return zip file Url and image to retrieve
    Search for lesser quality possible and for xxx_Color.jpg or xxx_var1.jpg file
    """
    downloads = asset["downloadFolders"]["default"]["downloadFiletypeCategories"][
        "zip"
    ]["downloads"]
    attribute = f"{quality}K-JPG"
    for download in downloads:
        if download["attribute"] == attribute:
            jpg_filename = check_file(
                download.get("zipContent", []), ["Color.jpg", "var1.jpg"]
            )
            if jpg_filename:
                return download["downloadLink"], jpg_filename

    if quality < 16:
        return get_asset_zip_url(asset, quality + 1)
    return None, None


def get_asset_data(asset):
    """
    From JSON asset return dict containing SH3D texture catalog data
    """
    zip_url, jpg_filename = get_asset_zip_url(asset)

    if not zip_url:
        raise Exception("No zip url found")
    
    # API return None for category, use displayCategory instead
    asset["category"] =  asset["category"] or asset["displayCategory"].replace(" ","")

    if asset["category"] in EXCLUDED_CATEGORIES:
        raise Exception("Excluded category")

    return {
        "catalog_infos": {
            "id": f"ambientcg#{asset['assetId']}",
            "name": asset["displayName"],
            "category": f"[ACG]{asset['category']}",
            "image": f"/{IN_ZIP_IMAGE_PATH}/{asset['assetId']}.jpg",
            "width": asset["dimensionX"] or 100,
            "height": asset["dimensionY"] or 100,
            "creator": "ambientCG.com",
        },
        "assetId": asset["assetId"],
        "category": asset["category"],
        "zip_url": zip_url,
        "in_zip_jpg_filename": jpg_filename,
        "image_filename": f"{asset['assetId']}.jpg",
    }


def fetch_catalog_data(options):
    """
    Fetch remote JSON of all material assets and return list of data required to
    download images and to build catalog
    """
    # expire_after = 0 if options.no_json_cache else -1
    session = requests_cache.CachedSession("requests_cache", expire_after=timedelta(days=1))
    if options.no_json_cache:
        session.cache.clear()
    session.remove_expired_responses()
    base_params = {
        "type": "Material",
        "include": "displayData,dimensionsData,downloadData",
    }
    offset = 0
    last_fetch_count = 1
    catalog_data = []
    while last_fetch_count:
        params = {
            **base_params,
            "limit": JSON_BATCH_SIZE,
            "offset": offset,
        }
        request = requests.Request("GET", BASE_URL, params=params)
        prepared_request = session.prepare_request(request)
        print(prepared_request.url)
        response = session.send(prepared_request)
        json_data = response.json()

        for asset in json_data["foundAssets"]:
            print(asset["assetId"])
            try:
                # with ipdb.launch_ipdb_on_exception():
                catalog_data.append(get_asset_data(asset))
            except Exception as e:
                print(f"ERROR: {e}")

        last_fetch_count = len(json_data["foundAssets"])
        offset += JSON_BATCH_SIZE
        if TOTAL_LIMIT and offset >= TOTAL_LIMIT:
            break

    return sorted(catalog_data, key=lambda entry: entry["assetId"])


def download_images(catalog_data, options):
    """
    Download all zip and extract images from given metadata
    """

    for entry in catalog_data:
        dest_path = ORIGINAL_IMAGES_PATH / entry["image_filename"]
        if not options.no_image_cache and dest_path.exists():
            continue
        print(entry["zip_url"])
        
        retry = ZIP_DOWNLOAD_RETRY
        while retry:
            try:
                zip_file_response = requests.get(entry["zip_url"])
            except requests.exceptions.ConnectionError:
                retry -=1
                if not retry:
                    raise
                print("Hmm, zip download fail. New attempt in 5 seconds")
                sleep(5)
            else:
                break
                    
            
        with zipfile.ZipFile(BytesIO(zip_file_response.content)) as the_zip:
            color_file_info = next(
                filter(
                    lambda zipinfo: zipinfo.filename == entry["in_zip_jpg_filename"],
                    the_zip.infolist(),
                ),
                None,
            )

            with the_zip.open(color_file_info) as the_file:
                with open(dest_path, "wb") as f:
                    f.write(the_file.read())


def get_resized_image_path(size):
    image_path = RESIZED_IMAGE_BASE_PATH.with_name(f"{RESIZED_IMAGE_BASE_PATH}_{size}")
    image_path.mkdir(exist_ok=True)
    return image_path


def resize_image(original_image_path, size=256):
    """
    Resize given image to fit in given box
    """
    image_path = get_resized_image_path(size) / original_image_path.name

    if image_path.exists():
        return
    print(f"Resize {size} {original_image_path}")
    image = Image.open(original_image_path)
    resized_image = ImageOps.contain(image, (size, size))
    resized_image.save(image_path)


def resize_images(catalog_data):
    """
    Parallelized image resize to fit in given box
    """
    image_files = [
        ORIGINAL_IMAGES_PATH / entry["image_filename"] for entry in catalog_data
    ]
    for size in SIZES:
        with multiprocessing.Pool() as p:
            p.map(partial(resize_image, size=size), image_files)


def write_catalog_file(catalog_data, version):
    """
    Write PluginTexturesCatalog.properties file from given catalog data
    """
    content = Path("catalog_header.txt").read_text().format(version=version)
    for index, entry in enumerate(catalog_data):
        entry_content = "\n".join(
            f"{key}#{index+1}={value}" for key, value in entry["catalog_infos"].items()
        )
        content += entry_content + "\n\n"
    CATALOG_FILE_PATH.write_text(content)

def get_package_path(size):
    return SH3T_PACKAGE_BASE_PATH.with_stem(SH3T_PACKAGE_BASE_PATH.stem + f"_{size}")

def __package_size__(catalog_data, size):
    sh3t_file_path = get_package_path(size)
    print(f"Build package {sh3t_file_path}")
    if sh3t_file_path.exists():
        sh3t_file_path.unlink()

    with zipfile.ZipFile(sh3t_file_path, "w", compression = zipfile.ZIP_DEFLATED) as zip_object:
        zip_object.write(CATALOG_FILE_PATH)
        for entry in catalog_data:
            zip_object.write(
                get_resized_image_path(size) / entry["image_filename"],
                f"{IN_ZIP_IMAGE_PATH}/{entry['image_filename']}",
            )

def package_lib(catalog_data):
    """
    Create .sh3t (zip file) for each size
    """
    with multiprocessing.Pool() as p:
        p.map(partial(__package_size__, catalog_data), SIZES)


def build_readme(catalog_data, version):
    print("Build README.md")
    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    template = env.get_template("README.jinja")
    git_tag = f"v{version}"
    preview_categories = sorted(list(set(entry['category'] for entry in catalog_data)))
    Path('README.md').write_text(template.render(
        download_base_url = f"https://github.com/fabien-michel/sweethome3d-textures-ambientcg/raw/{git_tag}",
        preview_base_url = f"https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/{git_tag}/previews",
        version = version,
        catalog_data = catalog_data,
        git_tag = git_tag,
        preview_categories = preview_categories,
        download_versions = [(get_package_path(size), DOWNLOAD_URLS[size]) for size in SIZES],
    ))



def build_texture_lib(options):
    catalog_data = fetch_catalog_data(options)
    version = get_version(options)
    download_images(catalog_data, options)
    resize_images(catalog_data)
    write_catalog_file(catalog_data, version)
    package_lib(catalog_data)
    make_preview(catalog_data)
    build_readme(catalog_data, version)
    write_version(version)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-json-cache", action="store_true")
    parser.add_argument("--no-image-cache", action="store_true")
    parser.add_argument("--no-version", action="store_true")
    options = parser.parse_args()
    build_texture_lib(options)

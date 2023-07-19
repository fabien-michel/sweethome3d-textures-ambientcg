import os
import urllib.parse

import tomlkit

from build import SIZES, DOWNLOAD_URLS, PYPROJECT_PATH

pyproject_toml = tomlkit.parse(PYPROJECT_PATH.read_text(encoding="UTF-8"))

VERSION = pyproject_toml["tool"]["poetry"]["version"]
GIT_VERSION = f"v{VERSION}"

if __name__ == "__main__":
    os.system("git add VERSION README.md previews/*.webp")
    os.system(f"git commit -m \"version: {GIT_VERSION}\"")
    os.system(f"git tag {GIT_VERSION}")
    # os.system("cd .. && bfg --delete-files \"*.sh3t\" sweethome3d-textures-ambientcg")
    os.system("git reflog expire --expire=now --all && git gc --prune=now --aggressive")
    os.system("git push --force")
    os.system("git push --force --tags")

    download_versions = [
        # f"- [ambientcg_{size}.sh3t](https://github.com/fabien-michel/sweethome3d-textures-ambientcg/raw/{GIT_VERSION}/ambientcg_{size}.sh3t)"
        f"- [ambientcg_{size}.sh3t]({DOWNLOAD_URLS[size]})"
        for size in SIZES
    ]
    body = "\n".join(download_versions)

    params = urllib.parse.urlencode(
        {
            "tag": GIT_VERSION,
            "title": GIT_VERSION,
            "body": body,
        }
    )

    print(
        "https://github.com/fabien-michel/sweethome3d-textures-ambientcg/releases/new?"
        + params
    )

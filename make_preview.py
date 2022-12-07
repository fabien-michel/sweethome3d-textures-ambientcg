import multiprocessing
import os
from collections import defaultdict
from operator import itemgetter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

# Configure values
IMAGE_WIDTH = 1024
THUMBNAIL_SIZE = 128
IMAGE_MARGIN = 16
THUMBNAILS_GAP_WIDTH = 16
THUMBNAILS_GAP_HEIGHT = 48
TEXT_PLACEHOLDER = 32
FONT_PATH = "/usr/share/fonts/TTF/DejaVuSans.ttf"
FONT_SIZE = 12
PREVIEWS_DIR = Path("previews")
ORIGINAL_IMAGES_PATH = Path("ambientcg_originals")


PREVIEWS_DIR.mkdir(exist_ok=True)


def group_by_categories(catalog_data):
    categories = defaultdict(list)
    for entry in catalog_data:
        categories[entry["category"]].append(entry)
    for category in categories.keys():
        categories[category].sort(key=itemgetter("assetId"))
    return categories


def make_category_preview(catalog_entries):
    category_name = catalog_entries[0]["category"]
    print(f"Create preview for category {category_name}")

    # Get the list of jpeg files in the current directory
    # files = [f for f in os.listdir('.') if f.endswith('.jpg')]

    # Calculate the number of columns and rows needed
    num_thumbs = len(catalog_entries)
    num_cols = int(
        (IMAGE_WIDTH - IMAGE_MARGIN * 2) / (THUMBNAIL_SIZE + THUMBNAILS_GAP_WIDTH / 2)
    )
    num_rows = num_thumbs // num_cols + (1 if num_thumbs % num_cols else 0)

    # Calculate the height of the image based on the number of rows
    image_height = 2 * IMAGE_MARGIN + num_rows * (
        THUMBNAIL_SIZE + THUMBNAILS_GAP_HEIGHT
    )

    # Create a blank image with the configured width and height
    main_image = Image.new("RGB", (IMAGE_WIDTH, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(main_image)

    # Set the font to use
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Iterate over the files, adding a thumbnail for each one
    for index, entry in enumerate(catalog_entries):
        # Open the image file
        image = Image.open(ORIGINAL_IMAGES_PATH / entry["image_filename"])

        # Resize the image to the thumbnail size
        # ImageOps.fit(image, )
        image.thumbnail((THUMBNAIL_SIZE, THUMBNAIL_SIZE))

        # Calculate the position to paste the thumbnail
        x = IMAGE_MARGIN + (index % num_cols) * (THUMBNAIL_SIZE + THUMBNAILS_GAP_WIDTH)
        y = IMAGE_MARGIN + (index // num_cols) * (
            THUMBNAIL_SIZE + THUMBNAILS_GAP_HEIGHT
        )

        # Paste the thumbnail onto the main image
        main_image.paste(image, (x, y))

        # Draw the filename under the thumbnail
        text_width, text_height = draw.textsize(entry["assetId"], font=font)
        draw.text(
            (
                x + (THUMBNAIL_SIZE - text_width) / 2,
                y + THUMBNAIL_SIZE + 5,
            ),
            entry["assetId"],
            (0, 0, 0),
            font=font,
        )

    # Save the final image
    main_image.save(PREVIEWS_DIR / f"{category_name}.webp")


def make_preview(catalog_data):
    categories = group_by_categories(catalog_data)

    with multiprocessing.Pool() as p:
        p.map(make_category_preview, categories.values())

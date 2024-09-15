import requests
import random

from dependencies.config import *
from PIL import Image, ImageDraw, ImageOps
from io import BytesIO

json_url = 'http://playrust.io/maps.json'

# Makes Map Image Rounded
def create_rounded_image(image, radius):
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, image.size[0], image.size[1]], radius, fill=255)

    rounded_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    rounded_image.putalpha(mask)

    return rounded_image


# Main Function For Getting Map Image, Level, Size
def get_map():
    response = requests.get(json_url)

    if response.status_code == 200:
        data = response.json()
        maps = data.get('maps', [])

        seeds_and_sizes = [(map_data.get('seed'), map_data.get('size'), map_data.get('name')) for map_data in maps]
        chosen_seed, chosen_size, level = random.choice(seeds_and_sizes)
        if level == "Procedural Map":
            image_url = f'http://playrust.io/preview.jpg?level=Procedural%20Map&size={chosen_size}&seed={chosen_seed}'
        else:
            image_url = f'http://playrust.io/preview.jpg?level=Barren&size={chosen_size}&seed={chosen_seed}'
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            pil_image = Image.open(BytesIO(image_response.content))
            resized_image = pil_image.resize((MAP_WIDTH, MAP_HEIGHT))

            rounded_image = create_rounded_image(resized_image, radius=15)

            return chosen_seed, chosen_size, level, rounded_image
        else:
            print(f"Failed to retrieve the image. Status code: {image_response.status_code}")
            return chosen_seed, chosen_size, None, None
    else:
        return response.status_code, None, None, None
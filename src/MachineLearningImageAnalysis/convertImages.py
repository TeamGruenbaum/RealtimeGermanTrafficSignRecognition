import os
from PIL import Image

input_folder = "images"

output_folder = "converted_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".ppm"):
        image = Image.open(os.path.join(input_folder, filename))
        image.save(os.path.join(output_folder,
                                os.path.splitext(filename)[0] + ".jpg"))
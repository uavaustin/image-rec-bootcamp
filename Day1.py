

import requests
url = "http://docs.uavaustin.org/guides/image-rec/img/background.jpg"
res = requests.get(url, stream=True)
filename = "background.jpg"

with open(filename, "wb") as f:
    # get request
    response = requests.get(url, stream=True)
    # write to file
    f.write(response.content)


from PIL import Image
import pathlib

img = Image.open("background.jpg")
img.resize((8,8), Image.ANTIALIAS)
img.save('img.jpg')
img.show()
print("Image width, height: {}.".format(img.size))


# Desired tile size
tile_width = tile_height = 512


save_dir = pathlib.Path("C:/Users/bprim/PycharmProjects/UAV_Img/image-rec-bootcamp/crop")
if not save_dir.is_dir():
    save_dir.mkdir(exist_ok= False, parents = False)

    for x in range(0, img.size[0] - tile_width, tile_width):
        for y in range(0, img.size[1] - tile_height, tile_height):
            crop = img.crop((x,y, x+tile_width, y+tile_height))
            crop.save(save_dir / f"crop_{x}_{y}.jpg")




import tarfile
import tempfile
import requests

# Images
# Where to download assets.
url = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=base-shapes-v1.tar.gz"

# Where to save assets.
save_dir = pathlib.Path("../image-rec-bootcamp/assets").expanduser()

if not save_dir.is_dir():
    save_dir.mkdir(exist_ok=True, parents=True)
    res = requests.get(url, stream=True)

    # Make a temp dir to download archive.
    with tempfile.TemporaryDirectory() as d:
        tmp_file = pathlib.Path(d) / "file.tar.gz"
        tmp_file.write_bytes(res.raw.read())

        with tarfile.open(tmp_file) as tar:
            tar.extractall(save_dir)

# Fonts

# Where to download assets.
url = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=fonts.tar.gz"

# Where to save assets.
save_dir = pathlib.Path("../image-rec-bootcamp/fonts").expanduser()

if not save_dir.is_dir():
    save_dir.mkdir(exist_ok=True, parents=True)
    res = requests.get(url, stream=True)

    # Make a temp dir to download archive.
    with tempfile.TemporaryDirectory() as d:
        tmp_file = pathlib.Path(d) / "file.tar.gz"
        tmp_file.write_bytes(res.raw.read())

        with tarfile.open(tmp_file) as tar:
            tar.extractall(save_dir)

target = Image.open(r"C:\Users\bprim\PycharmProjects\UAV_Img\image-rec-bootcamp\assets\base-shapes-v1\pentagon\pentagon-01.png")

# First, you must open the target image!
# target = target.rotate(45)
# target.show('Rotated Image')

from PIL import ImageDraw, ImageFont

# Create an drawable object which we can edit.
target_draw = ImageDraw.Draw(target)

# Use B for example
alpha = "B"

# Define font multiplier to shrink or grow to fit letter to target. For some shape/letter
# combinations, we must adapt the size of the letter.
font_multiplier = 0.5

# Path to font image file
font_file = save_dir / "fonts/Gudea/Gudea-Bold.ttf"

# Create font height based on target size and scaled by font_multiplier.
font_size = int(round(font_multiplier * target.height))

# Create font to put on target_draw.
font = ImageFont.truetype(str(font_file), font_size)

# Get width and height of the font.
w, h = target_draw.textsize(alpha, font=font)

# Get top left coordinate of where to paste alpha onto target.
x = (target.width - w) / 2
y = (target.height - h) / 2

# Set the rgb color of the alpha.
alpha_rgb = ((64, 115, 64))  # Greenish

# Finally, draw the alpha onto the target
target_draw.text((x,y), alpha, alpha_rgb, font=font)

# Rotate target
angle = 45
rotated_image = target.rotate(angle, expand=1)
rotated_image.show("Rotated Image")
rotated_image.save("C:/Users/bprim/PycharmProjects/UAV_Img/image-rec-bootcamp/manipulated_img.png")



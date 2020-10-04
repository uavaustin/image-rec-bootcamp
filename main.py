# Import the PIL package.
from PIL import Image

# Open up the background image. NOTE: The path on your computer will be different.
img = Image.open("background.jpg")

# Sanity check to make sure you have the right image.
img.show("Example Image")

print(f"Image width, height: {*img.size,}.")




# Desired tile size.
tile_width = tile_height = 512

# Make a folder to save images. We use `pathlib` for most path manipulation.
import pathlib

save_dir = pathlib.Path("Photos").expanduser()
save_dir.mkdir(exist_ok=True, parents=True)

# Now tile up the image:
for x in range(0, img.size[0] - tile_width, tile_width):
    for y in range(0, img.size[1] - tile_height, tile_height):
        crop = img.crop((x, y, x + tile_width, y + tile_height))
        crop.save(save_dir / f"crop_{x}_{y}.jpg")

print(f"Generated {len(list(save_dir.glob('*.jpg')))} slices!")



import tarfile
import tempfile
import requests


# Where to download assets.
url = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=base-shapes-v1.tar.gz"

# Where to save assets.
save_dir = pathlib.Path("Targets").expanduser()
save_dir.mkdir(exist_ok=True, parents=True)

res = requests.get(url, stream=True)

# Make a temp dir to download archive.
with tempfile.TemporaryDirectory() as d:
    tmp_file = pathlib.Path(d) / "file.tar.gz"
    tmp_file.write_bytes(res.raw.read())

    with tarfile.open(tmp_file) as tar:
        tar.extractall(save_dir)



shape = Image.open("/Users/alessandrakeeler/Documents/Practice/Targets/base-shapes-v1/pentagon/pentagon-01.png")

# Sanity check
#shape.show("Example shape")


# Where to download assets.
url = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=fonts.tar.gz"

# Where to save assets.
save_dir = pathlib.Path("Fonts").expanduser()
save_dir.mkdir(exist_ok=True, parents=True)

res = requests.get(url, stream=True)

# Make a temp dir to download archive.
with tempfile.TemporaryDirectory() as d:
    tmp_file = pathlib.Path(d) / "file.tar.gz"
    tmp_file.write_bytes(res.raw.read())

    with tarfile.open(tmp_file) as tar:
        tar.extractall(save_dir)

# First, you must open the target image!

target = Image.open("/Users/alessandrakeeler/Documents/Practice/Targets/base-shapes-v1/pentagon/pentagon-01.png")
target = target.rotate(45)
target.show('Rotated Image')




from PIL import ImageDraw, ImageFont

# Create an drawable object which we can edit.
target_draw = ImageDraw.Draw(target)

# Use B for example
alpha = "B"

# Define font multiplier to shrink or grow to fit letter to target. For some shape/letter
# combinations, we must adapt the size of the letter.
font_multiplier = 0.5

# Path to font image file
font_file = save_dir / "/Users/alessandrakeeler/Documents/Practice/Fonts/fonts/Gudea/Gudea-Bold.ttf"

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


for x in range(rotated_image.width):
    for y in range(rotated_image.height):

        r, g, b, a = rotated_image.getpixel((x, y))

        if r == 255 and g == 255 and b == 255:
            rotated_image.putpixel((x, y), (0, 0, 0, 0))


rotated_crop = rotated_image.crop(rotated_image.getbbox()) 


rotated_image.size 


rotated_image = rotated_image.resize((100, 100))


background_tile = Image.open("/Users/alessandrakeeler/Documents/Practice/Photos/crop_1024_1024.jpg")

paste_loc = (20, 20)
background_tile.paste(rotated_image, paste_loc, rotated_image)
background_tile.show()


w_target, h_target = rotated_image.size
txt = pathlib.Path("background_target.txt")
txt.write_text(
    f"pentagon, {int(paste_loc[0])}, {int(paste_loc[1])}, {w_target}, {h_target}\n"
)













from PIL import Image
img = Image.open("C:/Users/anyap/Desktop/uav/bootcamp/images/background.jpg")
img.show()
print(f"Image width, height: {*img.size,}.")
tile_width = tile_height = 512
import pathlib

save_dir = pathlib.Path("C:/Users/anyap/Desktop/uav/bootcamp/assets/tiles").expanduser()
save_dir.mkdir(exist_ok=True, parents=True)
for x in range(0, img.size[0] - tile_width, tile_width):
    for y in range(0, img.size[1] - tile_height, tile_height):
        crop = img.crop((x, y, x + tile_width, y + tile_height))
        crop.save(save_dir / f"crop_{x}_{y}.jpg")

print(f"Generated {len(list(save_dir.glob('*.jpg')))} slices!")
import tarfile
import tempfile
import requests
url = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=base-shapes-v1.tar.gz"
save_dir = pathlib.Path("C:/Users/anyap/Desktop/uav/bootcamp/assets").expanduser()
save_dir.mkdir(exist_ok=True, parents=True)

res = requests.get(url, stream=True)
with tempfile.TemporaryDirectory() as d:
    tmp_file = pathlib.Path(d) / "file.tar.gz"
    tmp_file.write_bytes(res.raw.read())

    with tarfile.open(tmp_file) as tar:
        tar.extractall(save_dir)
target = Image.open("C:/Users/anyap/Desktop/uav/bootcamp/assets/base-shapes-v1/circle/circle-01.png")
target.show()
import tarfile
import tempfile
import requests
url = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=fonts.tar.gz"
save_dir = pathlib.Path("C:/Users/anyap/Desktop/uav/bootcamp/assets").expanduser()
save_dir.mkdir(exist_ok=True, parents=True)

res = requests.get(url, stream=True)
with tempfile.TemporaryDirectory() as d:
    tmp_file = pathlib.Path(d) / "file.tar.gz"
    tmp_file.write_bytes(res.raw.read())

    with tarfile.open(tmp_file) as tar:
        tar.extractall(save_dir)
target = target.rotate(45)
target.show()
from PIL import ImageDraw, ImageFont
target_draw = ImageDraw.Draw(target)
alpha = "B"
font_multiplier = 0.5
font_file = save_dir / "C:/Users/anyap/Desktop/uav/bootcamp/assets/fonts/Gudea/Gudea-Bold.ttf"
font_size = int(round(font_multiplier * target.height))
font = ImageFont.truetype(str(font_file), font_size)
w, h = target_draw.textsize(alpha, font=font)
x = (target.width - w) / 2
y = (target.height - h) / 2
alpha_rgb = ((64, 115, 64))
target_draw.text((x,y), alpha, alpha_rgb, font=font)
angle = 45
rotated_image = target.rotate(angle, expand=1)
rotated_image.show()
for x in range(rotated_image.width):
    for y in range(rotated_image.height):

        r, g, b, a = rotated_image.getpixel((x, y))

        if r == 255 and g == 255 and b == 255:
            rotated_image.putpixel((x, y), (0, 0, 0, 0))
rotated_crop = rotated_image.crop(rotated_image.getbbox())
rotated_image.size
rotated_image = rotated_image.resize((100, 100))
paste_loc = (20, 20)
background_tile = Image.open("C:/Users/anyap/Desktop/uav/bootcamp/assets/tiles/crop_0_0.jpg")
background_tile.paste(rotated_image, paste_loc, rotated_image)
background_tile.show()
w_target, h_target = rotated_image.size
w_target, h_target = rotated_image.size
txt = pathlib.Path("C:/Users/anyap/Desktop/uav/bootcamp/assets/background_target.txt")
txt.write_text(
    f"pentagon, {int(paste_loc[0])}, {int(paste_loc[1])}, {w_target}, {h_target}\n"
)
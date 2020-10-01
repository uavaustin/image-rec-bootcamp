import io
from PIL import Image
from PIL import ImageDraw, ImageFont
import pathlib
import tarfile
import tempfile
import requests

#first demo
#for i in range(10):
#    fname = "image"+str(i)+".jpg"
#    im = Image.new(mode="RGB",size=(512,512),color=(int(255/(i+1)),int(255/(i+1)),int(255/(i+1))))
#    im.save("./images/"+fname)

#img = Image.open("./background.jpg")
#img.show("Background")
#print("Image Size:")
#print(img.size)
#print("\n")


url = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=base-shapes-v1.tar.gz"
url_background = "http://docs.uavaustin.org/guides/image-rec/img/background.jpg"

save_dir_assets = pathlib.Path("./assets").expanduser()
if not save_dir_assets.is_dir():
    save_dir_assets.mkdir(exist_ok=True,parents=True)

res = requests.get(url,stream=True)
res_background = requests.get(url_background,stream=True)

with tempfile.TemporaryDirectory() as d:
    tmp_file = pathlib.Path(d) / "file.tar.gz"
    tmp_file.write_bytes(res.raw.read())
    
    with tarfile.open(tmp_file) as tar:
        tar.extractall(save_dir_assets)

im_bytes = io.BytesIO(res_background.content)
img = Image.open(im_bytes)

w = h = 512

save_dir_crops = pathlib.Path("./crops").expanduser()
save_dir_crops.mkdir(exist_ok=True,parents=True)

for x in range(0,img.size[0]-w,w):
    for y in range(0,img.size[1]-h,h):
        crop = img.crop((x,y,x+w,y+h))
        crop.save(save_dir_crops / f"crop_{x}_{y}.jpg")
#print("Crops Generated:")
#print(len(list(save_dir_crops.glob("*.jpg"))))


#shape = Image.open("./assets/base-shapes-v1/circle/circle-01.png")
#shape.show("Shape")

url_fonts = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=fonts.tar.gz"

res_fonts = requests.get(url_fonts,stream=True)

with tempfile.TemporaryDirectory() as d:
    tmp_file = pathlib.Path(d) / "file.tar.gz"
    tmp_file.write_bytes(res_fonts.raw.read())

    with tarfile.open(tmp_file) as tar:
        tar.extractall(save_dir_assets)

## Image Manipulation

target = Image.open("./assets/base-shapes-v1/pentagon/pentagon-01.png")
target.rotate(45)
target_draw = ImageDraw.Draw(target)

alpha = "B"
font_multip = 0.5

font_file = save_dir_assets / "fonts/Gudea/Gudea-Bold.ttf"
font_size = int(round(font_multip*target.height))
font = ImageFont.truetype(str(font_file),font_size)

target_w, target_h = target_draw.textsize(alpha,font=font)

x = (target.width - target_w)/2
y = (target.height - target_h)/2

alpha_rgb = ((64,115,64))
target_draw.text((x,y),alpha,alpha_rgb,font=font)

angle = 45
rotated_image = target.rotate(angle,expand=1)
rotated_image.show("Rotated Image")

for x in range (rotated_image.width):
    for y in range(rotated_image.height):

        r,g,b,a = rotated_image.getpixel((x,y))

        if r == 255 and g == 255 and b == 255:
            rotated_image.putpixel((x,y),(0,0,0,0))

rotated_crop = rotated_image.crop(rotated_image.getbbox())

#print(rotated_image.size)

rotated_image = rotated_image.resize((100,100))

paste_loc = (20,20)
background_tile = img
background_tile.paste(rotated_image,paste_loc,rotated_image)
background_tile.show()

w_target,h_target = rotated_image.size
txt = pathlib.Path("background_target.txt")
txt.write_text(
        f"pentagon, {int(paste_loc[0])},{int(paste_loc[1])},{w_target},{h_target}\n"
        )

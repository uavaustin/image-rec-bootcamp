from PIL import Image
import pathlib
import tarfile
import tempfile
import requests

#first demo
#for i in range(10):
#    fname = "image"+str(i)+".jpg"
#    im = Image.new(mode="RGB",size=(512,512),color=(int(255/(i+1)),int(255/(i+1)),int(255/(i+1))))
#    im.save("./images/"+fname)

img = Image.open("./background.jpg")
img.show("Background")
print("Image Size:")
print(img.size)
print("\n")

w = h = 512

save_dir_crops = pathlib.Path("./images").expanduser()
save_dir_crops.mkdir(exist_ok=True,parents=True)

for x in range(0,img.size[0]-w,w):
    for y in range(0,img.size[1]-h,h):
        crop = img.crop((x,y,x+w,y+h))
        crop.save(save_dir_crops / f"crop_{x}_{y}.jpg")
print("Crops Generated:")
print(len(list(save_dir_crops.glob("*.jpg"))))

url = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=base-shapes-v1.tar.gz"

save_dir_assets = pathlib.Path("./assets").expanduser()
if not save_dir_assets.is_dir():
    save_dir_assets.mkdir(exist_ok=True,parents=True)

res = requests.get(url,stream=True)

with tempfile.TemporaryDirectory() as d:
    tmp_file = pathlib.Path(d) / "file.tar.gz"
    tmp_file.write_bytes(res.raw.read())
    
    with tarfile.open(tmp_file) as tar:
        tar.extractall(save_dir_assets)

shape = Image.open("./assets/base-shapes-v1/circle/circle-01.png")
shape.show("Shape")

url_fonts = "https://bintray.com/uavaustin/target-finder-assets/download_file?file_path=fonts.tar.gz"

res_fonts = requests.get(url_fonts,stream=True)

with tempfile.TemporaryDirectory() as d:
    tmp_file = pathlib.Path(d) / "file.tar.gz"
    tmp_file.write_bytes(res_fonts.raw.read())

    with tarfile.open(tmp_file) as tar:
        tar.extractall(save_dir_assets)


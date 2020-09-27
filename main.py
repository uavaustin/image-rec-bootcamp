from PIL import Image
import pathlib
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

save_dir = pathlib.Path("./images").expanduser()
save_dir.mkdir(exist_ok=True,parents=True)

for x in range(0,img.size[0]-w,w):
    for y in range(0,img.size[1]-h,h):
        crop = img.crop((x,y,x+w,y+h))
        crop.save(save_dir / f"crop_{x}_{y}.jpg")
print("Crops Generated:")
print(len(list(save_dir.glob("*.jpg"))))

from PIL import Image
for i in range(10):
    fname = "image"+str(i)+".jpg"
    im = Image.new(mode="RGB",size=(512,512),color=(int(255/(i+1)),int(255/(i+1)),int(255/(i+1))))
    im.save("./images/"+fname)
    

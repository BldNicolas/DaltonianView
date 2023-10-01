from PIL.Image import *

i = open("image.png")


a = 0
b = 0



while (a<256) and (b<192) :
    x = a
    y = b
    (red,green,blue,unknow) = i.getpixel((x,y)) 
    print (red,green,blue,unknow)
    if red==255 and green < 80 :
        x=a
        y=b
        (red,green,blue,unknow)=(255,128,1,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    
    a=a+1
    b=b+1
Image.show(i)

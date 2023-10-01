from PIL.Image import *

i = open("image.png")


a = 0
b = 0



while (a<256) and (b<192) :
    x = a
    y = b
    (red,green,blue,unknow) = i.getpixel((x,y)) 
    print (red,green,blue,unknow)
    if red > 200 and green < 80 :                # rouge
        x=a
        y=b
        (red,green,blue,unknow)=(255,0,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    elif red > 200 and green < 127 :             # orange
        x=a
        y=b
        (red,green,blue,unknow)=(255,127,127,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    elif red > 200 and green > 200 :            # jaune
        x=a
        y=b
        (red,green,blue,unknow)=(255,255,255,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    elif red < 50 and green > 200 :             # vert
        x=a
        y=b
        (red,green,blue,unknow)=(125,255,255,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    
    
    a=a+1
    b=b+1
Image.show(i)

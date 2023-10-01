from PIL.Image import *

i = open("image.png")


x = 0
y = 0
a = 0


while (x<256) and (y<192) :
    (red,green,blue,unknow) = i.getpixel((x,y)) 
    if red > 200 and green < 80 and  blue < 80:     # rouge
        (red,green,blue,unknow)=(255,0,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    elif red > 200 and green < 127 :                # orange
        (red,green,blue,unknow)=(255,127,127,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red > 200 and green > 200 :                # jaune
        (red,green,blue,unknow)=(255,255,255,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red < 50 and green < 200 :                 # vert
        (red,green,blue,unknow)=(125,255,255,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    
    x=x+1

    if (x==255):
        x=0
        y=y+1


        
Image.show(i)

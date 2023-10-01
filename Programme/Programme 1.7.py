from PIL.Image import *

i = open("image.png")

Image.show(i)

x = 0
y = 0
a = 0


while (x<256) and (y<192) :
    (red,green,blue,unknow) = i.getpixel((x,y)) 
    if red < 42 and green < 42 and  blue < 42:     # 1
        (red,green,blue,unknow)=(21,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    elif red < 42 and green < 42  and blue > 42 and blue < 85:                # 2
        (red,green,blue,unknow)=(21,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red < 42 and green < 42 and blue > 85 and blue < 128 :                # 3
        (red,green,blue,unknow)=(21,21,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red < 42 and green < 42 and blue < 170 and blue > 128 :                 # 4
        (red,green,blue,unknow)=(21,21,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red < 42 and green < 42 and blue < 212 and blue > 170 :                 # 5
        (red,green,blue,unknow)=(21,21,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red < 42 and green < 42 and blue < 255 and blue > 212 :                 # 6
        (red,green,blue,unknow)=(21,21,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>42 and green<85 and blue>0 and blue<42 :      # 7
        (red,green,blue,unknow)=(21,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>85 and green<128 and blue>0 and blue<42 :      # 8
        (red,green,blue,unknow)=(21,107,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>128 and green<170 and blue>0 and blue<42 :      # 9
        (red,green,blue,unknow)=(21,149,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>170 and green<212 and blue>0 and blue<42 :      # 10
        (red,green,blue,unknow)=(21,191,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>212 and green<255 and blue>0 and blue<42 :      # 11
        (red,green,blue,unknow)=(21,233,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>0 and green<42 and blue>0 and blue<42 :      # 12
        (red,green,blue,unknow)=(64,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>0 and green<42 and blue>0 and blue<42 :      # 13
        (red,green,blue,unknow)=(107,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>0 and green<42 and blue>0 and blue<42 :      # 14
        (red,green,blue,unknow)=(149,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>0 and green<42 and blue>0 and blue<42 :      # 15
        (red,green,blue,unknow)=(191,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>0 and green<42 and blue>0 and blue<42 :      # 16
        (red,green,blue,unknow)=(233,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>42 and green<85 and blue>0 and blue<42 :      # 17
        (red,green,blue,unknow)=(64,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>42 and green<85 and blue>0 and blue<42 :      # 18
        (red,green,blue,unknow)=(107,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>42 and green<85 and blue>0 and blue<42 :      # 19
        (red,green,blue,unknow)=(149,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>42 and green<85 and blue>0 and blue<42 :      # 20
        (red,green,blue,unknow)=(191,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>42 and green<85 and blue>0 and blue<42 :      # 21
        (red,green,blue,unknow)=(233,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>85 and green<128 and blue>0 and blue<42 :      # 22
        (red,green,blue,unknow)=(64,107,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>128 and green<170 and blue>0 and blue<42 :      # 23
        (red,green,blue,unknow)=(64,149,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>170 and green<212 and blue>0 and blue<42 :      # 24
        (red,green,blue,unknow)=(64,191,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>212 and green<255 and blue>0 and blue<42 :      # 25
        (red,green,blue,unknow)=(64,233,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>0 and green<42 and blue>42 and blue<85 :      # 26
        (red,green,blue,unknow)=(64,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>0 and green<42 and blue>42 and blue<85 :      # 27
        (red,green,blue,unknow)=(107,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>0 and green<42 and blue>42 and blue<85 :      # 28
        (red,green,blue,unknow)=(149,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>0 and green<42 and blue>42 and blue<85 :      # 29
        (red,green,blue,unknow)=(191,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>0 and green<42 and blue>42 and blue<85 :      # 30
        (red,green,blue,unknow)=(233,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>0 and green<42 and blue>85 and blue<128 :      # 31
        (red,green,blue,unknow)=(64,21,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>0 and green<42 and blue>128 and blue<170 :      # 32
        (red,green,blue,unknow)=(64,21,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>0 and green<42 and blue>170 and blue<212 :      # 33
        (red,green,blue,unknow)=(64,21,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>0 and green<42 and blue>212 and blue<255 :      # 34
        (red,green,blue,unknow)=(64,21,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>42 and green<85 and blue>42 and blue<85 :      # 35
        (red,green,blue,unknow)=(21,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>85 and green<128 and blue>42 and blue<85 :      # 36
        (red,green,blue,unknow)=(21,107,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>128 and green<170 and blue>42 and blue<85 :      # 37
        (red,green,blue,unknow)=(21,149,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>170 and green<212 and blue>42 and blue<85 :      # 38
        (red,green,blue,unknow)=(21,191,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>212 and green<255 and blue>42 and blue<85 :      # 39
        (red,green,blue,unknow)=(21,233,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>42 and green<85 and blue>85 and blue<128 :      # 40
        (red,green,blue,unknow)=(21,64,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>42 and green<85 and blue>128 and blue<170 :      # 41
        (red,green,blue,unknow)=(21,64,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>42 and green<85 and blue>170 and blue<212 :      # 42
        (red,green,blue,unknow)=(21,64,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>0 and red<42 and green>42 and green<85 and blue>212 and blue<255 :      # 43
        (red,green,blue,unknow)=(21,64,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>42 and green<85 and blue>42 and blue<85 :      # 44
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>85 and green<128 and blue>85 and blue<128 :      # 45
        (red,green,blue,unknow)=(107,107,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>128 and green<170 and blue>128 and blue<170 :      # 46
        (red,green,blue,unknow)=(149,149,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>170 and green<212 and blue>170 and blue<212 :      # 47
        (red,green,blue,unknow)=(191,191,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>212 and green<255 and blue>212 and blue<255 :      # 48
        (red,green,blue,unknow)=(233,233,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    
    x=x+1

    if (x==255):
        x=0
        y=y+1


        
Image.show(i)

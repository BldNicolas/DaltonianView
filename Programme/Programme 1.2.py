from PIL.Image import *

i = open("image.png")

x = 1
y = 2
(r,v,b) = i.getpixel((x,y)) 
print (r, v, b)

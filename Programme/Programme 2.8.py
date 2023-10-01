from PIL.Image import *

import time

nom = str (input ("Nom de la photo. "))
l = int(input ("Entrez la longeur de la photo. "))
m = int(input ("Entrez la largeur de la photo. "))

i = open(nom)



# Debut du decompte du temps
start_time = time.time()

x = 0
y = 0
a=0

while (x<l) and (y<m) :
    (red,green,blue) = i.getpixel((x,y)) 
    if red <= 42 and green <= 42 and  blue <= 42:     # 1
        (red,green,blue,unknow)=(21,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    elif red <= 42 and green <= 42  and blue > 42 and blue <= 85:                # 2
        (red,green,blue,unknow)=(21,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red <= 42 and green <= 42 and blue > 85 and blue <= 128 :                # 3
        (red,green,blue,unknow)=(21,21,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red <= 42 and green <= 42 and blue <= 170 and blue > 128 :                 # 4
        (red,green,blue,unknow)=(21,21,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red <= 42 and green <= 42 and blue <= 212 and blue > 170 :                 # 5
        (red,green,blue,unknow)=(21,21,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red <= 42 and green <= 42 and blue >= 212 :                 # 6
        (red,green,blue,unknow)=(21,21,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue<=42 :      # 7
        (red,green,blue,unknow)=(21,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue<=42 :      # 8
        (red,green,blue,unknow)=(21,107,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue<42 :      # 9
        (red,green,blue,unknow)=(21,149,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue<=42 :      # 10
        (red,green,blue,unknow)=(21,191,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue<=42 :      # 11
        (red,green,blue,unknow)=(21,233,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue<=42 :      # 12
        (red,green,blue,unknow)=(64,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue<=42 :      # 13
        (red,green,blue,unknow)=(107,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green<=42 and blue<=42 :      # 14
        (red,green,blue,unknow)=(149,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42 and blue<=42 :      # 15
        (red,green,blue,unknow)=(191,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue<=42 :      # 16
        (red,green,blue,unknow)=(233,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue<=42 :      # 17
        (red,green,blue,unknow)=(64,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue<=42 :      # 18
        (red,green,blue,unknow)=(107,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue<=42 :      # 19
        (red,green,blue,unknow)=(149,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue<=42 :      # 20
        (red,green,blue,unknow)=(191,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue<=42 :      # 21
        (red,green,blue,unknow)=(233,64,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue<=42 :      # 22
        (red,green,blue,unknow)=(64,107,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue<=42 :      # 23
        (red,green,blue,unknow)=(64,149,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue<=42 :      # 24
        (red,green,blue,unknow)=(64,191,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue<=42 :      # 25
        (red,green,blue,unknow)=(64,233,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>42 and blue<=85 :      # 26
        (red,green,blue,unknow)=(64,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue>42 and blue<=85 :      # 27
        (red,green,blue,unknow)=(107,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green<=42 and blue>42 and blue<=85 :      # 28
        (red,green,blue,unknow)=(149,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42 and blue>42 and blue<=85 :      # 29
        (red,green,blue,unknow)=(191,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>42 and blue<=85 :      # 30
        (red,green,blue,unknow)=(233,21,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>85 and blue<=128 :      # 31
        (red,green,blue,unknow)=(64,21,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>128 and blue<=170 :      # 32
        (red,green,blue,unknow)=(64,21,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>170 and blue<=212 :      # 33
        (red,green,blue,unknow)=(64,21,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>212 :      # 34
        (red,green,blue,unknow)=(64,21,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>42 and blue<=85 :      # 35
        (red,green,blue,unknow)=(21,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue>42 and blue<=85 :      # 36
        (red,green,blue,unknow)=(21,107,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue>42 and blue<=85 :      # 37
        (red,green,blue,unknow)=(21,149,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue>42 and blue<=85 :      # 38
        (red,green,blue,unknow)=(21,191,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>42 and blue<=85 :      # 39
        (red,green,blue,unknow)=(21,233,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>85 and blue<=128 :      # 40
        (red,green,blue,unknow)=(21,64,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>128 and blue<=170 :      # 41
        (red,green,blue,unknow)=(21,64,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>170 and blue<=212 :      # 42
        (red,green,blue,unknow)=(21,64,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>212 :      # 43
        (red,green,blue,unknow)=(21,64,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>85 and blue<=128 :      # 44
        (red,green,blue,unknow)=(64,64,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>128 and blue<=170 :      # 45
        (red,green,blue,unknow)=(64,64,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>170 and blue<=212 :      # 46
        (red,green,blue,unknow)=(64,64,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>212 :      # 47
        (red,green,blue,unknow)=(64,64,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>42 and blue<=85 :      # 48
        (red,green,blue,unknow)=(64,107,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>42 and blue<=85 :      # 49
        (red,green,blue,unknow)=(64,149,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>42 and blue<=85 :      # 50
        (red,green,blue,unknow)=(64,191,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>42 and blue<=85 :      # 51
        (red,green,blue,unknow)=(64,233,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>42 and blue<=85 :      # 52
        (red,green,blue,unknow)=(107,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue>42 and blue<=85 :      # 53
        (red,green,blue,unknow)=(149,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue>42 and blue<=85 :      # 54
        (red,green,blue,unknow)=(191,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue>42 and blue<=85 :      # 55
        (red,green,blue,unknow)=(233,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>85 and blue<=128 :      # 56
        (red,green,blue,unknow)=(64,107,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>128 and blue<=170 :      # 57
        (red,green,blue,unknow)=(64,107,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>170 and blue<=212 :      # 58
        (red,green,blue,unknow)=(64,107,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>212 :      # 59
        (red,green,blue,unknow)=(64,107,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>85 and blue<=128 :      # 60
        (red,green,blue,unknow)=(64,149,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>85 and blue<=128 :      # 61
        (red,green,blue,unknow)=(64,191,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>85 and blue<=128 :      # 62
        (red,green,blue,unknow)=(64,233,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>85 and green<=128 and blue>42 and blue<=85 :      # 63
        (red,green,blue,unknow)=(107,107,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>42 and blue<=85 :      # 64
        (red,green,blue,unknow)=(149,107,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>85 and green<=128 and blue>42 and blue<=85 :      # 65
        (red,green,blue,unknow)=(191,107,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue>42 and blue<=85 :      # 66
        (red,green,blue,unknow)=(233,107,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>42 and blue<=85 :      # 67
        (red,green,blue,unknow)=(107,149,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>170 and green<=212 and blue>42 and blue<=85 :      # 68
        (red,green,blue,unknow)=(107,191,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue>42 and blue<=85 :      # 69
        (red,green,blue,unknow)=(107,233,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>85 and blue<=128 :      # 70
        (red,green,blue,unknow)=(107,64,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue>85 and blue<=128 :      # 71
        (red,green,blue,unknow)=(149,64,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue>85 and blue<=128 :      # 72
        (red,green,blue,unknow)=(191,64,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue>85 and blue<=128 :      # 73
        (red,green,blue,unknow)=(233,64,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>128 and blue<=170 :      # 74
        (red,green,blue,unknow)=(107,64,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>170 and blue<=212 :      # 75
        (red,green,blue,unknow)=(107,64,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>212  :      # 76
        (red,green,blue,unknow)=(107,64,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>128 and green<=170 and blue>85 and blue<=128 :      # 77
        (red,green,blue,unknow)=(149,149,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>85 and blue<=128 :      # 78
        (red,green,blue,unknow)=(191,149,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue>85 and blue<=128 :      # 79
        (red,green,blue,unknow)=(233,149,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>85 and blue<=128 :      # 80
        (red,green,blue,unknow)=(149,191,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue>85 and blue<=128 :      # 81
        (red,green,blue,unknow)=(149,233,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>128 and blue<=170 :      # 82
        (red,green,blue,unknow)=(149,107,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>85 and green<=128 and blue>128 and blue<=170 :      # 83
        (red,green,blue,unknow)=(191,107,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue>128 and blue<=170 :      # 84
        (red,green,blue,unknow)=(233,107,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>170 and blue<=212 :      # 85
        (red,green,blue,unknow)=(149,107,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>212 :      # 86
        (red,green,blue,unknow)=(149,107,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>128 and blue<=170 :      # 87
        (red,green,blue,unknow)=(107,149,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>170 and green<=212 and blue>128 and blue<=170 :      # 88
        (red,green,blue,unknow)=(107,191,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue>128 and blue<=170 :      # 89
        (red,green,blue,unknow)=(107,233,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>170 and blue<=212 :      # 90
        (red,green,blue,unknow)=(107,149,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>212 :      # 91
        (red,green,blue,unknow)=(107,149,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>170 and green<=212 and blue>128 and blue<=170 :      # 92
        (red,green,blue,unknow)=(191,191,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue>128 and blue<=170 :      # 93
        (red,green,blue,unknow)=(233,191,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue>128 and blue<=170 :      # 94
        (red,green,blue,unknow)=(191,233,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>170 and blue<=212 :      # 95
        (red,green,blue,unknow)=(191,149,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue>170 and blue<=212 :      # 96
        (red,green,blue,unknow)=(233,149,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>212 :      # 97
        (red,green,blue,unknow)=(191,149,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>170 and blue<=212 :      # 98
        (red,green,blue,unknow)=(149,191,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue>170 and blue<=212 :      # 99
        (red,green,blue,unknow)=(149,233,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>212 :      # 100
        (red,green,blue,unknow)=(149,191,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>170 and blue<=212 :      # 101
        (red,green,blue,unknow)=(149,191,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue>212 :      # 102
        (red,green,blue,unknow)=(191,233,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue>212 :      # 103
        (red,green,blue,unknow)=(233,191,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>212 and blue>170 and blue<=212 :      # 104
        (red,green,blue,unknow)=(233,233,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>42 and blue<=85 :      # 105
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>85 and green<=128 and blue>85 and blue<=128 :      # 106
        (red,green,blue,unknow)=(107,107,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>128 and green<=170 and blue>128 and blue<=170 :      # 107
        (red,green,blue,unknow)=(149,149,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>170 and green<=212 and blue>170 and blue<=212 :      # 108
        (red,green,blue,unknow)=(191,191,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>212 and blue>212 :      # 109
        (red,green,blue,unknow)=(233,233,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue<=42 :      # 110
        (red,green,blue,unknow)=(107,233,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue<=42 :      # 111
        (red,green,blue,unknow)=(149,233,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue<=42 :      # 112
        (red,green,blue,unknow)=(191,233,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue<=42 :      # 113
        (red,green,blue,unknow)=(233,107,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue<=42 :      # 114
        (red,green,blue,unknow)=(233,149,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue<=42 :      # 115
        (red,green,blue,unknow)=(233,191,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>85 and blue<=128 :      # 116
        (red,green,blue,unknow)=(233,21,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>128 and blue<=170 :      # 117
        (red,green,blue,unknow)=(233,21,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>170 and blue<=212 :      # 118
        (red,green,blue,unknow)=(233,21,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue>212 :      # 119
        (red,green,blue,unknow)=(107,21,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green<=42 and blue>212 :      # 120
        (red,green,blue,unknow)=(149,21,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42 and blue>212 :      # 121
        (red,green,blue,unknow)=(191,21,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>85 and blue<=128 :      # 122
        (red,green,blue,unknow)=(21,233,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>128 and blue<=170 :      # 123
        (red,green,blue,unknow)=(21,233,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>170 and blue<=212 :      # 124
        (red,green,blue,unknow)=(21,233,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue>212 :      # 125
        (red,green,blue,unknow)=(21,107,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue>212 :      # 126
        (red,green,blue,unknow)=(21,149,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue>212 :      # 127
        (red,green,blue,unknow)=(21,191,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>212 :      # 128
        (red,green,blue,unknow)=(64,149,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>212 :      # 129
        (red,green,blue,unknow)=(64,191,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>212 :      # 130
        (red,green,blue,unknow)=(64,233,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>170 and blue<=212 :      # 131
        (red,green,blue,unknow)=(64,233,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>128 and blue<=170 :      # 132
        (red,green,blue,unknow)=(64,233,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212  and blue>85 and blue<=128 :      # 133
        (red,green,blue,unknow)=(107,233,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212  and blue>128 and blue<=170 :      # 134
        (red,green,blue,unknow)=(149,233,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212  and blue>170 and blue<=212 :      # 135
        (red,green,blue,unknow)=(191,233,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    x=x+1
    
    if (x==(l-1)):
        x=0
        y=y+1

print("Temps d execution pixelise : %s secondes " % (time.time() - start_time))

Image.show(i)

x = 0
y = 0

while (x<l) and (y<m) :
    (red,green,blue) = i.getpixel((x,y)) 
    if red <= 42 and green <= 42 and  blue <= 42:     # 1
        (red,green,blue,unknow)=(23,20,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    elif red <= 42 and green <= 42  and blue > 42 and blue <= 85:                # 2
        (red,green,blue,unknow)=(0,28,47,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red <= 42 and green <= 42 and blue > 85 and blue <= 128 :                # 3
        (red,green,blue,unknow)=(0,38,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red <= 42 and green <= 42 and blue <= 170 and blue > 128 :                 # 4
        (red,green,blue,unknow)=(0,50,83,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red <= 42 and green <= 42 and blue <= 212 and blue > 170 :                 # 5
        (red,green,blue,unknow)=(0,62,104,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red <= 42 and green <= 42 and blue > 212 :                 # 6
        (red,green,blue,unknow)=(0,75,124,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue<=42 :      # 7
        (red,green,blue,unknow)=(68,52,25,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue<=42 :      # 8
        (red,green,blue,unknow)=(114,86,30,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue<=42 :      # 9
        (red,green,blue,unknow)=(160,121,38,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue<=42 :      # 10
        (red,green,blue,unknow)=(205,155,46,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue<=42 :      # 11
        (red,green,blue,unknow)=(250,189,54,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue<=42 :      # 12
        (red,green,blue,unknow)=(44,34,19,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue<=42 :      # 13
        (red,green,blue,unknow)=(70,53,14,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170  and green<=42 and blue<=42 :      # 14
        (red,green,blue,unknow)=(97,73,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42  and blue<=42 :      # 15
        (red,green,blue,unknow)=(123,93,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and  green<=42 and blue<=42 :      # 16
        (red,green,blue,unknow)=(149,112,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue<=42 :      # 17
        (red,green,blue,unknow)=(76,58,23,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue<=42 :      # 18
        (red,green,blue,unknow)=(93,70,18,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue<=42 :      # 19
        (red,green,blue,unknow)=(114,85,6,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue<=42 :      # 20
        (red,green,blue,unknow)=(136,102,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue<=42 :      # 21
        (red,green,blue,unknow)=(160,120,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue<=42 :      # 22
        (red,green,blue,unknow)=(119,90,29,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue<=42 :      # 23
        (red,green,blue,unknow)=(163,123,37,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue<=42 :      # 24
        (red,green,blue,unknow)=(207,157,45,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue<=42 :      # 25
        (red,green,blue,unknow)=(252,190,53,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>42 and blue<=85 :      # 26
        (red,green,blue,unknow)=(29,39,60,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue>42 and blue<=85 :      # 27
        (red,green,blue,unknow)=(65,57,59,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green<=42 and blue>42 and blue<=85 :      # 28
        (red,green,blue,unknow)=(93,75,57,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42 and blue>42 and blue<=85 :      # 29
        (red,green,blue,unknow)=(120,94,54,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>=212 and green<=42 and blue>42 and blue<=85 :      # 30
        (red,green,blue,unknow)=(148,113,51,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>85 and blue<=128 :      # 31
        (red,green,blue,unknow)=(0,48,82,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>128 and blue<=170 :      # 32
        (red,green,blue,unknow)=(0,57,97,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>170 and blue<=212 :      # 33
        (red,green,blue,unknow)=(0,68,114,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>212 :      # 34
        (red,green,blue,unknow)=(0,80,133,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>42 and blue<=85 :      # 35
        (red,green,blue,unknow)=(59,55,65,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue>42 and blue<=85 :      # 36
        (red,green,blue,unknow)=(109,88,97,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue>42 and blue<=85 :      # 37
        (red,green,blue,unknow)=(157,122,70,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue>42 and blue<=85 :      # 38
        (red,green,blue,unknow)=(203,156,74,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>42 and blue<=85 :      # 39
        (red,green,blue,unknow)=(248,190,79,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>85 and blue<=128 :      # 40
        (red,green,blue,unknow)=(27,62,106,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>128 and blue<=170 :      # 41
        (red,green,blue,unknow)=(0,70,121,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>170 and blue<=212 :      # 42
        (red,green,blue,unknow)=(0,79,134,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>212 :      # 43
        (red,green,blue,unknow)=(0,89,150,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>85 and blue<=128 :      # 44
        (red,green,blue,unknow)=(46,67,106,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>128 and blue<=170 :      # 45
        (red,green,blue,unknow)=(0,76,132,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>170 and blue<=212 :      # 46
        (red,green,blue,unknow)=(0,84,143,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>212 :      # 47
        (red,green,blue,unknow)=(0,94,158,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>42 and blue<=85 :      # 48
        (red,green,blue,unknow)=(115,93,67,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>42 and blue<=85 :      # 49
        (red,green,blue,unknow)=(160,125,71,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>42 and blue<=85 :      # 50
        (red,green,blue,unknow)=(205,158,75,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>42 and blue<=85 :      # 51
        (red,green,blue,unknow)=(250,191,80,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>42 and blue<=85 :      # 52
        (red,green,blue,unknow)=(88,73,62,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue>42 and blue<=85 :      # 53
        (red,green,blue,unknow)=(110,88,60,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue>42 and blue<=85 :      # 54
        (red,green,blue,unknow)=(134,104,57,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue>42 and blue<=85 :      # 55
        (red,green,blue,unknow)=(159,122,54,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>85 and blue<=128 :      # 56
        (red,green,blue,unknow)=(104,97,109,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>128 and blue<=170 :      # 57
        (red,green,blue,unknow)=(85,103,150,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>170 and blue<=212 :      # 58
        (red,green,blue,unknow)=(41,110,190,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>212 :      # 59
        (red,green,blue,unknow)=(0,118,205,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>85 and blue<=128 :      # 60
        (red,green,blue,unknow)=(153,128,112,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>85 and blue<=128 :      # 61
        (red,green,blue,unknow)=(200,160,114,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>85 and blue<=128 :      # 62
        (red,green,blue,unknow)=(246,193,118,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>85 and green<=128 and blue>42 and blue<=85 :      # 63
        (red,green,blue,unknow)=(126,100,66,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>42 and blue<=85 :      # 64
        (red,green,blue,unknow)=(142,110,63,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>85 and green<=128 and blue>42 and blue<=85 :      # 65
        (red,green,blue,unknow)=(160,123,60,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue>42 and blue<=85 :      # 66
        (red,green,blue,unknow)=(181,138,57,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>42 and blue<=85 :      # 67
        (red,green,blue,unknow)=(168,130,69,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>170 and green<=212 and blue>42 and blue<=85 :      # 68
        (red,green,blue,unknow)=(211,162,74,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue>42 and blue<=85 :      # 69
        (red,green,blue,unknow)=(255,194,79,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>85 and blue<=128 :      # 70
        (red,green,blue,unknow)=(74,78,104,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue>85 and blue<=128 :      # 71
        (red,green,blue,unknow)=(100,92,103,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue>85 and blue<=128 :      # 72
        (red,green,blue,unknow)=(126,107,101,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue>85 and blue<=128 :      # 73
        (red,green,blue,unknow)=(153,124,99,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>128 and blue<=170 :      # 74
        (red,green,blue,unknow)=(41,86,145,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>170 and blue<=212 :      # 75
        (red,green,blue,unknow)=(0,94,162,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>212 :      # 76
        (red,green,blue,unknow)=(0,102,174,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>128 and green<=170 and blue>85 and blue<=128 :      # 77
        (red,green,blue,unknow)=(173,140,109,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>85 and blue<=128 :      # 78
        (red,green,blue,unknow)=(188,150,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue>85 and blue<=128 :      # 79
        (red,green,blue,unknow)=(206,162,104,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>85 and blue<=128 :      # 80
        (red,green,blue,unknow)=(215,170,112,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue>85 and blue<=128 :      # 81
        (red,green,blue,unknow)=(255,202,124,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>128 and blue<=170 :      # 82
        (red,green,blue,unknow)=(120,119,147,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>85 and green<=128 and blue>128 and blue<=170 :      # 83
        (red,green,blue,unknow)=(142,130,145,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue>128 and blue<=170 :      # 84
        (red,green,blue,unknow)=(166,144,143,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>170 and blue<=212 :      # 85
        (red,green,blue,unknow)=(98,125,187,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>212 :      # 86
        (red,green,blue,unknow)=(55,133,227,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>128 and blue<=170 :      # 87
        (red,green,blue,unknow)=(150,137,152,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>170 and green<=212 and blue>128 and blue<=170 :      # 88
        (red,green,blue,unknow)=(107,191,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue>128 and blue<=170 :      # 89
        (red,green,blue,unknow)=(244,199,157,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>170 and blue<=212 :      # 90
        (red,green,blue,unknow)=(132,142,192,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>212 :      # 91
        (red,green,blue,unknow)=(106,149,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>170 and green<=212 and blue>128 and blue<=170 :      # 92
        (red,green,blue,unknow)=(219,181,151,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue>128 and blue<=170 :      # 93
        (red,green,blue,unknow)=(234,191,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue>128 and blue<=170 :      # 94
        (red,green,blue,unknow)=(255,212,167,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>170 and blue<=212 :      # 95
        (red,green,blue,unknow)=(166,159,189,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue>170 and blue<=212 :      # 96
        (red,green,blue,unknow)=(186,170,187,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>212 :      # 97
        (red,green,blue,unknow)=(147,165,230,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>170 and blue<=212 :      # 98
        (red,green,blue,unknow)=(195,177,194,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue>170 and blue<=212 :      # 99
        (red,green,blue,unknow)=(242,207,196,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>212 :      # 100
        (red,green,blue,unknow)=(179,183,235,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>170 and blue<=212 :      # 101
        (red,green,blue,unknow)=(195,177,194,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue>212 :      # 102
        (red,green,blue,unknow)=(241,218,236,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue>212 :      # 103
        (red,green,blue,unknow)=(212,199,231,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>212 and blue>170 and blue<=212 :      # 104
        (red,green,blue,unknow)=(255,224,206,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>42 and blue<=85 :      # 105
        (red,green,blue,unknow)=(70,62,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>85 and green<=128 and blue>85 and blue<=128 :      # 106
        (red,green,blue,unknow)=(117,104,108,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>128 and green<=170 and blue>128 and blue<=170 :      # 107
        (red,green,blue,unknow)=(163,144,150,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>170 and green<=212 and blue>170 and blue<=212 :      # 108
        (red,green,blue,unknow)=(209,185,192,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>212 and blue>212 :      # 109
        (red,green,blue,unknow)=(255,226,234,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue<=42 :      # 110
        (red,green,blue,unknow)=(255,194,65,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue<=42 :      # 111
        (red,green,blue,unknow)=(255,200,102,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue<=42 :      # 112
        (red,green,blue,unknow)=(255,209,137,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue<=42 :      # 113
        (red,green,blue,unknow)=(183,137,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue<=42 :      # 114
        (red,green,blue,unknow)=(212,159,0,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue<=42 :      # 115
        (red,green,blue,unknow)=(147,185,27,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>85 and blue<=128 :      # 116
        (red,green,blue,unknow)=(141,117,97,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>128 and blue<=170 :      # 117
        (red,green,blue,unknow)=(130,121,139,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>170 and blue<=212 :      # 118
        (red,green,blue,unknow)=(112,127,179,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue>212 :      # 119
        (red,green,blue,unknow)=(0,90,151,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green<=42 and blue>212 :      # 120
        (red,green,blue,unknow)=(0,104,177,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42 and blue>212 :      # 121
        (red,green,blue,unknow)=(0,119,209,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>85 and blue<=128 :      # 122
        (red,green,blue,unknow)=(244,192,118,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>128 and blue<=170 :      # 123
        (red,green,blue,unknow)=(237,194,158,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>170 and blue<=212 :      # 124
        (red,green,blue,unknow)=(227,198,199,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue>212 :      # 125
        (red,green,blue,unknow)=(0,115,198,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue>212 :      # 126
        (red,green,blue,unknow)=(83,143,234,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue>212 :      # 127
        (red,green,blue,unknow)=(156,172,237,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>212 :      # 128
        (red,green,blue,unknow)=(91,145,234,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>212 :      # 129
        (red,green,blue,unknow)=(159,174,237,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>212 :      # 130
        (red,green,blue,unknow)=(216,204,239,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>170 and blue<=212 :      # 131
        (red,green,blue,unknow)=(229,199,198,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>128 and blue<=170 :      # 132
        (red,green,blue,unknow)=(239,196,158,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212  and blue>85 and blue<=128 :      # 133
        (red,green,blue,unknow)=(251,196,117,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212  and blue>128 and blue<=170 :      # 134
        (red,green,blue,unknow)=(251,204,156,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212  and blue>170 and blue<=212 :      # 135
        (red,green,blue,unknow)=(253,213,195,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    x=x+1
    
    if (x==(l-1)):
        x=0
        y=y+1

# Affichage du temps d execution
print("Temps d execution deuteranope : %s secondes " % (time.time() - start_time))

Image.show(i)

while (x<l) and (y<m) :
    (red,green,blue) = i.getpixel((x,y)) 
    if red <= 42 and green <= 42 and  blue <= 42:     # 1
        (red,green,blue,unknow)=(21,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
    elif red <= 42 and green <= 42  and blue > 42 and blue <= 85:                # 2
        (red,green,blue,unknow)=(0,30,32,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red <= 42 and green <= 42 and blue > 85 and blue <= 128 :                # 3
        (red,green,blue,unknow)=(0,41,43,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    elif red <= 42 and green <= 42 and blue <= 170 and blue > 128 :                 # 4
        (red,green,blue,unknow)=(0,54,56,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red <= 42 and green <= 42 and blue <= 212 and blue > 170 :                 # 5
        (red,green,blue,unknow)=(0,67,70,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red <= 42 and green <= 42 and blue > 212 :                 # 6
        (red,green,blue,unknow)=(0,81,84,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue<=42 :      # 7
        (red,green,blue,unknow)=(32,59,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue<=42 :      # 8
        (red,green,blue,unknow)=(48,99,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue<=42 :      # 9
        (red,green,blue,unknow)=(65,139,150,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue<=42 :      # 10
        (red,green,blue,unknow)=(82,178,192,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue<=42 :      # 11
        (red,green,blue,unknow)=(99,217,234,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue<=42 :      # 12
        (red,green,blue,unknow)=(63,21,22,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue<=42 :      # 13
        (red,green,blue,unknow)=(106,21,21,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170  and green<=42 and blue<=42 :      # 14
        (red,green,blue,unknow)=(149,21,19,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42  and blue<=42 :      # 15
        (red,green,blue,unknow)=(191,22,16,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and  green<=42 and blue<=42 :      # 16
        (red,green,blue,unknow)=(233,22,10,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue<=42 :      # 17
        (red,green,blue,unknow)=(67,59,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue<=42 :      # 18 fini
        (red,green,blue,unknow)=(108,59,63,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue<=42 :      # 19
        (red,green,blue,unknow)=(150,59,63,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue<=42 :      # 20
        (red,green,blue,unknow)=(192,59,62,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue<=42 :      # 21
        (red,green,blue,unknow)=(234,59,62,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue<=42 :      # 22
        (red,green,blue,unknow)=(75,99,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue<=42 :      # 23
        (red,green,blue,unknow)=(86,139,150,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue<=42 :      # 24
        (red,green,blue,unknow)=(99,178,192,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue<=42 :      # 25
        (red,green,blue,unknow)=(113,217,234,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>42 and blue<=85 :      # 26
        (red,green,blue,unknow)=(60,31,33,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue>42 and blue<=85 :      # 27
        (red,green,blue,unknow)=(107,31,32,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green<=42 and blue>42 and blue<=85 :      # 28
        (red,green,blue,unknow)=(148,31,31,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42 and blue>42 and blue<=85 :      # 29
        (red,green,blue,unknow)=(190,31,30,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>=212 and green<=42 and blue>42 and blue<=85 :      # 30
        (red,green,blue,unknow)=(232,31,27,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>85 and blue<=128 :      # 31
        (red,green,blue,unknow)=(50,45,48,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>128 and blue<=170 :      # 32
        (red,green,blue,unknow)=(29,60,65,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>170 and blue<=212 :      # 33
        (red,green,blue,unknow)=(0,73,78,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green<=42 and blue>212 :      # 34
        (red,green,blue,unknow)=(0,86,91,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>42 and blue<=85 :      # 35
        (red,green,blue,unknow)=(23,62,67,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue>42 and blue<=85 :      # 36
        (red,green,blue,unknow)=(43,101,109,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue>42 and blue<=85 :      # 37
        (red,green,blue,unknow)=(61,140,151,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue>42 and blue<=85 :      # 38
        (red,green,blue,unknow)=(79,179,193,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>42 and blue<=85 :      # 39
        (red,green,blue,unknow)=(97,217,235,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>85 and blue<=128 :      # 40
        (red,green,blue,unknow)=(0,69,74,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>128 and blue<=170 :      # 41
        (red,green,blue,unknow)=(0,76,81,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>170 and blue<=212 :      # 42
        (red,green,blue,unknow)=(0,86,90,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>42 and green<=85 and blue>212 :      # 43
        (red,green,blue,unknow)=(0,96,101,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>85 and blue<=128 :      # 44
        (red,green,blue,unknow)=(55,70,75,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>128 and blue<=170 :      # 45
        (red,green,blue,unknow)=(40,80,87,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>170 and blue<=212 :      # 46
        (red,green,blue,unknow)=(0,91,98,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>212 :      # 47
        (red,green,blue,unknow)=(0,101,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>42 and blue<=85 :      # 48
        (red,green,blue,unknow)=(73,102,110,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>42 and blue<=85 :      # 49
        (red,green,blue,unknow)=(84,140,151,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>42 and blue<=85 :      # 50
        (red,green,blue,unknow)=(97,179,193,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>42 and blue<=85 :      # 51
        (red,green,blue,unknow)=(112,217,235,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>42 and blue<=85 :      # 52
        (red,green,blue,unknow)=(107,63,68,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue>42 and blue<=85 :      # 53
        (red,green,blue,unknow)=(149,63,68,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue>42 and blue<=85 :      # 54
        (red,green,blue,unknow)=(191,64,67,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue>42 and blue<=85 :      # 55
        (red,green,blue,unknow)=(233,64,66,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>85 and blue<=128 :      # 56
        (red,green,blue,unknow)=(66,106,114,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>128 and blue<=170 :      # 57
        (red,green,blue,unknow)=(53,112,121,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>170 and blue<=212 :      # 58
        (red,green,blue,unknow)=(20,120,130,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>85 and green<=128 and blue>212 :      # 59
        (red,green,blue,unknow)=(0,128,137,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>85 and blue<=128 :      # 60
        (red,green,blue,unknow)=(78,143,154,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>85 and blue<=128 :      # 61
        (red,green,blue,unknow)=(93,181,195,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>85 and blue<=128 :      # 62
        (red,green,blue,unknow)=(108,219,237,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>85 and green<=128 and blue>42 and blue<=85 :      # 63
        (red,green,blue,unknow)=(112,102,110,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>42 and blue<=85 :      # 64
        (red,green,blue,unknow)=(153,102,109,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>85 and green<=128 and blue>42 and blue<=85 :      # 65
        (red,green,blue,unknow)=(194,102,109,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue>42 and blue<=85 :      # 66
        (red,green,blue,unknow)=(235,102,108,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>42 and blue<=85 :      # 67
        (red,green,blue,unknow)=(119,140,151,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>170 and green<=212 and blue>42 and blue<=85 :      # 68
        (red,green,blue,unknow)=(128,179,193,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue>42 and blue<=85 :      # 69
        (red,green,blue,unknow)=(139,217,235,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>85 and blue<=128 :      # 70
        (red,green,blue,unknow)=(103,71,76,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>42 and green<=85 and blue>85 and blue<=128 :      # 71
        (red,green,blue,unknow)=(146,71,76,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>42 and green<=85 and blue>85 and blue<=128 :      # 72
        (red,green,blue,unknow)=(189,71,75,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>42 and green<=85 and blue>85 and blue<=128 :      # 73
        (red,green,blue,unknow)=(231,71,75,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>128 and blue<=170 :      # 74
        (red,green,blue,unknow)=(96,81,87,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>170 and blue<=212 :      # 75
        (red,green,blue,unknow)=(85,92,100,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>42 and green<=85 and blue>212 :      # 76
        (red,green,blue,unknow)=(67,105,114,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>128 and green<=170 and blue>85 and blue<=128 :      # 77
        (red,green,blue,unknow)=(155,143,154,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>85 and blue<=128 :      # 78
        (red,green,blue,unknow)=(195,143,154,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue>85 and blue<=128 :      # 79
        (red,green,blue,unknow)=(237,143,154,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>85 and blue<=128 :      # 80
        (red,green,blue,unknow)=(162,181,195,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue>85 and blue<=128 :      # 81
        (red,green,blue,unknow)=(170,219,237,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>128 and blue<=170 :      # 82
        (red,green,blue,unknow)=(145,112,121,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>85 and green<=128 and blue>128 and blue<=170 :      # 83
        (red,green,blue,unknow)=(188,112,121,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue>128 and blue<=170 :      # 84
        (red,green,blue,unknow)=(231,112,120,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>170 and blue<=212 :      # 85
        (red,green,blue,unknow)=(139,121,130,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>85 and green<=128 and blue>212 :      # 86
        (red,green,blue,unknow)=(129,131,141,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>128 and blue<=170 :      # 87
        (red,green,blue,unknow)=(109,147,159,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>170 and green<=212 and blue>128 and blue<=170 :      # 88
        (red,green,blue,unknow)=(119,184,199,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue>128 and blue<=170 :      # 89
        (red,green,blue,unknow)=(131,222,240,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>170 and blue<=212 :      # 90
        (red,green,blue,unknow)=(100,154,166,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>128 and green<=170 and blue>212 :      # 91
        (red,green,blue,unknow)=(86,161,174,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>170 and green<=212 and blue>128 and blue<=170 :      # 92
        (red,green,blue,unknow)=(198,184,199,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue>128 and blue<=170 :      # 93
        (red,green,blue,unknow)=(238,184,199,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue>128 and blue<=170 :      # 94
        (red,green,blue,unknow)=(204,222,240,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>170 and blue<=212 :      # 95
        (red,green,blue,unknow)=(187,154,166,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue>170 and blue<=212 :      # 96
        (red,green,blue,unknow)=(230,154,165,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>128 and green<=170 and blue>212 :      # 97
        (red,green,blue,unknow)=(181,161,174,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>170 and blue<=212 :      # 98
        (red,green,blue,unknow)=(152,189,204,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue>170 and blue<=212 :      # 99
        (red,green,blue,unknow)=(161,226,244,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>212 :      # 100
        (red,green,blue,unknow)=(144,195,211,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>170 and green<=212 and blue>170 and blue<=212 :      # 101
        (red,green,blue,unknow)=(152,189,204,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue>212 :      # 102
        (red,green,blue,unknow)=(194,231,249,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue>212 :      # 103
        (red,green,blue,unknow)=(230,195,210,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>212 and blue>170 and blue<=212 :      # 104
        (red,green,blue,unknow)=(240,226,243,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>42 and green<=85 and blue>42 and blue<=85 :      # 105
        (red,green,blue,unknow)=(65,63,68,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>85 and green<=128 and blue>85 and blue<=128 :      # 106
        (red,green,blue,unknow)=(108,106,114,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>128 and green<=170 and blue>128 and blue<=170 :      # 107
        (red,green,blue,unknow)=(151,147,159,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>170 and green<=212 and blue>170 and blue<=212 :      # 108
        (red,green,blue,unknow)=(193,189,204,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>212 and blue>212 :      # 109
        (red,green,blue,unknow)=(235,231,249,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green>212 and blue<=42 :      # 110
        (red,green,blue,unknow)=(140,217,234,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green>212 and blue<=42 :      # 111
        (red,green,blue,unknow)=(173,217,234,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green>212 and blue<=42 :      # 112
        (red,green,blue,unknow)=(210,217,234,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>85 and green<=128 and blue<=42 :      # 113
        (red,green,blue,unknow)=(236,100,106,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>128 and green<=170 and blue<=42 :      # 114
        (red,green,blue,unknow)=(239,139,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green>170 and green<=212 and blue<=42 :      # 115
        (red,green,blue,unknow)=(243,178,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>85 and blue<=128 :      # 116
        (red,green,blue,unknow)=(230,46,46,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>128 and blue<=170 :      # 117
        (red,green,blue,unknow)=(228,61,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and green<=42 and blue>170 and blue<=212 :      # 118
        (red,green,blue,unknow)=(224,77,81,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<=128 and green<=42 and blue>212 :      # 119
        (red,green,blue,unknow)=(63,92,99,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<=170 and green<=42 and blue>212 :      # 120
        (red,green,blue,unknow)=(123,92,99,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<=212 and green<=42 and blue>212 :      # 121
        (red,green,blue,unknow)=(172,93,99,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>85 and blue<=128 :      # 122
        (red,green,blue,unknow)=(92,219,237,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>128 and blue<=170 :      # 123
        (red,green,blue,unknow)=(84,222,240,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>212 and blue>170 and blue<=212 :      # 124
        (red,green,blue,unknow)=(71,226,244,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>85 and green<=128 and blue>212 :      # 125
        (red,green,blue,unknow)=(0,125,133,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>128 and green<=170 and blue>212 :      # 126
        (red,green,blue,unknow)=(0,158,170,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red<=42 and green>170 and green<=212 and blue>212 :      # 127
        (red,green,blue,unknow)=(0,194,209,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>128 and green<=170 and blue>212 :      # 128 pas faite
        (red,green,blue,unknow)=(64,149,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>170 and green<=212 and blue>212 :      # 129pas faite
        (red,green,blue,unknow)=(64,191,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>212 :      # 130
        (red,green,blue,unknow)=(64,233,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>170 and blue<=212 :      # 131pas faite
        (red,green,blue,unknow)=(64,233,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<=85 and green>212 and blue>128 and blue<=170 :      # 132pas faite
        (red,green,blue,unknow)=(64,233,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    x=x+1
    
    if (x==(l-1)):
        x=0
        y=y+1

print("Temps d execution tritanope : %s secondes " % (time.time() - start_time))

Image.show(i)

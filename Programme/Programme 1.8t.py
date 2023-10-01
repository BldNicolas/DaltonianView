from PIL.Image import *

nom = str (input ("Nom de la photo. "))

i = open(nom)

l = int(input ("Entrez la longeur de la photo. "))
m = int(input ("Entrez la largeur de la photo. "))


x = 0
y = 0
a = 0


while (x<l) and (y<m) :
    (red,green,blue) = i.getpixel((x,y)) 
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

    elif red>42 and red<85 and green>42 and green<85 and blue>85 and blue<128 :      # 44
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>42 and green<85 and blue>128 and blue<170 :      # 45
        (red,green,blue,unknow)=(107,107,107,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>42 and green<85 and blue>170 and blue<212 :      # 46
        (red,green,blue,unknow)=(149,149,149,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>42 and green<85 and blue>212 and blue<255 :      # 47
        (red,green,blue,unknow)=(191,191,191,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>85 and green<128 and blue>42 and blue<85 :      # 48
        (red,green,blue,unknow)=(233,233,233,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>128 and green<170 and blue>42 and blue<85 :      # 49
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>170 and green<212 and blue>42 and blue<85 :      # 50
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>212 and green<255 and blue>42 and blue<85 :      # 51
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>42 and green<85 and blue>42 and blue<85 :      # 52
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>42 and green<85 and blue>42 and blue<85 :      # 53
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>42 and green<85 and blue>42 and blue<85 :      # 54
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>42 and green<85 and blue>42 and blue<85 :      # 55
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>85 and green<128 and blue>85 and blue<128 :      # 56
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>85 and green<128 and blue>128 and blue<170 :      # 57
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>85 and green<128 and blue>170 and blue<212 :      # 58
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>85 and green<128 and blue>212 and blue<255 :      # 59
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>128 and green<170 and blue>85 and blue<128 :      # 60
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>170 and green<212 and blue>85 and blue<128 :      # 61
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>212 and green<255 and blue>85 and blue<128 :      # 62
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>85 and green<128 and blue>42 and blue<85 :      # 63
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>85 and green<128 and blue>42 and blue<85 :      # 64
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>85 and green<128 and blue>42 and blue<85 :      # 65
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>85 and green<128 and blue>42 and blue<85 :      # 66
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>128 and green<170 and blue>42 and blue<85 :      # 67
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>170 and green<212 and blue>42 and blue<85 :      # 68
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>212 and green<255 and blue>42 and blue<85 :      # 69
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>42 and green<85 and blue>85 and blue<128 :      # 70
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>42 and green<85 and blue>85 and blue<128 :      # 71
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>42 and green<85 and blue>85 and blue<128 :      # 72
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>42 and green<85 and blue>85 and blue<128 :      # 73
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>42 and green<85 and blue>128 and blue<170 :      # 74
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>42 and green<85 and blue>170 and blue<212 :      # 75
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>42 and green<85 and blue>212 and blue<255 :      # 76
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>128 and green<170 and blue>85 and blue<128 :      # 77
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>128 and green<170 and blue>85 and blue<128 :      # 78
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>128 and green<170 and blue>85 and blue<128 :      # 79
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>170 and green<212 and blue>85 and blue<128 :      # 80
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>212 and green<255 and blue>85 and blue<128 :      # 81
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>85 and green<128 and blue>128 and blue<170 :      # 82
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>85 and green<128 and blue>128 and blue<170 :      # 83
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>85 and green<128 and blue>128 and blue<170 :      # 84
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>85 and green<128 and blue>170 and blue<212 :      # 85
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>85 and green<128 and blue>212 and blue<255 :      # 86
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>128 and green<170 and blue>128 and blue<170 :      # 87
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>170 and green<212 and blue>128 and blue<170 :      # 88
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>212 and green<255 and blue>128 and blue<170 :      # 89
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>128 and green<170 and blue>170 and blue<212 :      # 90
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>128 and green<170 and blue>212 and blue<255 :      # 91
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>170 and green<212 and blue>128 and blue<170 :      # 92
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>170 and green<212 and blue>128 and blue<170 :      # 93
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>212 and green<255 and blue>128 and blue<170 :      # 94
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>128 and green<170 and blue>170 and blue<212 :      # 95
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>128 and green<170 and blue>170 and blue<212 :      # 96
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>128 and green<170 and blue>212 and blue<255 :      # 97
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>170 and green<212 and blue>170 and blue<212 :      # 98
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>212 and green<255 and blue>170 and blue<212 :      # 99
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>170 and green<212 and blue>212 and blue<255 :      # 100
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>170 and green<212 and blue>170 and blue<212 :      # 101
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>212 and green<255 and blue>212 and blue<255 :      # 102
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>170 and green<212 and blue>212 and blue<255 :      # 103
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>212 and green<255 and blue>170 and blue<212 :      # 104
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>42 and red<85 and green>42 and green<85 and blue>42 and blue<85 :      # 105
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>85 and red<128 and green>85 and green<128 and blue>85 and blue<128 :      # 106
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>128 and red<170 and green>128 and green<170 and blue>128 and blue<170 :      # 107
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>170 and red<212 and green>170 and green<212 and blue>170 and blue<212 :      # 108
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))

    elif red>212 and red<255 and green>212 and green<255 and blue>212 and blue<255 :      # 108
        (red,green,blue,unknow)=(64,64,64,255)
        i.putpixel((x,y,),(red,green,blue,unknow))
        
    x=x+1

    if (x==(l-1)):
        x=0
        y=y+1


        
Image.show(i)

from PIL.Image import *                                 #Ouverture bibliothèque

i = open("paysage.bpm")                                 #Ouverture du fichier
Image.show(i)

(rouge,vert,bleu) = i.getpixel((x,y))                   #Récupération des données
print (rouge, vert, bleu)


#################################
            #Tritanopia
#################################


(rouge,vert,bleu) = (132,122,191)                       #rouge
i.putpixel((x,y),(rouge,vert,bleu))


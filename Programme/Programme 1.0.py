
nomFichierSource = 'paysage.jpg'
nomFichierSortie = 'modifie.pgm'

nbLigne = 512
nbCol = 512

ligne = []
image = []

###############################################
# LECTURE DU FICHIER SOURCE
###############################################
fichierSource = open(nomFichierSource,'rb')
tailleFichier = len(fichierSource.read())

tailleEnTete = tailleFichier - nbLigne*nbCol

fichierSource.seek(0)

entete = fichierSource.read(tailleEnTete)

for ctrLig in range(nbLigne):
    
    for ctrCol in range(nbCol):
        pixel = fichierSource.read(1)
        ligne.append(pixel[0])

    image.append(ligne)
    ligne = []
    
fichierSource.close()

###############################################
# TRAITEMENT DE L'IMAGE
###############################################
for ctrLig in range(nbLigne):
    for ctrCol in range (nbCol):
        if image[ctrLig][ctrCol]>122:
            image[ctrLig][ctrCol]=255
        else:
            image[ctrLig][ctrCol]=0

###############################################
# ECRITURE DANS LE FICHIER DESTINATION
###############################################
fichierSortie = open(nomFichierSortie, 'wb')
fichierSortie.write(entete)

sortie = bytearray()

for ctrLig in range(nbLigne):
    for ctrCol in range (nbCol):
        sortie.append(image[ctrLig][ctrCol])

fichierSortie.write(sortie)

fichierSortie.close()






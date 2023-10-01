from tkinter import *
fenetre = Tk()
def selection():
    a=liste.curselection() #choix fait
    print("Vous avez choisi :", liste.get(a),a)
liste = Listbox(fenetre)
bouton=Button(fenetre, text="Appuyez pour choisir", command=selection)
bouton.pack()
liste.insert(1, "Deutéranope")
liste.insert(2, "Tritanope")
liste.insert(3, "Protanope")


liste.pack()
liste.curselection()

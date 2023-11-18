from tkinter import *
import tkinter

fenetre = Tk()
fenetre.geometry('700x200')
fenetre.title('Gestion des matrices')
fenetre['bg']='pink'
label=Label (fenetre,text="Choisir un traiment",background='pink',font=("Times New Roman",20,"italic bold")).pack()


    

def passer_a_resolution():
    # Fermer la fenêtre actuelle
    fenetre.destroy()

    # Créer et afficher une nouvelle fenêtre de résolution
    nouvelle_fenetre = Tk()
    nouvelle_fenetre.geometry('700x700')
    nouvelle_fenetre.title('Résolution')
    nouvelle_fenetre['bg'] = 'mistyrose1'

    # Ajoutez les éléments de la nouvelle fenêtre ici

    nouvelle_fenetre.mainloop()

def passer_a_matrice_x_vecteur():
    # Fermer la fenêtre actuelle
    fenetre.destroy()

    # Créer et afficher une nouvelle fenêtre de résolution
    nouvelle_fenetre = Tk()
    nouvelle_fenetre.geometry('700x700')
    nouvelle_fenetre.title('matrice x vecteur')
    nouvelle_fenetre['bg'] = 'mistyrose1'
    def saisie():
        label=Label (nouvelle_fenetre,text="multiplication",background='mistyrose1',font=("Times New Roman",20,"italic ")).pack()

    # Ajoutez les éléments de la nouvelle fenêtre ici
    menu1=Menu(nouvelle_fenetre)
     #sous onglet
    les_types=Menu(menu1,background='mistyrose1')
    les_types.add_command(label="dense", command=saisie, background='darksalmon')
    les_types.add_command(label="bande", command=saisie, background='darksalmon')
    les_types.add_command(label="demi_bande", command=saisie, background='darksalmon')
    les_types.add_command(label="symetrique", command=saisie, background='darksalmon')
    les_types.add_command(label="triangulaire superieure", command=saisie, background='darksalmon')
    les_types.add_command(label="triangulaire inferieure", command=saisie, background='darksalmon')
    les_types.add_command(label="demi triangulaire inferieure", command=saisie, background='darksalmon')
    les_types.add_command(label="demi triangulaire superieure", command=saisie, background='darksalmon')




     #principles
    menu1.add_cascade(label="les types",menu=les_types,background='pink')

    # Associez le menu à la fenêtre principale
    nouvelle_fenetre.config(menu=menu1)
    nouvelle_fenetre.mainloop()
   

def passer_a_matrice_x_matrice():
    # Fermer la fenêtre actuelle
    fenetre.destroy()

    # Créer et afficher une nouvelle fenêtre de résolution
    nouvelle_fenetre = Tk()
    nouvelle_fenetre.geometry('700x700')
    nouvelle_fenetre.title('matrice x matrice')
    nouvelle_fenetre['bg'] = 'mistyrose1'
    def saisie():
        label=Label (nouvelle_fenetre,text="multiplication",background='mistyrose1',font=("Times New Roman",20,"italic bold")).pack()

    # Ajoutez les éléments de la nouvelle fenêtre ici

     
    menu2=Menu(nouvelle_fenetre)
    #sous onglet
    les_types=Menu(menu2,background='mistyrose1')
    les_types.add_command(label="dense x dense", command=saisie, background='darksalmon')
    les_types.add_command(label="dense x transpose", command=saisie, background='darksalmon')
    les_types.add_command(label="bande x bande", command=saisie, background='darksalmon')
    les_types.add_command(label="dense x bande", command=saisie, background='darksalmon')
    les_types.add_command(label="bande x dense", command=saisie, background='darksalmon')
    les_types.add_command(label="dense x demi_bande", command=saisie, background='darksalmon')
    les_types.add_command(label="demi_bande x dense", command=saisie, background='darksalmon')
    les_types.add_command(label="dense xtriangulaire inferieure ", command=saisie, background='darksalmon')
    les_types.add_command(label="dense xtriangulaire superieure ", command=saisie, background='darksalmon')
    les_types.add_command(label="bande xtriangulaire inferieure ", command=saisie, background='darksalmon')
    les_types.add_command(label="bande xtriangulaire superieure ", command=saisie, background='darksalmon')
    les_types.add_command(label="triangulaire inferieure x triangulaire inferieure", command=saisie, background='darksalmon')
    les_types.add_command(label="triangulaire superieure x triangulaire superieure", command=saisie, background='darksalmon')
    les_types.add_command(label="triangulaire inferieure x triangulaire superieure", command=saisie, background='darksalmon')
    les_types.add_command(label="triangulaire superieure x triangulaire inferieure", command=saisie, background='darksalmon')
    les_types.add_command(label="demi triangulaire superieure x demi triangulaire inferieure", command=saisie, background='darksalmon')

    #principles
    menu2.add_cascade(label="les types",menu=les_types,background='pink')
  

    # Associez le menu à la fenêtre principale
    nouvelle_fenetre.config(menu=menu2)
    nouvelle_fenetre.mainloop()


mon_menu=Menu(fenetre)
#sous onglet matrice x vecteur
matrice_x_vecteur=Menu(mon_menu)

#sous onglet matrice x matrice
matrice_x_matrice=Menu(mon_menu)
#sous onglet multiplication
Multiplication=Menu(mon_menu,background='pink')
Multiplication.add_command(label="passer à la matrice x vecteur",command=passer_a_matrice_x_vecteur,background='red')
Multiplication.add_command(label="passer à la matrice x matrice",command=passer_a_matrice_x_matrice,background='red')
#sous onglet resolution
resolution=Menu(mon_menu,background='pink')
resolution.add_command(label="Passer à la résolution", command=passer_a_resolution, background='red')
#principles
mon_menu.add_cascade(label="Multiplication",menu=Multiplication,background='pink')
mon_menu.add_cascade(label="Résolution", menu=resolution, background='pink')

# Associez le menu à la fenêtre principale
fenetre.config(menu=mon_menu)
fenetre.mainloop()

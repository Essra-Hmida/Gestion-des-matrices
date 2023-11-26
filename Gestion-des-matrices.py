from tkinter import *
import tkinter
import random
from PIL import Image, ImageTk


fenetre = Tk()

fenetre.title('Gestion des matrices')
fenetre['bg']='#F0EAD2'
#fenetre.iconbitmap('M.ico')

image_path = r"C:\Users\essra hmida\Downloads\istockphoto-1457115338-612x612 (5).jpg"  # Use a raw string
original_image = Image.open(image_path)
converted_image = ImageTk.PhotoImage(original_image)
# Get the width and height of the image
image_width = converted_image.width()
image_height = converted_image.height()

# Set the window size to match the image size
fenetre.geometry(f"{image_width}x{image_height}")
# Create a label to hold the image
background_label = Label(fenetre, image=converted_image)
background_label.place(relwidth=1, relheight=1)
label=Label (fenetre,text="Gestion des matrices \n  Bienvenue!On est ici pour t'aider à faire des divers  opérations sur les matrices \n  n'hésitez pas de choisir l'opréation que vous voulez faire",font=("Times New Roman",15,"italic bold"),relief="raised",highlightthickness=6 , borderwidth=5)
label.pack()
label.place(x=150,y=20)
    
 
    



    

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
    

    
    nouvelle_fenetre.mainloop()
   

def passer_a_matrice_x_matrice():
    # Fermer la fenêtre actuelle
    fenetre.destroy()

    # Créer et afficher une nouvelle fenêtre de résolution
    nouvelle_fenetre = Tk()
    nouvelle_fenetre.geometry('800x800')
    nouvelle_fenetre.title('matrice x matrice')
    nouvelle_fenetre['bg'] = '#BCD2EE'
    label=Label (nouvelle_fenetre,text="Choisir le type de votre matrice",font=("Times New Roman",15,"italic bold"),relief="raised",highlightthickness=6 , borderwidth=5)
    label.pack()
    label.place(x=250,y=15)
   

    nouvelle_fenetre.mainloop()


button=Button(text="Multiplication matrice × vecteur",command=passer_a_matrice_x_vecteur,width=30,height= 2, relief='raised', highlightthickness=6 , borderwidth=5,font=("Times New Roman",15,"italic bold"))
button.pack()
button.place(x=600, y=200)
button=Button(text="Multiplication matrice × matrice",command=passer_a_matrice_x_matrice,width=30,height= 2, relief='raised', highlightthickness=6 , borderwidth=5,font=("Times New Roman",15,"italic bold"))
button.pack()
button.place(x=600, y=300) 
button=Button(text="Résolution",command=passer_a_resolution,width=30,height= 2, relief='raised', highlightthickness=6 , borderwidth=5,font=("Times New Roman",15,"italic bold"))
button.pack()
button.place(x=600, y=400)  

fenetre.mainloop()

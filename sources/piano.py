import tkinter
from classes import *


# Dico de l'octave 3, celui du milieu

keymap3 = {
    "s" : "do",
    "S" : "do#",
    "d" : "re", 
    "D" : "re#",
    "f" : "mi",
    "g" : "fa", 
    "G" : "fa#",
    "h" : "sol",
    "H" : "sol#",
    "j" : "la",
    "J" : "la#",
    "k" : "si"
}  

#Dico de l'octave 2

keymap2 = {
    "z" : "do",
    "Z" : "do#",
    "e" : "re", 
    "E" : "re#",
    "r" : "mi",
    "t" : "fa", 
    "T" : "fa#",
    "y" : "sol",
    "Y" : "sol#",
    "u" : "la",
    "U" : "la#",
    "i" : "si"
}  

# Dico de l'octave 4

keymap4 = {
    "x" : "do",
    "X" : "do#",
    "c" : "re", 
    "C" : "re#",
    "v" : "mi",
    "b" : "fa",
    "B" : "fa#", 
    "n" : "sol",
    "N" : "sol#",
    "," : "la",
    "?" : "la#",
    ";" : "si"
}
#fonction jouant le piano avec le clavier

def key_press(event):
    key = event.char  #key pressed

    if key in keymap3:
        note = Note(keymap3[key], 3)
        note.play()
        print(note)

    elif key in keymap2:
        note = Note(keymap2[key], 2)
        note.play()
        print(note)

    elif key in keymap4:
        note = Note(keymap4[key], 4)
        note.play()

        print(note)
    else:
        print("Key pressed does nothing")

#fonction jouant le piano avec les boutons

def play_note(note_name : str, octave : int):
    note = Note(note_name, octave)
    note.play()
    print(note)

#AIDE DE LA DOCUMENTATION TKINTER https://docs.python.org/fr/3.13/library/tkinter.html 


# Initialize tkinter window
window = tkinter.Tk()
window.title("Play Piano")
window.geometry('1080x720')
window.minsize(480, 360)
window.config(background="#cccccc")

# Frames
frame = tkinter.Frame(window, bg="#cccccc", bd=2, relief="sunken")
frame_piano = tkinter.Frame(window, bg="#cccccc")

# Title
label_title = tkinter.Label(frame, text="Jouez au piano avec le clavier", font=('Courrier', 35), bg="#cccccc")
label_title.pack()

# Subtitle
label_subtitle = tkinter.Label(frame, text="3 octaves disponibles !", font=('Courrier', 15), bg="#cccccc")
label_subtitle.pack()

def create_piano_octave(octave, keymap, row):  #pour ne pas avoir 400 lignes de créations de boutons

    i = 0   # placer dans les colonnes

    for key, note in keymap.items():

        txt = note+str(octave) + "\n" + "("+key+")"   #texte du bouton
        button = tkinter.Button(frame_piano, text=txt, font=('Arial', 12), width=4, height=12,command=lambda note=note, octave=octave: play_note(note, octave))
        button.grid(row=row, column=i, padx=2, pady=2) 

        if key.islower() or key in [",",";"]: # tout ce qui est une touche blanche du piano
            button.config(bg='white', fg='black')

        else: #touches noirs du piano
            button.config(bg='black', fg='white')

        i += 1  # on passe à la colonne suivante

# Creer rangée de notes pour chaques octaves
create_piano_octave(2, keymap2, 0)
create_piano_octave(3, keymap3, 1)
create_piano_octave(4, keymap4, 2)

# affichage
frame.pack(side="top")
frame_piano.pack(expand=True)

# Associe l'evenement d'une touche préssée a la fonction key_press
window.bind("<KeyPress>", key_press)

# lancer fenetre
window.mainloop()
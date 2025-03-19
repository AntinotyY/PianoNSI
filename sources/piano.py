import os
from classes import *
import tkinter


def get_kb_input():

    if os.name == "nt":  #windows
        import msvcrt
        while True:
            if msvcrt.kbhit(): #touche appuyée
                key = msvcrt.getwch() #obtenir la touche
                return key

    else:  #GOOGLE (STACK OVERFLOW)

        import termios
        import tty
        import sys
        filedescriptors = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
        key = sys.stdin.read(1)[0]
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)
        return key
    
# Dico de l'octave 3, celui du milieu

keymap3 = {
    "s" : "do",
    "d" : "re", 
    "f" : "mi",
    "g" : "fa", 
    "h" : "sol",
    "j" : "la",
    "k" : "si",
    "S" : "do#",
    "D" : "re#",
    "G" : "fa#",
    "H" : "sol#",
    "J" : "la#"
}  

#Dico de l'octave 2

keymap2 = {
    "z" : "do",
    "e" : "re", 
    "r" : "mi",
    "t" : "fa", 
    "y" : "sol",
    "u" : "la",
    "i" : "si",
    "Z" : "do#",
    "E" : "re#",
    "T" : "fa#",
    "Y" : "sol#",
    "U" : "la#"
}  

# Dico de l'octave 4

keymap4 = {
    "x" : "do",
    "c" : "re", 
    "v" : "mi",
    "b" : "fa", 
    "n" : "sol",
    "," : "la",
    ";" : "si",
    "X" : "do#",
    "C" : "re#",
    "B" : "fa#",
    "N" : "sol#",
    "?" : "la#"
}  

def piano():
    while True:
        key = get_kb_input()  # Capture the keyboard input.
        if key in keymap3:
            note = Note(keymap3[key],3)
            note.play()
            print(note)

        elif key in keymap2:
            note = Note(keymap2[key],2)
            note.play()
            print(note)

        elif key in keymap4:
            note = Note(keymap4[key],4)
            note.play()
            print(note)

        else :
            print("key pressed do nothing")
        window.mainloop()

#Initialiser fenetre
window = tkinter.Tk() #créer fenetre
window.title("Play Piano") #titre fenetre
window.geometry('1080x720')
window.minsize(480,360)
window.config(background="#cccccc")

#Frames
frame = tkinter.Frame(window,bg="#cccccc",bd=2,relief="sunken") #titre et sous titres
frame_piano = tkinter.Frame(window,bg="#cccccc")

#Titre
label_title = tkinter.Label(frame,text="Jouez au piano avec le clavier", font=('Courrier',35),bg="#cccccc")
label_title.pack()

#Sous Titre
label_subtitle = tkinter.Label(frame,text="3 octaves disponibles !", font=('Courrier',15),bg="#cccccc")
label_subtitle.pack()

#bouton start
button_start = tkinter.Button(frame,text="START",fg = "black", bg= "white",command=piano)
button_start.pack()

#affichage
frame.pack(side="top")
frame_piano.pack(expand=True)

piano()
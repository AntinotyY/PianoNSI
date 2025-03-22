import tkinter
from classes import *

# Key mappings for different octaves
keymap3 = {
    "s": "do", "d": "re", "f": "mi", "g": "fa", "h": "sol", "j": "la", "k": "si",
    "S": "do#", "D": "re#", "G": "fa#", "H": "sol#", "J": "la#"
}

keymap2 = {
    "z": "do", "e": "re", "r": "mi", "t": "fa", "y": "sol", "u": "la", "i": "si",
    "Z": "do#", "E": "re#", "T": "fa#", "Y": "sol#", "U": "la#"
}

keymap4 = {
    "x": "do", "c": "re", "v": "mi", "b": "fa", "n": "sol", ",": "la", ";": "si",
    "X": "do#", "C": "re#", "B": "fa#", "N": "sol#", "?": "la#"
}

# Function to handle key press and play the note
def key_press(event):
    key = event.char  # Get the key pressed

    # Check if the key is in any of the keymaps and play the corresponding note
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

# Display frames
frame.pack(side="top")
frame_piano.pack(expand=True)

# Bind the key press event to the `key_press` function
window.bind("<KeyPress>", key_press)

# Start tkinter's main loop (this must run in the main thread)
window.mainloop()
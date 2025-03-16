import os
from classes import *
import threading


def get_kb_input():

    if os.name == "nt":  #windows
        import msvcrt
        while True:
            if msvcrt.kbhit(): #key is pressed
                key = msvcrt.getwch() #decode
                return key

    else:   #google

        import termios
        import tty
        import sys
        filedescriptors = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
        key = sys.stdin.read(1)[0]
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)
        return key

keymap = {
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

def play_concurrently(key):  
    if key in keymap:
        note = Note(keymap[key],3)
        note.play()
    else :
        print("key pressed do nothing")
    

def piano():
    while True:
        key = get_kb_input()  # Capture the keyboard input.

        if key in keymap:
            note = Note(keymap[key],3)
            note.play()
            print(note)

        # Start a new thread to play the note concurrently
        #threading.Thread(target=play_concurrently, args=(key,)).start()

piano()



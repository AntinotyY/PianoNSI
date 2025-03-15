import os
from classes import *

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
    "l" : "do2"
}

def piano():
    while True:
        key = get_kb_input()
        if key in keymap:
            note = Note(keymap[key],3)
            print(note)
        elif key in keymap.upper():
            note = Note(keymap[key])
            print(note)
        else :
            print("key pressed do nothing")

while True:
    piano()
        


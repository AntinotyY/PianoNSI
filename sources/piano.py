import os

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

print(get_kb_input())

keymap = {
    "s" : "do",
    "d" : "ré", 
    "f" : "mi",
    "g" : "fa", 
    "h" : "sol",
    "j" : "la",
    "k" : "si",
    "l" : "do2"
}

class Note:
    def __init__(self,clé,diese):
        self.clé = clé
        self.diese = diese

def piano():
    while True:
        key = get_kb_input()
        if key in keymap:
            note = Note(key,False)
        elif key in keymap.upper():
            note = Note(key,True)
        else :
            print("key pressed do nothing")
        


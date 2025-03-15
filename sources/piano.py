import os


class File :
    def __init__(self):
        self.tab = []

    def est_vide(self) :
        return len(self.tab)==0
    
    def defile(self):
        return self.tab.pop(0)
        
    def enfile(self,x):
        self.tab.append(x)

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

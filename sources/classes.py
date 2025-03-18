import math
import playsound3
import time

class Note():

    NOTES = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

    def __init__(self, nom:str, octave:int, duration=0, position=0):

        assert (nom in Note.NOTES or nom == None), "débile ca existe pas " + nom

        self.nom = nom
        self.octave = octave

        self.duration = duration
        self.position = position

        #NE PAS METTRE OS.SEP ICI
        self.path = "/".join(["data", "notes", str(nom) + str(octave) + ".wav"]) #/data/notes/do2.wav
       
    
    def __str__(self):
        if self.nom == None:
            return "None"

        return self.nom + str(self.octave)


    def __eq__(self, value):
        return self.nom == value.nom and self.octave == value.octave


    def play(self):
        if self.nom == None:
            return
        
        playsound3.playsound(self.path, False)

        
    
    #deuxième constructeur (donc pas de self)
    def from_frequency(frequency:float, duration=0, position=0):
        if frequency == 0.0:
            return Note(None, 0, duration, position)

        DO_0 = 440 * 2**(-4.75)

        i = round(12 * math.log2(frequency / DO_0))

        note = Note.NOTES[i % 12]
        octave = (i // 12)

        return Note(note, octave, duration, position)



class Partition():

    def __init__(self, notes: list):

        self.notes = notes
        self.remove_duplicates()
    
    def __repr__(self):
        string = "----------\n"
        for note in self.notes:
            string = string + str(note) + " à " + str(note.position) + " de " + str(note.duration) + "s\n"
        return string + "----------"
    

    def remove_duplicates(self):

        cleaned = [self.notes[0]]

        for note in self.notes[1:]:
            if note != cleaned[-1] or cleaned[-1].duration >= 0.4:
                cleaned.append(note)
            else:
                cleaned[-1].duration += note.duration
        
        self.notes = cleaned
    
    def play(self):
        for note in self.notes:
            print("---")
            print(note)
            print(note.duration)
            note.play()
            time.sleep(note.duration)



    

import math
from playsound import playsound #version 1.2.2

class Note():

    NOTES = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

    def __init__(self, nom:str, octave:int, duration=0, position=0):

        assert (nom in Note.NOTES or nom == "None"), "débile ca existe pas " + nom

        self.nom = nom
        self.octave = octave

        self.duration = duration
        self.position = position

        self.path = "data/notes/" + nom + str(octave)+ ".wav" #TODO refaire psk ils aiment pas les slash
    
    def __str__(self):
        return self.nom + str(self.octave)


    def __eq__(self, value):
        return self.nom == value.nom and self.octave == value.octave


    def play(self):
        playsound(self.path)
    
    #deuxième constructeur (donc pas de self)
    def from_frequency(frequency:float, duration=0, position=0):
        if frequency == 0.0:
            return Note("None", 0, duration, position)

        DO_0 = 440 * 2**(-4.75)

        i = round(12 * math.log2(frequency / DO_0))

        note = Note.NOTES[i % 12]
        octave = (i // 12)

        return Note(note, octave, duration, position)



class Partition():

    def __init__(self, notes: list[Note]):

        self.notes = notes
        self.cleanup()
    
    def __repr__(self):
        string = "----------\n"
        for note in self.notes:
            string = string + str(note) + " à " + str(note.position) + " de " + str(note.duration) + "s\n"
        return string + "----------"
    

    def cleanup(self):

        cleaned = [self.notes[0]]

        for note in self.notes[1:]:
            if note != cleaned[-1]:
                cleaned.append(note)
            else:
                cleaned[-1].duration += note.duration
        
        self.notes = cleaned


    

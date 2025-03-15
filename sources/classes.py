import math

class Note():

    NOTES = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

    def __init__(self, nom:str, octave:int):

        assert nom in Note.NOTES, "débile ca existe pas " + nom

        self.nom = nom
        self.octave = octave

        self.path = "data/notes/" + nom + str(octave) #TODO refaire psk ils aiment pas les slash
    

    def __repr__(self):
        return self.nom + str(self.octave)



    def play(self):
        pass
        #jsp mais ya besoin de self.path surement
    



    #deuxième constructeur (donc pas de self)
    def from_frequency(frequency:float):

        DO_0 = 440 * 2**(-4.75)

        i = round(12 * math.log2(frequency / DO_0))

        note = Note.NOTES[i % 12]
        octave = (i // 12) - 1

        return Note(note, octave)





    

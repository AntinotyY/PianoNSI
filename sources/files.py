import wave
import matplotlib.pyplot as plt
import numpy

from classes import *



def wav_to_signal(song: wave.Wave_read):

    width = song.getsampwidth()                             #nombre d'octets de chaque échantillon
    frames_buffer = song.readframes(song.getnframes())


    int_size = numpy.int16     #entier 16 bits signé, le plus utilisé pour les fichiers wav, correspond a une width de 2 octets 
    print("channels : ", width * 8)
    if width == 1:
        int_size = numpy.uint8 #entier 8 bits non signé, utilisé il y a longtemps
    elif width == 4:
        int_size = numpy.int32 #entier 32 bit signé
    

    signal = numpy.frombuffer(frames_buffer, int_size)

    if song.getnchannels() == 2:    # fichier stéréo, coté gauche et droit intercalés
        signal = signal[::2]        # on garde une valeur sur 2 (les valeurs à gauche, on saute les droites)
                                    # (garder les deux rendrait le signal deux fois trop long avec chaque valeur répétée (majorité des cas))

    return signal                   # renvoie un array numpy d'entiers qui correspondent aux valeurs du fichier wav (amplitude du son)




def find_frequency(signal, framerate):  #trouve la fréquence dominante d'un signal à l'aide de la FFT (merci chatgpt)

    # Appliquer la FFT pour obtenir le spectre fréquentiel
    fft_result = numpy.fft.fft(signal)
    
    # Calculer les fréquences associées aux indices du spectre FFT
    freqs = numpy.fft.fftfreq(len(signal), d=1/framerate)
    
    # Calculer la magnitude du résultat FFT (valeurs absolues)
    magnitudes = numpy.abs(fft_result)
    
    # Prendre seulement la partie positive du spectre (symétrique)
    positive_freqs = freqs[:len(freqs)//2]
    positive_magnitudes = magnitudes[:len(magnitudes)//2]
    
    # Trouver l'indice de la fréquence avec l'amplitude maximale
    max_index = numpy.argmax(positive_magnitudes)
    
    # Retourner la fréquence dominante
    dominant_frequency = positive_freqs[max_index]
    
    return dominant_frequency




def split_signal(signal, size:int, overlap:int): # découpe un signal en une liste de signaux de taille size AVEC REPETITION JUSQU'A OVERLAP (ex. [1, 2, 3, 4, 5] -> [[1, 2], [2, 3], [3, 4], [4, 5]] avec size = 2 et overlap = 1)
                                         # l'overlap permet d'avoir des meilleurs résultats en prenant en compte la note dominante dans tous ses alentours plutot que par bouts totalements séparés
    
    assert overlap < size

    if len(signal) < size:
        return signal

    result = []

    for i in range(0, len(signal)- size+1, size - overlap): #fenetre qui se déplace de size - overlap
        result.append(signal[ i : i+size ]) #on ajoute le bout de signal coupé
    
    return result



def get_song_partition(path) -> Partition:

    with wave.open(path, "rb") as song:

        signal = wav_to_signal(song)
        framerate = song.getframerate() #fréquence d'échantillonage en Hz

        CHECK_DURATION = 0.25   # en secondes, la durée sur laquelle on cherche la note dominante
        OVERLAP_RATIO = 0.5     # ENTRE 0 et 1 (LOGIQUEMENT 0.5 ou moins) proportion du sous signal répétée dans le suivant

        splitting_size = int(CHECK_DURATION / (1-OVERLAP_RATIO) * framerate ) # taille des sous signaux
    
        sub_signals = split_signal(signal, splitting_size, int(splitting_size * OVERLAP_RATIO))


        notes = []

        for i in range(len(sub_signals)):

            frequence = find_frequency(sub_signals[i], framerate)
            duration = CHECK_DURATION
            position = i * CHECK_DURATION

            notes.append(Note.from_frequency(frequence, duration, position))

        """
        plt.figure(figsize=(10, 4))
        plt.plot(
            [i * CHECK_DURATION for i in range(len(sub_signals))],
            [find_frequency(sub, framerate) for sub in sub_signals]
        )
        plt.xlabel("Temps (secondes)")
        plt.ylabel("Fréquence dominante (Hz)")
        plt.title("Fréquences")
        plt.legend()
        plt.show
        """
        return Partition(notes)

print(get_song_partition("data/asgore.wav"))
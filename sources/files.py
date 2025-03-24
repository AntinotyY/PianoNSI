#Projet : PianoNSI
#Auteurs : Antoine Meignan, Rafaël Lacan

import wave
import matplotlib.pyplot as plt
import numpy
import os

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


#----------------------------------------------------------------------------------------------------------------------------------------------
#---------------PARTIE ECRITE GRACE A CHAT GPT-------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

# Cette partie utilise la transformée de Fourier, trop avancée pour notre niveau actuel mais indispensable à notre projet.
# Nous avons ainsi eu recours à l'aide de l'IA pour cette partie délimitée.


#fonctions permettant de trouver la fréquence dominante d'un signal + trucs d'optimisation pour avoir de meilleurs résultats

def bandpass_filter(signal, lowcut, highcut, framerate):
    """Applique un filtre passe-bande pour limiter les fréquences hors de la plage musicale."""
    freqs = numpy.fft.fftfreq(len(signal), d=1 / framerate)
    fft_signal = numpy.fft.fft(signal)
    filter_mask = (numpy.abs(freqs) >= lowcut) & (numpy.abs(freqs) <= highcut)
    return numpy.fft.ifft(fft_signal * filter_mask).real

def cepstral_analysis(signal, framerate):
    """Analyse cepstrale pour détecter la fréquence fondamentale."""
    cepstrum = numpy.fft.ifft(numpy.log(numpy.abs(numpy.fft.fft(signal)) + 1e-6)).real
    return framerate / (numpy.argmax(cepstrum[1:]) + 1)

def find_frequency(signal, framerate):
    if len(signal) == 0:
        return 0.0
    
    filtered_signal = bandpass_filter(signal, 150, 1200, framerate)
    freqs = numpy.fft.fftfreq(len(filtered_signal), d=1 / framerate)
    magnitudes = numpy.abs(numpy.fft.fft(filtered_signal))[:len(freqs) // 2]
    positive_freqs = freqs[:len(freqs) // 2]
    
    melody_indices = (positive_freqs > 150) & (positive_freqs < 1200)
    filtered_freqs = positive_freqs[melody_indices]
    filtered_magnitudes = magnitudes[melody_indices]
    
    if not numpy.any(filtered_magnitudes):
        return 0.0
    
    dominant_frequency = filtered_freqs[numpy.argmax(filtered_magnitudes)]
    
    for i in range(2, 6):
        harmonic_freq = dominant_frequency * i
        if any(numpy.isclose(filtered_freqs, harmonic_freq, atol=1.0)):
            dominant_frequency /= i
            break
    
    return dominant_frequency

#----------------------------------------------------------------------------------------------------------------------------------------------
#---------------FIN DE PARTIE ECRITE GRACE A CHAT GPT------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------



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

        CHECK_DURATION = 0.10   # en secondes, la durée sur laquelle on cherche la note dominante
        OVERLAP_RATIO = 0.5  # ENTRE 0 et 1, (pas 1) proportion du sous signal répétée dans le suivant

        splitting_size = int(CHECK_DURATION / (1-OVERLAP_RATIO) * framerate ) # taille des sous signaux
    
        sub_signals = split_signal(signal, splitting_size, int(splitting_size * OVERLAP_RATIO))


        notes = []

        for i in range(len(sub_signals)):

            frequence = find_frequency(sub_signals[i], framerate)
            duration = CHECK_DURATION
            position = i * CHECK_DURATION

            notes.append(Note.from_frequency(frequence, duration, position))


        #tests
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
        plt.show()"
        """
        
        return Partition(notes)


#PAS BESOIN DE OS.SEP.JOIN ICI
get_song_partition("data/zelda.wav").play()
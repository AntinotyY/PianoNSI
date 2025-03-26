import files
print("bienvenue dans PianoNsi")
n = int(input("1:jouez du piano"+"\n"+"2:lancez la musique piano démo"+"\n"+"3:lancer une musique personnalisée \n"))
if n == 1:
    from piano import *
if n == 2:
    files.get_song_partition("data/zelda.wav").play()
if n == 3:
    print("Mettez bien votre fichier dans le dossier data en .wav")
    files.get_song_partition(f"data/{input("nom du fichier (sans le dossier ni .wav) : ")}.wav").play()
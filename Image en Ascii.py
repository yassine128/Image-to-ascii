import numpy as np
from PIL import Image
import os
def get_path():
    with open("ASCII-path-log.txt", "r", encoding="utf-8") as log:
         path = log.read()
    return(path)

def path_folder_create():
    while(True):
        path = input("Entrez le chemin d'accès du dossier où les images seront transformées: ")
        try:
            os.mkdir(path)
            with open (f"ASCII-path-log.txt", "w", encoding="utf-8") as log:
                log.write(path)
            return(path)
        except FileExistsError:
            print("Le fichier existe déjà!")

        except FileNotFoundError: 
            print("Chemin d'accès entré invalide!")


def moyen_nuance_gris(case):

    bloc_image = np.array(case)
    w,h = bloc_image.shape

    moyenne =  np.average(bloc_image.reshape(w*h))
    #print("Moyenne de gris : %d" %moyenne)
    return(moyenne)

def image_to_ascii(fichier, gris_choix):
    image = Image.open(fichier, "r").convert("L")

    print(gris_choix)
    W, H = image.size[0], image.size[1]
    ratio = H/W*0.45
    nbr_col = int(W/1)
    nbr_ligne = int(ratio*nbr_col)

    print("Nombre de caractères ASCII %d x %d" %(nbr_ligne, nbr_col))
    gris_choix= int(gris_choix)
    image_texte = []
    if gris_choix == 10:
        nuance_gris = "@%#*+=-:. "
    elif gris_choix ==70:
        nuance_gris = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    for i in range(nbr_ligne):
        y1 = int(i*H/nbr_ligne)
        y2 = int((i+1)*H/nbr_ligne)
        image_texte.append("")
        ligne = ""
        for j in range(nbr_col):
            x1 = int(j*W/nbr_col)
            x2 = int((j+1)*W/nbr_col)

            tuile = image.crop((x1,y1,x2,y2))
            gris = moyen_nuance_gris(tuile)
            character = nuance_gris[int(gris*(gris_choix-1)/255)]

            ligne += character

        image_texte[i] = ligne

    return(image_texte)

def main():
    #nom_image = input("Tapez le nom de l'image à transformer (avec l'extension): ")
    choix = input("Voulez vous utiliser le dossier par défaut (1) ou changer le dossier par défaut? (2): ")
    if choix == "2":
        path = path_folder_create()
    else: 
        path = get_path()
    nom_image = input("Entrez le nom de l'image (avec extension): ")
    gris = input("Nuance de gris [10] ou [70] (niveau de précision): ")
    print("Création du chef d'oeuvre en cours...")
    path_de_image = f"{path}/{nom_image}"
    finale = image_to_ascii(path_de_image, gris)

    with open(f"{path}\{nom_image}_en_ASCII.txt", "w", encoding="utf-8") as file:
        for ligne in finale:
            file.write(f"{ligne} \n")
    print("Tadam!")

if __name__ == "__main__":
    main()
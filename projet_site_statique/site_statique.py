import argparse 
import os
import markdown2
import sys

# Interface en ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", type = str,
                    help = "chemin du dossier des fichiers source")
parser.add_argument("-o", "--output", type = str,
                    help = "chemin du dossier des fichiers generes")
args = parser.parse_args()

# Création de la liste des fichiers à modifier
dossier_md = os.listdir(args.input)
# lecture des fichiers md
for fichier in dossier_md:
    if fichier.split('.')[1] == "md":
        with open("{}/{}".format(args.input, fichier), 'r', encoding = "utf-8") as md:
            texte = markdown2.markdown(md.read())
            html = open("{}/{}.html".format(args.output,fichier.split('.')[0]), 'w', encoding = "utf-8")
            html.write(texte)
            html.close
            print("{}.html a ete cree!".format(fichier.split('.')[0]))
    else:
        pass

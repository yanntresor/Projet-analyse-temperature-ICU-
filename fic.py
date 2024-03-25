# Importation des bibliothèques nécessaires
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation



import os
#---------------------PARTIE BASE DE DONNEE --------------------------------- 
print("Début du script")

# Définition de la fonction pour lire et fusionner les fichiers CSV
def lire_et_fusionner(fichiers_csv, dossier='.'):
    dataframes = []  # Liste pour stocker les DataFrames temporaires
    for fichier in fichiers_csv:
        chemin_complet = os.path.join(dossier, fichier)  # Construction du chemin complet vers le fichier
        df_temp = pd.read_csv(chemin_complet)  # Lecture du fichier CSV
        annee = fichier.split('.')[0][-4:]  # Extraction de l'année à partir du nom du fichier
        df_temp['Annee'] = annee  # Ajout de la colonne 'Annee'
        dataframes.append(df_temp)  # Ajout du DataFrame temporaire à la liste
    return pd.concat(dataframes, ignore_index=True)  # Fusion des DataFrames en un seul

# Liste des noms des fichiers CSV à lire et à fusionner
fichiers_csv = ['2012.csv', '2013.csv', '2014.csv', '2015.csv', '2016.csv', '2017.csv', '2018.csv', '2019.csv', '2020.csv', '2021.csv']

# Lecture et fusion des fichiers CSV
df_final = lire_et_fusionner(fichiers_csv)

# Affichage des premières lignes du DataFrame final pour vérification
print(df_final.head(100000))

# Affichage des informations générales sur le DataFrame final
print(df_final.info())

print("Affichage noms des joueurs" )

print("verification")
joueurs_recherches = [" André Onana", " Samir Nasri", "Dele Alli" ,"Mamadou Sakho", "Paul Pogba", "Sergio Ramos"]

joueurs_trouves = df_final['Name'].isin(joueurs_recherches)

for joueur in joueurs_recherches:
    if joueur in df_final[joueurs_trouves]['Name'].values:
        print(f"{joueur} est dans le fichier.")
    else:
        print(f"{joueur} n'est pas trouvé.")


print    ("Fin verification")

print(df_final)


      




print("Fin du script")



#---------------------PARTIE BASE DE DONNEE --------------------------------- 
#---------------------------------------------------------------
#Nettoyage BASE DE DONNEES
#  1)                                               Gestion valeures Manquantes

# Supprimer les lignes où au moins une valeur est manquante
df_final.dropna(inplace=True)

#-----------------------------------------------------------------------------
import pandas as pd
from api import app, db
from api import GenreModel


def import_genre():
    # Charger le fichier CSV brut
    file_path = './data/genres.csv'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Retirer l'en-tête
    data_lines = lines[1:]

    # Découper chaque ligne et convertir en objets genreModel
    genres = []
    for line in data_lines:
        line = line.strip()  # Supprimer les espaces ou sauts de ligne
        values = line.split(',', maxsplit=1)  # Découper en 1 parties : idd, age, email, generi_preferiti
        
        # Assigner les valeurs et nettoyer si nécessaire
        id = int(values[0].strip('"')) 
        name = values[1].strip('"')  


        # Créer un genre 
        genre = GenreModel(
            id=id,
            name=name,
        )
        genres.append(genre)

    # Ajouter les genres à la base de données
    with app.app_context():
        db.session.add_all(genres)
        db.session.commit()

    print("Données importées avec succès !")

# Exécuter l'importation des données
import_genre()
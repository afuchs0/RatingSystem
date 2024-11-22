import pandas as pd
from api import app, db
from api import UserModel

def import_data():
    # Charger le fichier CSV brut
    file_path = '/mnt/c/Users/leoba/Documents/CoursesProject/DigitalL/RatingSystem/Api/data/users.csv'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Retirer l'en-tête
    data_lines = lines[1:]

    # Découper chaque ligne et convertir en objets UserModel
    users = []
    for line in data_lines:
        # print(line)
        line = line.strip()  # Supprimer les espaces ou sauts de ligne
        values = line.split(',', maxsplit=3)  # Découper en 4 parties : idd, id, age, generi_preferiti
        # print(line)
        # print(values)
        # Assigner les valeurs et nettoyer si nécessaire
        idd = int(values[0].strip('"'))  # Retirer les guillemets pour le premier champ
        user_id = int(values[1].strip('"'))  # Retirer les guillemets pour le deuxième champ
        age = int(values[2].strip('"'))  # Retirer les guillemets pour le troisième champ
        generi_preferiti = values[3].strip('"')  # Retirer les guillemets pour le dernier champ

        # Nettoyer les formats spécifiques (comme les doubles guillemets internes dans generi_preferiti)
        generi_preferiti = generi_preferiti.replace('"""', '"').replace("''", "'").strip()

        # Créer un utilisateur
        user = UserModel(
            idd=idd,
            id=user_id,
            age=age,
            generi_preferiti=generi_preferiti
        )
        users.append(user)

    # Ajouter les utilisateurs à la base de données
    with app.app_context():
        db.session.add_all(users)
        db.session.commit()

    print("Données importées avec succès !")

# Exécuter l'importation des données
import_data()

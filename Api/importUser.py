import pandas as pd
from api import app, db
from api import UserModel
import json
from werkzeug.security import generate_password_hash, check_password_hash

def import_data():
    # Charger le fichier CSV brut
    file_path = './data/users.csv'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Retirer l'en-tête
    data_lines = lines[1:]

    # Découper chaque ligne et convertir en objets UserModel
    users = []
    for line in data_lines:
        line = line.strip()  # Supprimer les espaces ou sauts de ligne
        values = line.split(',', maxsplit=4)  # Découper en 4 parties : idd, age, email, generi_preferiti
        
        # Assigner les valeurs et nettoyer si nécessaire
        id = int(values[0].strip('"'))
        idd = int(values[1].strip('"'))  
        age = int(values[2].strip('"'))  
        email = values[3].strip('"') 
        generi_preferiti = values[4].strip('"')  

        # Nettoyer et sérialiser les genres préférés
        generi_preferiti = json.dumps(generi_preferiti.split(';'))  # Si les genres sont séparés par ";"

        # Créer un utilisateur avec un mot de passe par défaut haché
        user = UserModel(
            id=id,
            idd=idd,
            age=age,
            email=email,
            password_hash=generate_password_hash("password123"),  # Mot de passe par défaut
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
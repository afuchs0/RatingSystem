from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from backend.app.models.rating import Rating
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
# Configurer la connexion à la base de données
DATABASE_URL = 'sqlite:///library.db'  # Remplacez par votre URL de base de données
engine = create_engine(DATABASE_URL)
Rating.metadata.create_all(engine)  # Crée les tables si elles n'existent pas encore
Session = sessionmaker(bind=engine)

def load_visualisation_from_csv(file_path):
    # Créer une nouvelle session
    session = Session()
    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(file_path)
    # Convertir chaque ligne en objet Book et l'ajouter à la session
    for _, row in df.iterrows():
        rating = Rating(
            user_id=row['userId'],
            book_id=row['bookId'],
            rating=row['rating']
        )
        session.add(rating)

    # Valider et fermer la session
    session.commit()
    session.close()


def findAll():
    ratings = Rating.query.all()
    return jsonify([rating.to_dict() for rating in ratings])


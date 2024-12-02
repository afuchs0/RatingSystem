from flask import json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app.models.users import User
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import re
from werkzeug.security import generate_password_hash
from flask import jsonify, request
from app.models import users

db = SQLAlchemy()
# Configurer la connexion à la base de données
DATABASE_URL = 'sqlite:///library.db'  # Remplacez par votre URL de base de données
engine = create_engine(DATABASE_URL)
#users.metadata.create_all(engine)  # Crée les tables si elles n'existent pas encore
Session = sessionmaker(bind=engine)

#find user 
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


def load_users_from_csv():
    csv_file = request.files.get('file')
    session = Session()

    if not csv_file:
        return jsonify({"error": "No file uploaded"}), 400
    try:
        # Lire le contenu du fichier CSV
        csv_reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
        new_users = []
        errors = []

        for index, row in enumerate(csv_reader, start=1):
            email = row.get("email")
            password = row.get("password")
            generi_preferiti = row.get("generi_preferiti", "[]")
            age = row.get("age")

            # Validation des champs
            if not email or not password or not age:
                errors.append(f"Missing data in row {index}: {row}")
                continue

            # Valider l'email
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                errors.append(f"Invalid email format in row {index}: {email}")
                continue

            # Convertir l'âge
            try:
                age = int(age)
            except ValueError:
                errors.append(f"Invalid age in row {index}: {row}")
                continue

            # Charger les genres préférés
            try:
                generi_preferiti = json.loads(generi_preferiti)
            except json.JSONDecodeError:
                errors.append(f"Invalid generi_preferiti format in row {index}: {row}")
                continue

            # Vérifier si l'utilisateur existe déjà
            if session.query(User).filter_by(email=email).first():
                errors.append(f"User with email {email} already exists (row {index})")
                continue

            # Ajouter l'utilisateur à la liste
            hashed_password = generate_password_hash(password)
            new_user = User(
                email=email,
                password=hashed_password,
                generi_preferiti=generi_preferiti,
                age=age
            )
            new_users.append(new_user)

        # Insérer les utilisateurs dans la base de données
        if new_users:
            session.add_all(new_users)
            session.commit()

        # Retourner le résultat
        return jsonify({
            "message": f"{len(new_users)} users successfully loaded",
            "errors": errors
        }), 201 if not errors else 207

    except Exception as e:
        session.rollback()
        return jsonify({"error": "Failed to load users", "message": str(e)}), 500

    finally:
        session.close()

#update user 
def upadte_user(user_id):
    data= request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error":"User not found"}), 404
    user.update(data)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Update failed", "message": str(e)}), 400
    
    return jsonify(user.to_dict()), 200
    

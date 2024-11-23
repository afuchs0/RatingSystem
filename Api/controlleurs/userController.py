from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app.models.users import User
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
from werkzeug.security import generate_password_hash
from flask import jsonify, request
from app.models import User

db = SQLAlchemy()
# Configurer la connexion à la base de données
DATABASE_URL = 'sqlite:///library.db'  # Remplacez par votre URL de base de données
engine = create_engine(DATABASE_URL)
User.metadata.create_all(engine)  # Crée les tables si elles n'existent pas encore
Session = sessionmaker(bind=engine)

#find user 
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


def load_users_from_csv():
    # Récupérer le fichier CSV depuis la requête (si uploadé)
    csv_file = request.files.get('file')
    session = Session()
    if not csv_file:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        # Lire le fichier CSV
        csv_reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
        
        new_users = []
        for row in csv_reader:
            email = row.get("email")
            password = row.get("password")
            generi_preferiti = eval(row.get("generi_preferiti"))  # Convertir en liste
            age = row.get("age")

            # Validation des champs obligatoires
            if not email or not password or not age:
                return jsonify({"error": f"Invalid data in row: {row}"}), 400

            # Vérifier si l'utilisateur existe déjà
            if session.query(User).filter_by(email=email).first():
                return jsonify({"error": f"User with email {email} already exists"}), 409

            # Créer un nouvel utilisateur
            hashed_password = generate_password_hash(password)
            new_user = User(
                email=email,
                password=hashed_password,
                generi_preferiti=generi_preferiti,
                age=age
            )
            new_users.append(new_user)

        # Insérer les utilisateurs dans la base de données
        session.add_all(new_users)
        session.commit()
        return jsonify({"message": f"{len(new_users)} users successfully loaded"}), 201

    except Exception as e:
        session.rollback()
        return jsonify({"error": "Failed to load users", "message": str(e)}), 500


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
    

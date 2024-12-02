from flask import request, jsonify
from flask_jwt_extended import create_access_token

from backend.app.models.user import User


def login():
    # Obtenir les données de la requête
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Vérifier que l'utilisateur existe
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Créer un token JWT pour l'utilisateur
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token, "user": user.to_dict()}), 200
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app.models.user import User
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()

#find user 
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


#create user 
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], surname=data['surname'], age=data['age'])
    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Database Integrity Error", "message": str(e)}), 400
    return jsonify(new_user.to_dict()), 201

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
    

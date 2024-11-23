from sqlalchemy import ARRAY, Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from api import db
import json

Base = declarative_base()

# Visualization class
class VisualizationModel(db.Model):
    __tablename__ = 'visualizations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    reading_date = db.Column(db.Date, nullable=True)

    # Relationships
    user = db.relationship("UserModel", back_populates="visualizations")
    book = db.relationship("BookModel", back_populates="visualizations")

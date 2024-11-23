from sqlalchemy import ARRAY, Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from api import db
import json

Base = declarative_base()
class BookModel(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    serie = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
    desc = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
    lang = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
    pages = db.Column(db.Integer, nullable=True)  # Made nullable True for optional pages
    nawards = db.Column(db.Integer, nullable=False, default=0)  # Default value for awards
    avg_vote = db.Column(db.Float, nullable=True, default=0.0)  # Default value for avg_vote
    price = db.Column(db.Float, nullable=True)  # Changed to Float for price

    author = db.Column(db.String(100), nullable=False)
    genres = db.Column(db.String(200), nullable=True)  # Increased size for genres (if a list)

    # Relationships
    ratings = db.relationship("RatingModel", back_populates="book")
    visualizations = db.relationship("VisualizationModel", back_populates="book") 

    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title, 
            "serie": self.serie, 
            "desc": self.desc, 
            "lang": self.lang, 
            "naward": self.nawards, 
            "avg_vote": self.avg_vote,
            "price": self.price, 
            "author": self.author,
            "genres": self.genres
        }

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)


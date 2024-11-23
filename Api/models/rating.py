from sqlalchemy import ARRAY, Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from api import db
import json

Base = declarative_base()

# Rating class
class RatingModel(db.Model):
    __tablename__ = 'ratings'
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.String(100), db.ForeignKey('books.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    # Relationships
    user = db.relationship("UserModel", back_populates="ratings")
    book = db.relationship("BookModel", back_populates="ratings")

    def to_dict(self):
        return {"user_id": self.user_id, "book_id": self.book_id, "rating": self.rating}

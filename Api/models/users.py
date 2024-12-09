from sqlalchemy import ARRAY, Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from api import db
import json

Base = declarative_base()

# User class
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(100), nullable=False)

    # Relationships
    ratings = db.relationship("RatingModel", back_populates="user")
    visualizations = db.relationship("VisualizationModel", back_populates="user") 

    def to_dict(self):
        return {
            "id": self.id, 
            "age": self.age
        }

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)

    def set_generi_preferiti(self, generi_preferiti):
        # Store the list as JSON string
        self.generi_preferiti = json.dumps(generi_preferiti)

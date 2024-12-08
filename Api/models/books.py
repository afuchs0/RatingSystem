from sqlalchemy import ARRAY, Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from api import db  # Absolute import from the Api package

import json

Base = declarative_base()
# Book class
class BookModel(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incremented primary key
    bookId = db.Column(db.String(100), nullable=True)  
    title = db.Column(db.String(100), nullable=True)
    series = db.Column(db.String(100), nullable=True)
    author = db.Column(db.String(100))
    rating = db.Column(db.String(100))
    description = db.Column(db.String(100))
    language = db.Column(db.String(100), nullable=True)
    #isbn = db.Column(db.String(100), nullable=True)
    #genres = db.Column(db.JSON(db.String(100)), nullable=True)
    #characters = db.Column(db.JSON(db.String(100)), nullable=True)  # Corrected typo: "charaters" -> "characters"
    #bookFormat = db.Column(db.String(100), nullable=True)
    #edition = db.Column(db.String(100), nullable=True)
    pages = db.Column(db.String(100), nullable=True)
    #publisher = db.Column(db.String(100), nullable=True)
    publishDate = db.Column(db.String(100), nullable=True)
    #firstPublishDate = db.Column(db.String(100), nullable=True)  # Fixed typo: "firtPublisherDate" -> "firstPublisherDate"
    awards = db.Column(db.JSON(db.String(100)), nullable=True)
    #numRatings = db.Column(db.String(100), nullable=True)
    #ratingsByStars = db.Column(db.JSON(db.String(100)), nullable=True)  # Fixed misplaced parenthesis
    #likedPercent = db.Column(db.String(100), nullable=True)
    #setting = db.Column(db.JSON(db.String(100)), nullable=True)  # Fixed misplaced parenthesis
    coverImg = db.Column(db.String(200), nullable=True)
    #bbeScore = db.Column(db.String(100))
    #bbeVotes = db.Column(db.String(100), nullable=True)
    price = db.Column(db.String(100), nullable=True)

    # Relationships
    ratings = db.relationship("RatingModel", back_populates="book")
    visualizations = db.relationship("VisualizationModel", back_populates="book")
    genres = db.relationship('Belong', back_populates='book')

    def to_dict(self):
        return {
            "id": self.id,
            "bookId": self.bookId,
            "title": self.title,
            "series": self.series,
            "author": self.author,
            "rating": self.rating,
            "description": self.description,
            "language": self.language,
            #"isbn": self.isbn,
            #"genres": self.genres,
            #"characters": self.characters,  # Corrected typo: "charaters" -> "characters"
            #"bookFormat": self.bookFormat,
            #"edition": self.edition,
            "pages": self.pages,
            #"publisher": self.publisher,
            "publishDate": self.publishDate,
            #"firstPublishDate": self.firstPublishDate,  # Corrected typo: "firtPublisherDate" -> "firstPublisherDate"
            "awards": self.awards,
            #"numRatings": self.numRatings,
            #"ratingsByStars": self.ratingsByStars,
            #"likedPercent": self.likedPercent,
            #"setting": self.setting,
            "coverImg": self.coverImg,
            #"bbeScore": self.bbeScore,
            #"bbeVotes": self.bbeVotes,  # Corrected typo: "bbVote" -> "bbeVote"
            "price": self.price,
        }
    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)

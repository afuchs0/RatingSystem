from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define all models (copying the models from your Flask setup)
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
    pages = db.Column(db.String(100), nullable=True)
    publishDate = db.Column(db.String(100), nullable=True)
    awards = db.Column(db.JSON, nullable=True)
    coverImg = db.Column(db.String(200), nullable=True)
    price = db.Column(db.String(100), nullable=True)

    # Relationships
    ratings = db.relationship("RatingModel", back_populates="book")
    visualizations = db.relationship("VisualizationModel", back_populates="book")
    genres = db.relationship('Belong', back_populates='book')

# GENRES Table
class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # Relationships
    books = db.relationship('Belong', back_populates='genre', cascade='all, delete-orphan')
    favourites = db.relationship('Favourite', back_populates='genre', cascade='all, delete-orphan')

# Rating class
class RatingModel(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.String(100), db.ForeignKey('books.bookId'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    rating_date = db.Column(db.Date, nullable=True)

    # Relationships
    user = db.relationship("UserModel", back_populates="ratings")
    book = db.relationship("BookModel", back_populates="ratings")

# Visualization class
class VisualizationModel(db.Model):
    __tablename__ = 'visualizations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.String(100), db.ForeignKey('books.bookId'), nullable=False)
    reading_date = db.Column(db.Date, nullable=True)

    # Relationships
    user = db.relationship("UserModel", back_populates="visualizations")
    book = db.relationship("BookModel", back_populates="visualizations")

# BELONG Table (Many-to-Many between Books and Genres)
class Belong(db.Model):
    __tablename__ = 'belong'
    id = db.Column(db.Integer, primary_key=True)
    genres_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    book_id = db.Column(db.String(100), db.ForeignKey('books.bookId'), nullable=False)

    # Relationships
    genre = db.relationship('Genre', back_populates='books')
    book = db.relationship('BookModel', back_populates='genres')

# FAVOURITE Table (Many-to-Many between Users and Genres)
class Favourite(db.Model):
    __tablename__ = 'favourite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    genres_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)

    # Relationships
    user = db.relationship('UserModel', back_populates='favourites')
    genre = db.relationship('Genre', back_populates='favourites')

# USER Table
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)

    # Relationships
    ratings = db.relationship("RatingModel", back_populates="user")
    visualizations = db.relationship("VisualizationModel", back_populates="user")
    favourites = db.relationship("Favourite", back_populates="user")

# Create all tables
with app.app_context():
    db.create_all()
    print("All tables created successfully in the database!")

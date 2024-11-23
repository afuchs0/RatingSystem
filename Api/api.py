from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from flask_restful import Resource, Api
# from routes import routes
from models.books import BookModel
from models.users import UserModel
from models.rating import RatingModel
from models.visualizations import VisualizationModel

app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# Configuration CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.register_blueprint(routes)

# # User class
# class UserModel(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     idd = db.Column(db.Integer, unique=True, nullable=False)
#     age = db.Column(db.String(100), nullable=False)
#     generi_preferiti = db.Column(db.Text)  # Change 'ARRAY' to 'Text'

#     # Relationships
#     ratings = db.relationship("RatingModel", back_populates="user")
#     visualizations = db.relationship("VisualizationModel", back_populates="user") 

#     def to_dict(self):
#         return {
#             "id": self.id, 
#             "idd": self.idd, 
#             "age": self.age,
#             "generi_preferiti": json.loads(self.generi_preferiti) if self.generi_preferiti else []  # Deserialize JSON to list
#         }

#     def update(self, data):
#         for key, value in data.items():
#             if hasattr(self, key) and value is not None:
#                 setattr(self, key, value)

#     def set_generi_preferiti(self, generi_preferiti):
#         # Store the list as JSON string
#         self.generi_preferiti = json.dumps(generi_preferiti)

# Book class
# class BookModel(db.Model):
#     __tablename__ = 'books'
    
#     id = db.Column(db.String(100), primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     serie = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
#     desc = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
#     lang = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
#     pages = db.Column(db.Integer, nullable=True)  # Made nullable True for optional pages
#     nawards = db.Column(db.Integer, nullable=False, default=0)  # Default value for awards
#     avg_vote = db.Column(db.Float, nullable=True, default=0.0)  # Default value for avg_vote
#     price = db.Column(db.Float, nullable=True)  # Changed to Float for price

#     author = db.Column(db.String(100), nullable=False)
#     genres = db.Column(db.String(200), nullable=True)  # Increased size for genres (if a list)

#     # Relationships
#     ratings = db.relationship("RatingModel", back_populates="book")
#     visualizations = db.relationship("VisualizationModel", back_populates="book") 

#     def to_dict(self):
#         return {
#             "id": self.id, 
#             "title": self.title, 
#             "serie": self.serie, 
#             "desc": self.desc, 
#             "lang": self.lang, 
#             "naward": self.nawards, 
#             "avg_vote": self.avg_vote,
#             "price": self.price, 
#             "author": self.author,
#             "genres": self.genres
#         }

#     def update(self, data):
#         for key, value in data.items():
#             if hasattr(self, key) and value is not None:
#                 setattr(self, key, value)

# # Rating class
# class RatingModel(db.Model):
#     __tablename__ = 'ratings'
    
#     id = db.Column(db.Integer, primary_key=True, index=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     book_id = db.Column(db.String(100), db.ForeignKey('books.id'), nullable=False)
#     rating = db.Column(db.Integer, nullable=False)
    
#     # Relationships
#     user = db.relationship("UserModel", back_populates="ratings")
#     book = db.relationship("BookModel", back_populates="ratings")

#     def to_dict(self):
#         return {"user_id": self.user_id, "book_id": self.book_id, "rating": self.rating}

# # Visualization class
# class VisualizationModel(db.Model):
#     __tablename__ = 'visualizations'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
#     reading_date = db.Column(db.Date, nullable=True)

#     # Relationships
#     user = db.relationship("UserModel", back_populates="visualizations")
#     book = db.relationship("BookModel", back_populates="visualizations")

# Users API Resource
# class Users(Resource):
#     def get(self):
#         users = UserModel.query.all()
#         return [user.to_dict() for user in users]

# api.add_resource(Users, '/api/users')




@app.route('/api/getBookDetail', methods=['GET'])
def get_book_detail():
    # from models.books import BookModel
    # from models.rating import RatingModel
    # Récupérer le paramètre bookId
    book_id = request.args.get('bookId')
    if not book_id:
        return jsonify({"error": "Missing bookId parameter"}), 400

    # Rechercher le livre dans la base de données
    book = BookModel.query.filter_by(id=book_id).first()
    if not book:
        return jsonify({"error": "Book not found"}), 404

    # Rechercher les évaluations liées au livre
    ratings = RatingModel.query.filter_by(book_id=book_id).all()

    # Calculer la note moyenne
    average_rating = (
        sum(rating.rating for rating in ratings) / len(ratings)
        if ratings else None
    )

    # Exemple d'utilisateur connecté (remplacez par la logique réelle)
    current_user_id = 1
    user_rating = next(
        (rating.rating for rating in ratings if rating.user_id == current_user_id), None
    )

    # Formater la réponse
    response = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "description": book.desc,
        "genres": book.genres.split(",") if book.genres else [],
        # "coverImg": book.cover_img_url,
        "price": float(book.price),
        "averageRating": round(average_rating, 2) if average_rating else None,
        "userRating": user_rating
    }

    return jsonify(response)


@app.route('/api/getUserList', methods=['GET'])
def get_user_list():
    # from models.users import UserModel
    # Récupérer tous les utilisateurs de la base de données
    users = UserModel.query.all()

    # Formater les données
    user_list = [
        {
            "id": user.id,  # Format personnalisé pour l'ID
            "age": user.age,
            "generi_preferiti": user.generi_preferiti
        }
        for user in users
    ]

    # Retourner la liste d'utilisateurs en JSON
    return jsonify(user_list)


@app.route('/api/updateUserRating', methods=['PUT'])
def update_user_rating():
    # from models.books import BookModel
    # from models.users import UserModel
    # from models.rating import RatingModel
    data = request.get_json()
    user_id = data.get('userId')
    book_id = data.get('bookId')
    user_rating = data.get('userRating')
    print(data)
    print(user_id)
    print(book_id)
    print(user_rating)

    if user_id is None or book_id is None or user_rating is None:
        return jsonify({"error": "Missing required parameters"}), 400

    user = UserModel.query.filter_by(id=user_id).first()
    book = BookModel.query.filter_by(id=book_id).first()

    if not user or not book:
        return jsonify({"error": "User or Book not found"}), 404

    user_rating_entry = RatingModel.query.filter_by(user_id=user.id, book_id=book.id).first()
    if user_rating_entry:
        user_rating_entry.rating = user_rating
    else:
        new_rating = RatingModel(user_id=user.id, book_id=book.id, rating=user_rating)
        db.session.add(new_rating)

    # Recalculate the average rating for the book
    all_ratings = RatingModel.query.filter_by(book_id=book.id).all()
    average_rating = sum([rating.rating for rating in all_ratings]) / len(all_ratings)

    book.avg_vote = average_rating
    db.session.commit()

    book_data = {
        "id": str(book.id),
        "title": book.title,
        "author": book.author,
        "genres": book.genres.split(",") if book.genres else [],
        "averageRating": round(book.avg_vote, 1),
        "userRating": user_rating
    }

    return jsonify(book_data)

@app.route('/api/getBookList', methods=['GET'])
def get_book_list():
    # Récupérer les paramètres de la requête
    user_id = request.args.get('userId')  # Le paramètre userId (non utilisé ici mais pourrait être ajouté pour la logique)
    sort_criteria = request.args.get('sortCriteria')  # Le paramètre sortCriteria

    # Vérification de la présence du paramètre sortCriteria
    if not sort_criteria:
        return jsonify({"error": "Missing sortCriteria parameter"}), 400

    # Exemple de données fictives (normalement, cela serait récupéré à partir de la base de données)
    book_list = [
        {
            "id": "2",
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genres": ["Classic", "Fiction"],
            "averageRating": 4.4,
            "userRating": None
        },
        {
            "id": "1",
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "genres": ["Classic", "Historical", "Fiction"],
            "averageRating": 4.8,
            "userRating": 4
        },
        {
            "id": "5",
            "title": "1984",
            "author": "George Orwell",
            "genres": ["Dystopian", "Science Fiction", "Classic"],
            "averageRating": 4.7,
            "userRating": 5
        },
        {
            "id": "4",
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "genres": ["Classic", "Fiction"],
            "averageRating": 3.9,
            "userRating": 3
        },
        {
            "id": "3",
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "genres": ["Classic", "Romance"],
            "averageRating": 4.6,
            "userRating": 4
        }
    ]

    # Retourner la réponse sous forme de JSON
    return jsonify({
        "sortCriteria": sort_criteria,
        "books": book_list
    })

# Exportation du modèle pour créer les tables
if __name__ == "__main__":
    app.run(debug=True)

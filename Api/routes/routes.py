from flask import jsonify, request,render_template
# from api import app, db  # Import the app instance created in _init_.py
from flask_cors import CORS, cross_origin
from random import randint
# from backend.app.controllers.userController import load_users_from_csv
# from data.user import lista_utenti
# from app.controllers import authController
import csv

from models.users import UserModel
from models.books import BookModel
from models.rating import RatingModel
from models.visualizations import VisualizationModel

from flask import Blueprint

routes = Blueprint('routes', __name__)

# books=[]

# @app.route('/users', methods=['GET'])
# def index():
#     print(lista_utenti)
#     return render_template('index.html')
# # POST /api/getOrder - Handles the sorting based on the ratedBooks and sortCriteria
# @app.route('/api/getOrder', methods=['POST', 'OPTIONS'])
# def get_order():
#     if request.method == 'OPTIONS':
#         return _build_cors_prelight_response()
    
#     data = request.json
#     current_user = data.get('currentUser')
#     rated_books = data.get('ratedBooks')
#     sort_criteria = data.get('sortCriteria')
    
#     print(f"Received request from user: {current_user}")
#     print(f"Rated books: {rated_books}")
#     print(f"Sort Criteria: {sort_criteria}")

#     # Example: Sort books by rating if sortCriteria is "Similar Content"
#     if sort_criteria == "Similar Content":
#         sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Sort by rating
#         return jsonify({"sortedBooks": sorted_books})

#     elif sort_criteria == "Similar Authors":
#         sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
#         return jsonify({"sortedBooks": sorted_books})

#     elif sort_criteria == "Similar Categories":
#         sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
#         return jsonify({"sortedBooks": sorted_books})

#     elif sort_criteria == "Similar Page-length":
#         sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
#         return jsonify({"sortedBooks": sorted_books})

#     return jsonify({"message": "No valid sorting criteria provided"}), 400

# def _build_cors_prelight_response():
#     response = jsonify()
#     response.headers.add("Access-Control-Allow-Origin", "http://localhost:4200")
#     response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
#     return response


#     # Route de connexion
# @app.route('/login', methods=['POST'])
# def login():
#     return authController.login()

# @app.route('/load_users', methods=['POST'])
# def load_users():
#     return load_users_from_csv()


@routes.route('/api/getBookDetail', methods=['GET'])
def get_book_detail():
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


@routes.route('/api/getUserList', methods=['GET'])
def get_user_list():
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


@routes.route('/api/updateUserRating', methods=['PUT'])
def update_user_rating():
    from api import db
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

@routes.route('/api/getBookList', methods=['GET'])
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


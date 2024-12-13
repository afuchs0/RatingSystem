from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from flask_restful import Resource, Api

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from RecSystem.CBF.cbf import cbf
from RecSystem.CFI.cfi import cfi
from RecSystem.CFU.cfu import cfu_single_user
from RecSystem.Qlearning.applyQlearning import qlearning


app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)
app.secret_key = 'your_secret_key'  # Clé secrète pour les sessions Flask

# Initialisation de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 
# Configuration CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.register_blueprint(routes)


class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    #idd = db.Column(db.Integer, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)  # Integer type for age
    #email = db.Column(db.String(100), nullable=False, unique=False)
    #generi_preferiti = db.Column(db.Text)  # Storing JSON as Text

    #ratings = db.relationship("RatingModel", back_populates="user")
    #visualizations = db.relationship("VisualizationModel", back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            #"idd": self.idd,
            "age": self.age
            #"email": self.email,
            #"generi_preferiti": json.loads(self.generi_preferiti) if self.generi_preferiti else []
        }
    
    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
    @property
    def is_active(self):
        return True
    
    def get_id(self):
        return str(self.id)

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
    awards = db.Column(db.String(100), nullable=True)
    #numRatings = db.Column(db.String(100), nullable=True)
    #ratingsByStars = db.Column(db.JSON(db.String(100)), nullable=True)  # Fixed misplaced parenthesis
    #likedPercent = db.Column(db.String(100), nullable=True)
    #setting = db.Column(db.JSON(db.String(100)), nullable=True)  # Fixed misplaced parenthesis
    coverImg = db.Column(db.String(200), nullable=True)
    #bbeScore = db.Column(db.String(100))
    #bbeVotes = db.Column(db.String(100), nullable=True)
    price = db.Column(db.String(100), nullable=True)

    # Relationships
    #ratings = db.relationship("RatingModel", back_populates="book")
    #visualizations = db.relationship("VisualizationModel", back_populates="book")
    #genres = db.relationship('Belong', back_populates='book')

    def to_dict(self):
        return {
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

# GENRES Table
class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # Genre name

    # Relationships
    #books = db.relationship('Belong', back_populates='genre', cascade='all, delete-orphan')
    #favourites = db.relationship('Favourite', back_populates='genre', cascade='all, delete-orphan')
    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name
            }

# Rating class
class RatingModel(db.Model):
    __tablename__ = 'ratings'
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.String(100), db.ForeignKey('books.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    # Relationships
    #user = db.relationship("UserModel", back_populates="ratings")
    #book = db.relationship("BookModel", back_populates="ratings")

    def to_dict(self):
        return {
                "user_id": self.user_id,
                "book_id": self.book_id,
                "rating": self.rating
            }

# Visualization class
class VisualizationModel(db.Model):
    __tablename__ = 'visualizations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.String(100), db.ForeignKey('books.id'), nullable=False)
    reading_date = db.Column(db.Date, nullable=True)

    # Relationships
    #user = db.relationship("UserModel", back_populates="visualizations")
    #book = db.relationship("BookModel", back_populates="visualizations")
    def to_dict(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "book_id": self.book_id,
                "reading_date": self.reading_date
                }

# BELONG Table (Many-to-Many between Books and Genres)
class Belong(db.Model):
    __tablename__ = 'belong'
    id = db.Column(db.Integer, primary_key=True)
    genres_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    book_id = db.Column(db.String(100), db.ForeignKey('books.id'), nullable=False)

    # Relationships
    #genre = db.relationship('Genre', back_populates='books')
    #book = db.relationship('Book', back_populates='genres')

    def to_dict(self):
        return {
            "id": self.id,
            "genres_id": self.genres_id,
            "book_id": self.book_id
        }

# FAVOURITE Table (Many-to-Many between Users and Genres)
class Favourite(db.Model):
    __tablename__ = 'favourite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    genres_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)

    # Relationships
    #user = db.relationship('UserModel', back_populates='favourites')
    #genre = db.relationship('Genre', back_populates='favourites')
    
    def to_dict(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "genres_id": self.genres_id
                }
    
# Users API Resource
class Users(Resource):
    def get(self):
        users = UserModel.query.all()
        return [user.to_dict() for user in users]

api.add_resource(Users, '/api/users')



@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))

#login founction 
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()  # Récupérer les données JSON envoyées par le client
    email = data.get('email')
    password = data.get('password_hash')

    # Vérifier les informations utilisateur
    user = UserModel.query.filter_by(email=email).first()
    if user and user.check_password(password):
        login_user(user)  # Connecter l'utilisateur
        return jsonify({"message": "login success", "user_id": user.id}), 200
    return jsonify({"message": "Email ou mot de passe incorrect"}), 401


#current user
@app.route('/api/current_user', methods=['GET'])
@login_required  # Protéger la route pour les utilisateurs connectés uniquement
def get_current_user():
    if  current_user.is_authenticated:
        return jsonify({
            "id": current_user.id,
            "email": current_user.email,
            "age": current_user.age,
            "generi_preferiti": json.loads(current_user.generi_preferiti or "[]")
        }), 200
    else:
        return 'Please log in to view your profile.'

# @app.route('/api/getBookList', methods=['GET'])
# def get_books():
#     books = BookModel.query.all()
#     return jsonify([book.to_dict() for book in books])

@app.route('/api/cazzifinti', methods=['GET'])
def ciao():
    try:
        # Ottieni tutti i libri
        books = BookModel.query.all()

        # Se non ci sono libri, restituisci una lista vuota
        if not books:
            return jsonify([]), 200

        # Converte i libri in dizionari
        books_list = [book.to_dict() for book in books]

        # Restituisce i dati come JSON
        return jsonify(books_list[0:100]), 200
    except Exception as e:
        # In caso di errore, restituisci il messaggio di errore
        return jsonify({"error": str(e)}), 500


@app.route('/api/getBookList', methods=['GET'])
def get_books():
    # Récupérer les paramètres
    user_id = request.args.get('userId')
    sort_criteria = request.args.get('sortCriteria')
    # Print pour déboguer
    print(f"Received userId: {user_id}")
    print(f"Received sortCriteria: {sort_criteria}")
    # Vérifier que les paramètres requis sont fournis
    if not user_id or not sort_criteria:
        return jsonify({"error": "Missing 'userId' or 'sortCriteria' parameter."}), 400

    # Récupérer tous les livres de la base de données
    books = BookModel.query.all()
    books_data = [book.to_dict() for book in books]

    # Variable pour stocker l'ordre trié des livres
    sorted_books = []

    # Logique basée sur le critère de tri
    if sort_criteria == "Content Based Filtering":
        recommendations = cbf(user_id)  # Appel de la fonction Content-Based Filtering
    elif sort_criteria == "Collaborative Filtering Userbased":
        recommendations = cfi(user_id)  # Appel CF User-based
    elif sort_criteria == "Collaborative Filtering Itembased":
        recommendations = cfu_single_user(user_id)  # Appel CF Item-based
    elif sort_criteria == "Q-Learning":
        recommendations = qlearning(user_id)  # Appel Q-Learning
    # elif sort_criteria == "DQN":
    #     recommendations = dqn_recommendations(user_id)  # Appel DQN
    else:
        return jsonify({"error": f"Invalid sortCriteria: {sort_criteria}"}), 400

    # Trier les livres en fonction des recommandations
    if recommendations:
        book_id_order = recommendations  # Les IDs des livres triés
        # Trier les livres par leur ordre dans les recommandations
        if sort_criteria != "Q-Learning":
            sorted_books = sorted(books_data, key=lambda x: book_id_order.index(x['id']) if x['id'] in book_id_order else len(book_id_order))
        else:
            sorted_books = sorted(books_data, key=lambda x: book_id_order.index(x['bookId']) if x['bookId'] in book_id_order else len(book_id_order))
        
    else:
        # Si aucune recommandation, renvoyer les livres sans ordre spécifique
        sorted_books = books_data

    # Construire la réponse
    response = {
        "sortCriteria": sort_criteria,
        "books": sorted_books[0:100]
    }

    return jsonify(response), 200

# @app.route('/api/getBookDetail', methods=['GET'])
# def get_book_detail():
#     # Retrieve the bookId parameter
#     book_id = request.args.get('bookId')
#     if not book_id:
#         return jsonify({"error": "Missing bookId parameter"}), 400
#     print(book_id)
#     # Query to join books, belong, and genres
#     results = (
#         db.session.query(
#             BookModel.id,
#             BookModel.title,
#             BookModel.author,
#             Genre.name.label("genre_name")  # Genre name
#         )
#         .join(Belong, BookModel.bookId == Belong.book_id)  # Join with belong
#         .join(Genre, Belong.genres_id == Genre.id)  # Join with genres
#         .filter(BookModel.bookId == book_id)  # Filter by bookId
#         .all()
#     )
#     print(results)

#     if not results:
#         return jsonify({"error": "Book not found"}), 404

#     # Group genres for the book
#     book_dict = None
#     genres = []
#     for book_id, title, author, genre_name in results:
#         if not book_dict:
#             book_dict = {
#                 "id": book_id,
#                 "title": title,
#                 "author": author,
#                 "genres": []
#             }
#         genres.append(genre_name)

#     book_dict["genres"] = genres

#     # json return
#     return jsonify(book_dict)

@app.route('/api/getBookDetail', methods=['GET'])
def get_book_detail():
    # Retrieve the bookId parameter
    book_id = request.args.get('bookId')
    if not book_id:
        return jsonify({"error": "Missing bookId parameter"}), 400

    print(f"Book ID requested: {book_id}")

    # Query to join books, belong, and genres
    results = (
        db.session.query(
            BookModel.id,
            BookModel.title,
            BookModel.author,
            Genre.name.label("genre_name")  # Genre name
        )
        .join(Belong, BookModel.bookId == Belong.book_id)  # Join with belong
        .join(Genre, Belong.genres_id == Genre.id)  # Join with genres
        .filter(BookModel.bookId == book_id)  # Filter by bookId
        .all()
    )

    if not results:
        return jsonify({"error": "Book not found"}), 404

    # Group genres for the book
    book_dict = None
    genres = []
    for book_id, title, author, genre_name in results:
        if not book_dict:
            book_dict = {
                "id": book_id,
                "title": title,
                "author": author,
                "genres": []
            }
        genres.append(genre_name)

    book_dict["genres"] = genres

    # Call each recommendation function and determine the ranking of the book
    user_id = request.args.get('userId')
    if not user_id:
        return jsonify({"error": "Missing userId parameter for ranking"}), 400

    rankings = {}

    # Content-Based Filtering
    cbf_recommendations = cbf(user_id)
    if cbf_recommendations and book_id in cbf_recommendations:
        rankings["Content Based Filtering"] = cbf_recommendations.index(book_id) + 1
    else:
        rankings["Content Based Filtering"] = None

    # Collaborative Filtering User-based
    cfu_recommendations = cfi(user_id)
    if cfu_recommendations and book_id in cfu_recommendations:
        rankings["Collaborative Filtering Userbased"] = cfu_recommendations.index(book_id) + 1
    else:
        rankings["Collaborative Filtering Userbased"] = None

    # # Collaborative Filtering Item-based
    # cfi_recommendations = cfu_single_user(user_id)
    # if cfi_recommendations and book_id in cfi_recommendations:
    #     rankings["Collaborative Filtering Itembased"] = cfi_recommendations.index(book_id) + 1
    # else:
    #     rankings["Collaborative Filtering Itembased"] = None

    # # Q-Learning
    # qlearning_recommendations = qlearning(user_id)
    # if qlearning_recommendations and book_id in qlearning_recommendations:
    #     rankings["Q-Learning"] = qlearning_recommendations.index(book_id) + 1
    # else:
    #     rankings["Q-Learning"] = None

    # Add rankings to the response
    book_dict["rankings"] = rankings

    # Return the response as JSON
    return jsonify(book_dict)


# get users 
@app.route('/api/getUserList', methods=['GET'])
def get_user_list():
    # join between users, favourite e genres
    results = (
        db.session.query(
            UserModel.id,  
            UserModel.age, 
            Genre.name.label("genre_name")  # genre name
        )
        .join(Favourite, UserModel.id == Favourite.user_id)  # Join with table favourite
        .join(Genre, Favourite.genres_id == Genre.id)  # Join with genres
        .all()
    )
    
    # group results
    user_dict = {}
    for user_id, age, genre_name in results:
        if user_id not in user_dict:
            user_dict[user_id] = {
                "id": user_id,
                "age": age,
                "generi_preferiti": []
            }
        user_dict[user_id]["generi_preferiti"].append(genre_name)

    # converts dictionary in user list
    user_list = list(user_dict.values())

    # json return
    return jsonify(user_list)


@app.route('/api/updateUserRating', methods=['PUT'])
def update_user_rating():
    data = request.get_json()
    user_id = data.get('userId')
    book_id = data.get('bookId')
    user_rating = data.get('userRating')

    if user_id is None or book_id is None or user_rating is None:
        return jsonify({"error": "Missing required parameters"}), 400

    # Debugging information
    print(f"Book ID: {book_id}, User ID: {user_id}, Rating: {user_rating}")

    # Vérification de l'existence de l'utilisateur et du livre
    user = UserModel.query.filter_by(id=user_id).first()
    book = BookModel.query.filter_by(bookId=book_id).first()

    if not user or not book:
        return jsonify({"error": "User or Book not found"}), 404

    # Mise à jour ou création de l'entrée de notation
    user_rating_entry = RatingModel.query.filter_by(user_id=user.id, book_id=book.id).first()
    if user_rating_entry:
        user_rating_entry.rating = user_rating
    else:
        new_rating = RatingModel(user_id=user.id, book_id=book.id, rating=user_rating)
        db.session.add(new_rating)

    # Recalcul de la note moyenne pour le livre
    all_ratings = RatingModel.query.filter_by(book_id=book.id).all()
    average_rating = sum([rating.rating for rating in all_ratings]) / len(all_ratings)
    book.avg_vote = average_rating
    db.session.commit()

    # Fetch genres exactly like in `get_user_list`
    genres_results = (
        db.session.query(
            UserModel.id, 
            Genre.name.label("genre_name")  # Genre name
        )
        .join(Favourite, UserModel.id == Favourite.user_id)  # Join with table favourite
        .join(Genre, Favourite.genres_id == Genre.id)  # Join with genres
        .filter(UserModel.id == user_id)  # Filter by current user ID
        .all()
    )

    # Process genres into a list
    genres = [genre_name for _, genre_name in genres_results]

    # Création de la réponse avec les données du livre
    book_data = {
        "id": str(book.id),
        "title": book.title,
        "author": book.author,
        "genres": genres,  # Use the processed genres list
        "averageRating": round(book.avg_vote, 1),
        "userRating": user_rating
    }

    return jsonify(book_data)



#recherche personnalisee
@app.route('/api/books/research', methods=['GET'])
def research():
    # Récupération des paramètres de requête
    title = request.args.get('title')
    lang = request.args.get('language')
    price = request.args.get('price', type=float)
    desc = request.args.get('description')

    # Initialisation de la requête
    query = BookModel.query

    # Ajout des filtres dynamiques
    if title:
        query = query.filter(BookModel.title.ilike(f"%{title}%"))
    if lang:
        query = query.filter(BookModel.language.ilike(f"%{lang}%"))
    if price:
        query = query.filter(BookModel.price <= price)  
    if desc:
        query = query.filter(BookModel.description.ilike(f"%{desc}%"))

    try:
        # Exécution de la requête
        books = query.all()
        if not books:
            return jsonify({"message": "No books found matching your criteria."}), 404
        
        # Retourner les résultats
        return jsonify([book.to_dict() for book in books]), 200

    except Exception as e:
        # Gestion des erreurs
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Exportation du modèle pour créer les tables
if __name__ == "__main__":
    app.run(debug=True)
    

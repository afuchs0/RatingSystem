from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from flask_restful import Resource, Api

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

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
    idd = db.Column(db.Integer, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)  # Integer type for age
    email = db.Column(db.String(100), nullable=False, unique=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Renamed for clarity
    generi_preferiti = db.Column(db.Text)  # Storing JSON as Text

    ratings = db.relationship("RatingModel", back_populates="user")
    visualizations = db.relationship("VisualizationModel", back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "idd": self.idd,
            "age": self.age,
            "email": self.email,
            "generi_preferiti": json.loads(self.generi_preferiti) if self.generi_preferiti else []
        }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)

    def set_generi_preferiti(self, generi_preferiti):
        self.generi_preferiti = json.dumps(generi_preferiti)
    @property
    def is_active(self):
        # Retourne True si l'utilisateur est actif. Changez cette logique si nécessaire.
        return True
    

    def get_id(self):
        return str(self.id)

# Book class
class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    bookId = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(100), nullable=True)
    series = db.Column(db.String(100), nullable=True)
    author = db.Column(db.String(100))
    rating = db.Column(db.String(100))
    description = db.Column(db.String(100))
    language = db.Column(db.String(100), nullable=True)
    isbn = db.Column(db.String(100), nullable=True)
    genres = db.Column(db.JSON(db.String(100)), nullable=True)
    characters = db.Column(db.JSON(db.String(100)), nullable=True)  # Corrected typo: "charaters" -> "characters"
    bookFormat = db.Column(db.String(100), nullable=True)
    edition = db.Column(db.String(100), nullable=True)
    pages = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=True)
    publishDate = db.Column(db.String(100), nullable=True)
    firstPublishDate = db.Column(db.String(100), nullable=True)  # Fixed typo: "firtPublisherDate" -> "firstPublisherDate"
    awards = db.Column(db.JSON(db.String(100)), nullable=True)
    numRatings = db.Column(db.String(100), nullable=True)
    ratingsByStars = db.Column(db.JSON(db.String(100)), nullable=True)  # Fixed misplaced parenthesis
    likedPercent = db.Column(db.String(100), nullable=True)
    setting = db.Column(db.JSON(db.String(100)), nullable=True)  # Fixed misplaced parenthesis
    coverImg = db.Column(db.String(200), nullable=True)
    bbeScore = db.Column(db.String(100))
    bbeVotes = db.Column(db.String(100), nullable=True)
    price = db.Column(db.String(100), nullable=True)

    # Relationships
    ratings = db.relationship("RatingModel", back_populates="book")
    visualizations = db.relationship("VisualizationModel", back_populates="book")

    # id = db.Column(db.String(100), primary_key=True)
    # title = db.Column(db.String(100), nullable=False)
    # serie = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
    # desc = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
    # lang = db.Column(db.String(100), nullable=True)  # Made nullable True if optional
    # pages = db.Column(db.Integer, nullable=True)  # Made nullable True for optional pages
    # nawards = db.Column(db.Integer, nullable=False, default=0)  # Default value for awards
    # avg_vote = db.Column(db.Float, nullable=True, default=0.0)  # Default value for avg_vote
    # price = db.Column(db.Float, nullable=True)  # Changed to Float for price
    # author = db.Column(db.String(100), nullable=False)
    # genres = db.Column(db.String(200), nullable=True)  # Increased size for genres (if a list)
    # Relationships
   
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
            "isbn": self.isbn,
            "genres": self.genres,
            "characters": self.characters,  # Corrected typo: "charaters" -> "characters"
            "bookFormat": self.bookFormat,
            "edition": self.edition,
            "pages": self.pages,
            "publisher": self.publisher,
            "publishDate": self.publishDate,
            "firstPublishDate": self.firstPublishDate,  # Corrected typo: "firtPublisherDate" -> "firstPublisherDate"
            "awards": self.awards,
            "numRatings": self.numRatings,
            "ratingsByStars": self.ratingsByStars,
            "likedPercent": self.likedPercent,
            "setting": self.setting,
            "coverImg": self.coverImg,
            "bbeScore": self.bbeScore,
            "bbeVotes": self.bbeVotes,  # Corrected typo: "bbVote" -> "bbeVote"
            "price": self.price,
        }
    
    # def to_dict(self):
    #     return {
    #         "id": self.id, 
    #         "title": self.title, 
    #         "serie": self.serie, 
    #         "desc": self.desc, 
    #         "lang": self.lang, 
    #         "naward": self.nawards, 
    #         "avg_vote": self.avg_vote,
    #         "price": self.price, 
    #         "author": self.author,
    #         "genres": self.genres
    #     }

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)

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

@app.route('/api/getBookList', methods=['GET'])
def get_books():
    books = BookModel.query.all()
    return jsonify([book.to_dict() for book in books])

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

# get users 
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
            #"email":user.email,
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

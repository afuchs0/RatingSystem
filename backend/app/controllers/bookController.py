from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from backend.app.models.books import Book
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
# Configurer la connexion à la base de données
DATABASE_URL = 'sqlite:///library.db'  # Remplacez par votre URL de base de données
engine = create_engine(DATABASE_URL)
Book.metadata.create_all(engine)  # Crée les tables si elles n'existent pas encore
Session = sessionmaker(bind=engine)

#find books 
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])


#create 
def load_books_from_csv(file_path):
    # Créer une nouvelle session
    session = Session()
    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(file_path)
    # Convertir chaque ligne en objet Book et l'ajouter à la session
    for _, row in df.iterrows():
        book = Book(
            bookId=row['bookId'],
            title=row['title'],
            series=row['series'],
            author=row.get('author'),
            rating=row.get('rating'),
            description=row.get('description'),
            language=row['language'],
            isbn=row['isbn'],
            genres=row['genres'].split(',') if 'genres' in row and pd.notna(row['genres']) else None,
            characters=row['characters'].split(',') if 'characters' in row and pd.notna(row['characters']) else None,
            bookFormat=row.get('bookFormat'),
            edition=row.get('edition'),
            pages=row['pages'],
            publisher=row.get('publisher'),
            publishDate=row.get('publishDate'),
            firstPublisherDate=row.get('firstPublisherDate'),
            awards=row['awards'].split(',') if 'awards' in row and pd.notna(row['awards']) else None,
            numRating=row.get('numRating'),
            ratingsByStars=row['ratingsByStars'].split(',') if 'ratingsByStars' in row and pd.notna(row['ratingsByStars']) else None,
            likedPercent=row.get('likedPercent'),
            setting=row['setting'].split(',') if 'setting' in row and pd.notna(row['setting']) else None,
            coverImg=row['coverImg'].split(',') if 'coverImg' in row and pd.notna(row['coverImg']) else None,
            bbeScore=row.get('bbeScore'),
            bbeVote=row.get('bbeVote'),
            price=row['price']
        )
        session.add(book)

    # Valider et fermer la session
    session.commit()
    session.close()

# Appeler la fonction pour charger les livres depuis un fichier CSV
load_books_from_csv('books.csv')


# creation des livres 
def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'],
                    serie=data ['serie'], 
                    desc=data['desc'], 
                    lang=data['lang'], 
                    ISBN=data['ISBN'], 
                    naward=data['naward'], 
                    avg_vote=data['avg_vote'],
                    price=data['price'], 
                    author=data['author'],
                    genres=data ['genres'])
    try:
        db.session.add(new_book)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Database Integrity Error", "message": str(e)}), 400
    return jsonify(new_book.to_dict()), 201


##update book  
def upadte(book_id):
    data= request.get_json()
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error":"book not found"}), 404
    book.update(data)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Update failed", "message": str(e)}), 400
    
    return jsonify(book.to_dict()), 200

#research 
def research():
    title = request.args.get('title')
    lang= request.args.get('language')
    price= request.args.get('price')
    desc = request.args.get('desc')

    query=Book.requery
    
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if lang: 
        query= query.filter(Book.lang.ilike(f"%{lang}%"))
    if price: 
        query = query.filter(Book.price.ilike(f"%{price}%"))
    if desc: 
        query = query.filter(Book.desc.ilike(f"%{desc}%"))

    try:
        books = query.all()
        
    except Exception as e:
        return jsonify({"error":"Book  not found"}), 404
    return jsonify([book.to_dict() for book in books])
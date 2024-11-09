from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from backend.app.models.books import Book

db = SQLAlchemy()


#find books 
def get_books():
    new_books = Book.query.all()
    return jsonify([book.to_dict() for book in Book])


#create 

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
    lang= request.args.get('lang')
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
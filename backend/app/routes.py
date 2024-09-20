from flask import jsonify, request
from app import app  # Import the app instance created in __init__.py
from flask_cors import CORS, cross_origin
from random import randint
import csv
import pandas as pd
class User:
    def __init__(self, id, nome,voting,prefgenre,eta):
        self.id = id
        self.nome = nome
        self.voting = voting
        self.prefgenre = prefgenre
        self.eta = eta
    def add_val(self,key, value):
        self.voting[key] = value
    def add_pref(self,gen):
        self.prefgenre.append(gen)

class Book:
    def __init__(self, id, title, serie, author, desc, lang, ISBN, genres, npag, nawards, avg_vote, price):
        self.id = id
        self.title = title
        self.serie = serie
        self.autore = author
        self.desc = desc
        self.lang = lang
        self.ISBN = ISBN
        self.genres = genres
        self.npag = npag
        self.nawards = nawards
        self.avg_vote = avg_vote
        self.prezzo = price
# Example book data (in-memory)
lista_utenti = [
    User(1, "Alice", {}, ["Fantascienza"], 25),
    User(2, "Marco", {}, ["Fantasy"], 30),
    User(3, "Giulia", {}, ["Romance"], 28),
    User(4, "Luca", {}, ["Horror"], 22),
    User(5, "Sara", {}, ["Giallo"], 35),
    User(6, "Tommaso", {}, ["Avventura"], 40)
]
lista_utenti[0].add_val(101, 5)  # Alice vota il libro con ID 101 con 5
lista_utenti[1].add_val(102, 4)  # Marco vota il libro con ID 102 con 4
lista_utenti[2].add_val(103, 3)  # Giulia vota il libro con ID 103 con 3

# Aggiungere generi preferiti per alcuni utenti
lista_utenti[3].add_pref("Thriller")  # Luca aggiunge il genere Thriller
lista_utenti[4].add_pref("Storico")   # Sara aggiunge il genere Storico






# Function to convert the CSV into a static list of Book objects with only the required attributes
def csv_to_books(file_path):

    data = pd.read_csv(file_path)
    
    books = []
    # Loop over the dataframe rows and create Book objects
    for _, row in data.iterrows():
        if row['price'] == '':
            row['price'] = randint(1,20)
        book = Book(
            id=row['bookId'],
            title=row['title'],
            serie=row['series'],
            author=row['author'],
            desc=row['description'],
            lang=row['language'],
            ISBN=row['isbn'],
            genres=row['genres'],
            npag=row['pages'],
            nawards=row['awards'],
            avg_vote=row['likedPercent'],
            price=row['price']
        )
        books.append(book)
    
    return books


# Convert the CSV to a list of Book objects
books_list = csv_to_books("books.csv")


print(lista_utenti)














# POST /api/getOrder - Handles the sorting based on the ratedBooks and sortCriteria
@app.route('/api/getOrder', methods=['POST', 'OPTIONS'])
def get_order():
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    
    data = request.json
    current_user = data.get('currentUser')
    rated_books = data.get('ratedBooks')
    sort_criteria = data.get('sortCriteria')
    
    print(f"Received request from user: {current_user}")
    print(f"Rated books: {rated_books}")
    print(f"Sort Criteria: {sort_criteria}")

    # Example: Sort books by rating if sortCriteria is "Similar Content"
    if sort_criteria == "Similar Content":
        sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Sort by rating
        return jsonify({"sortedBooks": sorted_books})

    elif sort_criteria == "Similar Authors":
        sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
        return jsonify({"sortedBooks": sorted_books})

    elif sort_criteria == "Similar Categories":
        sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
        return jsonify({"sortedBooks": sorted_books})

    elif sort_criteria == "Similar Page-length":
        sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
        return jsonify({"sortedBooks": sorted_books})

    return jsonify({"message": "No valid sorting criteria provided"}), 400

def _build_cors_prelight_response():
    response = jsonify()
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:4200")
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

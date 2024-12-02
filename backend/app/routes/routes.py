from flask import  Blueprint, Flask, jsonify, request,render_template
from app import app  # Import the app instance created in _init_.py
#from flask_cors import CORS, cross_origin
#from random import randint
#from backend.app.controllers.userController import load_users_from_csv
#from data.user import lista_utenti
#from app.controllers import authController


books=[]
rt = Blueprint('routes', __name__)
@app.route('/users', methods=['GET'])
def index():
    #print(lista_utenti)
    return render_template('index.html')
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



    # Route de connexion
#@app.route('/login', methods=['POST'])
#def login():
#    return authController.login()




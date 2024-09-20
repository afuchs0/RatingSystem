from flask import jsonify, request
from app import app  # Import the app instance created in __init__.py
from flask_cors import CORS, cross_origin

# Example book data (in-memory)
books = [
    {"id": 1, "title": "Book1", "author": "Suzanne Collins", "genres": ["Young Adult", "Fiction"], "rating": 4.3},
    {"id": 2, "title": "Book2", "author": "J.K. Rowling", "genres": ["Fantasy", "Adventure"], "rating": 4.8},
    {"id": 3, "title": "Book3", "author": "George Orwell", "genres": ["Dystopian", "Science Fiction"], "rating": 4.0},
]

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

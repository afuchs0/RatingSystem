from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/books')
def get_books():
    return {'books': ['Book 1', 'Book 2']}

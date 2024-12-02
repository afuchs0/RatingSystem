#from app import app
from flask import Flask, render_template
from flask import Flask, jsonify, request
from flask_sqlalchemy  import SQLAlchemy

from app.controllers.userController import load_users_from_csv



app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialiser SQLAlchemy
db = SQLAlchemy(app)
  
@app.before_request
def before_request_func():
    db.create_all()

# Définir la route de l'URL principale ("/")
@app.route('/us')
def index():
    return render_template('index.html')

@app.route('/load_users', methods=['POST'])
def load_users():
    return jsonify({load_users_from_csv()})


if __name__ == '__main__':
    app.run(debug=True)
   


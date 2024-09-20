from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')  # Loads the configurations
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow CORS for any URL starting with "/api/"


from RatingSystem.backend.app.routes import routes  #Import routes after the app is initialized

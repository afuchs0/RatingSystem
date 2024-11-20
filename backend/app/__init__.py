from flask import Flask
#from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')  # Loads the configurations
#CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow CORS for any URL starting with "/api/"
app.config["JWT_SECRET_KEY"] = "votre_secret_pour_jwt"  
jwt = JWTManager(app)


from RatingSystem.backend.app.routes import routes  #Import routes after the app is initialized

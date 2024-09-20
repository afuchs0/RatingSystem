from flask import Flask

app = Flask(__name__)
app.config.from_object('config')  # configurations

from app import routes  # imports routes

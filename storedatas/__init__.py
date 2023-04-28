from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.init_app(app)


from storedatas import routes

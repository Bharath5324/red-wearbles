from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager
import firebase_admin
from firebase_admin import credentials
app = Flask (__name__)
login = LoginManager(app)
cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://nodemcu-1206.firebaseio.com/'})
# login.login_view = 'webapp.routes.signin'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import routes, models
routes.init_app(app)
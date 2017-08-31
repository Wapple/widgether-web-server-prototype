from flask_login import LoginManager
from flask_pymongo import PyMongo

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'accounts.login'

mongo = PyMongo()
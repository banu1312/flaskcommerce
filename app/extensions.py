from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
db = SQLAlchemy()
mongo = PyMongo()
migrate = Migrate()
jwt = JWTManager()
BLACKLIST = set()
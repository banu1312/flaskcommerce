from flask import Flask
from .extensions import db, mongo, migrate,jwt
import os
from dotenv import load_dotenv
load_dotenv()
from .extensions import BLACKLIST
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/db_ecommerce'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/db_ecommerce'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "jwtsecret")
    app.config['SECRET_KEY']= 'supersecret'
    app.config['JWT_SECRET_KEY'] = 'jwt-secret'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

    db.init_app(app)
    mongo.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return jti in BLACKLIST
    
    from . import model
    from . import mongoModel

    from app.route.auth import auth
    from app.route.product import product_bp
    from app.route.order import order_bp
    from app.route.review import review_bp
    from app.route.log import log_bp

    app.register_blueprint(auth, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(review_bp, url_prefix='/api/reviews')
    app.register_blueprint(log_bp, url_prefix='/api/logs')
    
    return app

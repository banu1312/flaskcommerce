from app.extensions import db
from ..extensions import bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='buyer')

    products = db.relationship('Product', backref='seller', lazy=True)
    orders = db.relationship('Order', backref='buyer', lazy=True)

    def hash_password(self):
        self.password = bcrypt.generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

from app.extensions import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    delete_flag = db.Column(db.Boolean, default = False)
    
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    order_items = db.relationship('OrderItem', backref='product', lazy=True)

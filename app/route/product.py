from flask import Blueprint, request, jsonify
from app.model.product import Product
from app import db
from flask_jwt_extended import jwt_required
from ..utils.decorators import role_required

product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.filter_by(delete_flag=False).all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'stock': p.stock,
        'description': p.description
    } for p in products])

@product_bp.route('/', methods=['POST'])
@jwt_required()
@role_required(['admin','seller'])
def create_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        price=data['price'],
        stock=data.get('stock', 0),
        description=data.get('description', ''),
        seller_id=data.get('seller_id', 1)
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created'})

@product_bp.route('/<int:product_id>', methods=['PUT'])
@jwt_required()
@role_required(['admin','seller'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()

    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    product.description = data.get('description', product.description)

    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@product_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
@role_required(['admin','seller'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    product.delete_flag = True
    db.session.commit()
    return jsonify({'message': 'Product soft-deleted successfully'})
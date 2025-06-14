from flask import Blueprint, request, jsonify
from app.model.order import Order, OrderItem
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.decorators import role_required

order_bp = Blueprint('order', __name__)

@order_bp.route('/', methods=['POST'])
@jwt_required()
@role_required(['admin','buyer'])
def create_order():
    data = request.get_json()
    user_id = get_jwt_identity()
    total_price = data.get('total_price')
    items = data.get('items')

    order = Order(user_id=user_id, total_price=total_price)
    db.session.add(order)
    db.session.commit()

    for item in items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity']
        )
        db.session.add(order_item)

    db.session.commit()
    return jsonify({'message': 'Order placed'})
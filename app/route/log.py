from flask import Blueprint, request, jsonify
from app import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..mongoModel import add_logs
log_bp = Blueprint('log', __name__)

@log_bp.route('/view', methods=['POST'])
@jwt_required()
def log_view():
    user_id = get_jwt_identity()
    data = request.get_json()
    add_logs(user_id,'view_product',data['product_id'])
    return jsonify({'message': 'Log recorded'})

@log_bp.route('/cart', methods=['POST'])
@jwt_required()
def log_cart():
    user_id = get_jwt_identity()
    data = request.get_json()
    add_logs(user_id,'add_to_cart',data['product_id'])
    return jsonify({'message': 'Cart log recorded'})
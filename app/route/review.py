from flask import Blueprint, request, jsonify
from app import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
from ..mongoModel import add_review
from ..utils.decorators import role_required

review_bp = Blueprint('review', __name__)

@review_bp.route('/<product_id>', methods=['POST'])
@jwt_required()
@role_required(['admin','buyer'])
def add_review(product_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    add_review(product_id,user_id,data['rating'],data.get('comment', ''))
    return jsonify({'message': 'Review added'})

@review_bp.route('/<product_id>', methods=['GET'])
def get_reviews(product_id):
    reviews = list(mongo.db.reviews.find({'product_id': product_id}))
    for r in reviews:
        r['_id'] = str(r['_id'])
    return jsonify(reviews)
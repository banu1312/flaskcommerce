from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, jwt_required,
    get_jwt_identity, create_refresh_token,get_jwt
)
from ..model import User
from ..extensions import db,BLACKLIST


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already registered"}), 409

    user = User(name=data["name"], email=data["email"], password=data["password"])
    user.hash_password()
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not user.check_password(data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    refresh_token = create_refresh_token(identity=str(user.id))


    return jsonify(access_token=access_token, refresh_token=refresh_token), 200


@auth.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })

@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    new_access_token = create_access_token(identity=str(current_user),additional_claims={"role": user.role})
    return jsonify(access_token=new_access_token)


@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]  # JWT ID
    BLACKLIST.add(jti)
    return jsonify({"message": "Successfully logged out"}), 200
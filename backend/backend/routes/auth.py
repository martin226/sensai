from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from argon2 import PasswordHasher, exceptions
from ..database import mongo
from datetime import datetime


auth = Blueprint("auth", __name__)
ph = PasswordHasher()


db = mongo["sensai"]
users_collection = db["users"]

default_user = {
    "email": "",
    "username": "",
    "password": "",
    "workout_log": [],
    "streak": 0,
    "created_at": None,
}


@auth.route("/register", methods=["POST"])
def register():
    user = request.json
    if "email" in user and "username" in user and "password" in user:
        user["password"] = ph.hash(user["password"])
    else:
        return make_response(jsonify({"message": "Bad request"}), 400)
    email_exists: bool = users_collection.find_one({"email": user["email"]})
    username_exists: bool = users_collection.find_one({"username": user["username"]})
    if not email_exists and not username_exists:
        user_obj = default_user.copy()
        user_obj["email"] = user["email"]
        user_obj["username"] = user["username"]
        user_obj["password"] = user["password"]
        user_obj["created_at"] = int(datetime.now().timestamp())
        users_collection.insert_one(user_obj)
        return make_response(jsonify({"message": "User registered"}), 201)
    else:
        return make_response(jsonify({"message": "User already exists"}), 400)


@auth.route("/token", methods=["POST"])
def token():
    user = request.json
    if "username" not in user and "password" not in user:
        return make_response(jsonify({"message": "Bad request"}), 400)
    user_from_db = users_collection.find_one({"username": user["username"]})
    if user_from_db:
        try:
            ph.verify(user_from_db["password"], user["password"])
            access_token = create_access_token(identity=user_from_db["username"])
            return make_response(jsonify({"access_token": access_token}), 200)
        except (exceptions.VerifyMismatchError):
            return make_response(jsonify({"message": "Unauthorized"}), 401)
    else:
        return make_response(jsonify({"message": "Not registered"}), 400)


@auth.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user_from_db = users_collection.find_one({"username": current_user})
    if user_from_db:
        del (
            user_from_db["_id"],
            user_from_db["password"],
        )
        return make_response(jsonify({"profile": user_from_db}), 200)
    else:
        return make_response(jsonify({"message": "Profile not found"}), 404)

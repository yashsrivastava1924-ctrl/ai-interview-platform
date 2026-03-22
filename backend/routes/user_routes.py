from flask import Blueprint, request, jsonify
from config.db import db
import jwt
from bson import ObjectId

user_bp = Blueprint("user", __name__)
SECRET = "secret"

@user_bp.route("/me", methods=["GET"])
def get_me():
    token = request.headers.get("Authorization")
    decoded = jwt.decode(token, SECRET, algorithms=["HS256"])

    user = db.users.find_one({"_id": ObjectId(decoded["id"])})
    user["_id"] = str(user["_id"])

    return jsonify(user)

@user_bp.route("/leaderboard", methods=["GET"])
def leaderboard():
    users = list(db.users.find().sort("points", -1).limit(10))

    for u in users:
        u["_id"] = str(u["_id"])

    return jsonify(users)
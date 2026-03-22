from flask import Blueprint, request, jsonify
from config.db import db
import bcrypt, jwt

auth_bp = Blueprint("auth", __name__)

SECRET = "secret"

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())

    user = {
        "name": data["name"],
        "email": data["email"],
        "password": hashed,
        "points": 0
    }

    db.users.insert_one(user)
    return jsonify({"msg": "User registered"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = db.users.find_one({"email": data["email"]})

    if not user:
        return jsonify({"error": "User not found"}), 400

    if not bcrypt.checkpw(data["password"].encode(), user["password"]):
        return jsonify({"error": "Wrong password"}), 400

    token = jwt.encode({"id": str(user["_id"])}, SECRET, algorithm="HS256")

    return jsonify({"token": token})
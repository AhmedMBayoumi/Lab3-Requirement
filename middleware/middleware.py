from flask import request, jsonify

Token = "adminSecretToken"

def authenticate_token():
    token = request.headers.get("Authorization")
    if token != f"Bearer {Token}":
        return jsonify({"error": "Unauthorized"}), 401

# app/routes/auth_routes.py

from flask import Blueprint, jsonify

# Create a Blueprint named 'auth_bp'
auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Auth routes working!"})


#!/usr/bin/python3
""" Flask Application """
from datetime import timedelta
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import json
import os
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not JWT_SECRET_KEY:
    print("JWT_SECRET_KEY is empty")
    exit(1)

app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY


jwt = JWTManager(app)


@app.teardown_appcontext
def close_db(_):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(_):
    """Handle the 404 page"""
    return jsonify({"error": "Not found"}), 200


if __name__ == "__main__":
    """Starts the API"""
    with app.app_context():
        app.run(threaded=True, debug=True)

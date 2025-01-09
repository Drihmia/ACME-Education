#!/usr/bin/python3
""" Flask Application """
from datetime import timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity, get_jwt, create_access_token, set_access_cookies
from datetime import datetime
from datetime import timedelta
from datetime import timezone
import json
import os
from models import storage
from api.v1.views import app_views, app_views_docs


app = Flask(__name__)
app.register_blueprint(app_views)
app.register_blueprint(app_views_docs)
# cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

cors = CORS(
    app,
    resources={r"/api/v1/*": {"origins": ["https://www.drihmia.tech", "https://drihmia.tech", "https://www.drihmia.me", "https://drihmia.me"]}},
    supports_credentials=True
)

# Location and name of cookie:
app.config["JWT_TOKEN_LOCATION"] = ["cookies", "headers"]
app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'

# Setting life time of cookies
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

# Securing cookies:
app.config['JWT_COOKIE_SECURE'] = True  # I'm using https for my webapp
app.config['JWT_COOKIE_HTTPONLY'] = True
app.config['JWT_COOKIE_SAMESITE'] = 'Lax'  # 'None'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_COOKIE_DOMAIN'] = '.drihmia.tech'
# app.config['JWT_COOKIE_DOMAIN'] = '.drihmia.me'

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not JWT_SECRET_KEY:
    print("JWT_SECRET_KEY is empty")
    exit(1)

app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY


jwt = JWTManager(app)


# From Flask-JWT's Documentations
# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
            print("acess token has been efeshed successfully")
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


@app.teardown_appcontext
def close_db(_):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(_):
    """Handle the 404 page"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """Starts the API"""
    with app.app_context():
        app.run(threaded=True, debug=os.getenv("DEBUG", False))

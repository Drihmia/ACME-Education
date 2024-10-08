#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint, request
from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from dotenv import load_dotenv, find_dotenv
from os import getenv
import jwt

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
app_views_docs = Blueprint('app_views_docs', __name__)
pathenv = find_dotenv()
load_dotenv(pathenv)


def role_required(roles):
    """
    A decorator to restrict access to routes based on user roles.

    This decorator checks if the current user's role is in the allowed roles.
    If the user does not have the required role, it returns a 403 Unauthorized response.

    Args:
        roles (list): A list of roles that are allowed to access the route.

    Returns:
        function: The wrapped function which checks the user's role before allowing access.

    Example:
        @app.route('/common', methods=['GET'])
        @roles_required(['teacher', 'student', 'dev'])
        def common_access():
            return jsonify({"msg": "Welcome! You have access to this common section"}), 200
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # print(request.url)
            valid_head  =False
            if "Authorization" in request.headers:
                auth = request.headers.get("Authorization")
                if "Bearer" in auth:
                    access_token = auth.split("Bearer")[1]
                    try:
                        current_user_data = jwt.decode(access_token, getenv("JWT_SECRET_KEY"), algorithms=["HS256"], options={"verify_signature": False}).get("sub", {})
                        valid_head = True
                    except jwt.ExpiredSignatureError:
                        print("Token has expired")
                    except jwt.InvalidTokenError:
                        print("Invalid token")
            if not valid_head:
                try:
                    # print("before:" ,"+" * 10)
                    verify_jwt_in_request()
                    # print("after:" ,"-" * 10)

                    current_user_data = get_jwt_identity()
                    # print("current_user_data:", current_user_data)
                    if not current_user_data:
                        return
                except Exception as e:
                    print("From decorator, cookies:", e)
                    return jsonify({"msg": "Forbidden access"}), 401

            current_user_role = current_user_data.get("role")
            if current_user_role not in roles:
                return jsonify({"msg": "Unauthorized access"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

from api.v1.views.index import *
from api.v1.views.lessons import *
from api.v1.views.teachers import *
from api.v1.views.students import *
from api.v1.views.dev import *
from api.v1.views.subjects import *
from api.v1.views.years import *
from api.v1.views.institutions import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.login import *
from api.v1.views.verify_email_registration import *
from api.v1.views.api_docs import *

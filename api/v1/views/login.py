#!/usr/bin/python3
"""Define the State API"""
import bcrypt
from flask import jsonify, request
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    set_access_cookies, set_refresh_cookies,
)
from werkzeug.exceptions import BadRequest
<<<<<<< Updated upstream
from api.v1.views import app_views
=======

from flask_jwt_extended import jwt_required
from api.v1.views import app_views, role_required

>>>>>>> Stashed changes
from models import storage
from models.teacher import Teacher
from models.student import Student
from hashlib import sha256


@app_views.route("/teacher_login", methods=["POST"], strict_slashes=False)
def teacher_login():
    """
    Login verification of a teacher's profile.
    POST: {'email', 'password'}
    """
    if not request.is_json:
        return jsonify({'error': 'Not a JSON'}), 400

    try:
        data = request.get_json()
    except BadRequest:
        return jsonify({'error': 'Not a JSON'}), 400

    if not data:
        return jsonify({'error': 'No data'}), 422

    if 'email' not in data.keys():
        return jsonify({'error': 'Missing email'}), 400

    if 'password' not in data.keys():
        return jsonify({'error': 'Missing password'}), 400

    print("Teacher logging...")
    print("Email:", data.get("email"))

    teacher = storage.query(Teacher).filter(Teacher.email == data.
                                            get('email')).first()

    if not teacher:
        return jsonify({'error': 'UNKNOWN TEACHER'}), 404
    from datetime import datetime as date
    print(f"Teacher {teacher.last_name} {teacher.first_name} has logged in at {str(date.now())}")

    if bcrypt.checkpw(data.get('password', '').encode('utf-8'),
                      teacher.password.encode('utf-8')):
        # generate JWT token for teacher with id and user_type.
        access_token = create_access_token(identity={'id': teacher.id,
                                                     'role': 'teacher'})
        refresh_token = create_refresh_token(identity={'id': teacher.id,
                                                       'role': 'teacher'})

        resp = jsonify({'access_token': access_token,
                        'user_id': teacher.id, 'class': 'Teacher'})
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)

        # resp.set_cookie("access_token", access_token, httponly=True)
        # resp.set_cookie("refresh_token", refresh_token,
        # httponly=True,
        # secure=True,
        # samesite='Strict')
        # resp.headers['Authorization'] = f"Bearer {access_token}"
        return resp
    else:
        return jsonify({'status': 'ERROR'}), 401


@app_views.route("/student_login", methods=["POST"], strict_slashes=False)
def student_login():
    """
    Login verification of a student's profile.
    POST: {'email', 'password'}
    """
    if not request.is_json:
        return jsonify({'error': 'Not a JSON'}), 400

    try:
        data = request.get_json()
    except BadRequest:
        return jsonify({'error': 'Not a JSON'}), 400

    if not data:
        return jsonify({'error': 'No data'}), 422

    if 'email' not in data.keys():
        return jsonify({'error': 'Missing email'}), 400

    if 'password' not in data.keys():
        return jsonify({'error': 'Missing password'}), 400

    print("Student logging...")
    print("Email:", data.get("email"))
    student = storage.query(Student).filter(Student.email == data.
                                            get('email')).first()

    if not student:
        return jsonify({'error': 'UNKNOWN STUDENT'}), 404

    from datetime import datetime as date
    print(f"Student {student.last_name} {student.first_name} has logged in at {str(date.now())}, From {student.classes.alias}")
    if bcrypt.checkpw(data.get('password', '').encode('utf-8'),
                      student.password.encode('utf-8')):
        # Generate JWT token for student with additional information
        access_token = create_access_token(identity={'id': student.id,
                                                     'role': 'student'})
        refresh_token = create_refresh_token(identity={'id': student.id,
                                                       'role': 'student'})

        resp = jsonify({'access_token': access_token,
                        'user_id': student.id, 'class': 'Student'})

        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)

        return resp
    else:
        return jsonify({'status': 'ERROR'}), 401
<<<<<<< Updated upstream
=======


@app_views.route("/dev_login", methods=["POST"], strict_slashes=False)
def dev_login():
    """
    Login verification of a dev's profile.
    POST: {'email', 'password'}
    """
    if not request.is_json:
        return jsonify({'error': 'Not a JSON'}), 400

    try:
        data = request.get_json()
    except BadRequest:
        return jsonify({'error': 'Not a JSON'}), 400

    if not data:
        return jsonify({'error': 'No data'}), 422

    if 'email' not in data.keys():
        return jsonify({'error': 'Missing email'}), 400

    if 'password' not in data.keys():
        return jsonify({'error': 'Missing password'}), 400

    dev = storage.query(Dev).filter(Dev.email == data.
                                    get('email')).first()

    if not dev:
        return jsonify({'error': 'UNKNOWN Develpor'}), 404

    if bcrypt.checkpw(data.get('password', '').encode('utf-8'),
                      dev.password.encode('utf-8')):
        # Generate JWT token for dev with additional information
        access_token = create_access_token(identity={'id': dev.id,
                                                     'role': 'dev'})
        refresh_token = create_refresh_token(identity={'id': dev.id,
                                                       'role': 'dev'})

        resp = jsonify({'access_token': access_token,
                        'user_id': dev.id, 'class': 'Dev'})

        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)

        return resp
    else:
        return jsonify({'status': 'ERROR'}), 401


@app_views.route("/logout", methods=["POST"], strict_slashes=False)
@jwt_required()
@role_required(['dev', 'teacher', 'student'])  # type: ignore
def logout():
    """
    Logout the user by revoking the JWT token and clearing the access token cookie.
    """
    response = make_response(jsonify({'status': 'OK'}))

    response.set_cookie(
        'access_token',
        '',
        expires=0,  # Expire the cookie immediately
        httponly=True,  # Set HttpOnly for security
        secure=True,  # Set secure if using HTTPS
        samesite='Strict'  # Protect against CSRF
    )

    response.set_cookie(
        'refresh_token',
        '',
        expires=0,
        httponly=True,
        secure=True,
        samesite='Strict'
    )
    return response


@app_views.route("/checkjwt", methods=["GET"], strict_slashes=False)
def checkjwt():
    """
    Check if JWT access token in the browser's cookies is valid and not expired
    """
    valid = False
    try:
        verify_jwt_in_request()
        valid = True
    except Exception as e:
        print("Error while verifying jwt access token")

    return jsonify({"jwtIsValid": valid}), 200


@app_views.route("/read_logs", methods=["GET"], strict_slashes=False)
@jwt_required()
@role_required(['dev'])  # type: ignore
def read_logs():
    """
    Read the logs for the application.
    """
    import re

    A = request.args.get('A', '50')
    B = request.args.get('B', '1')
    contain = request.args.get('contain', ' ')

    # Read the log file.
    with open('gunicorn_error.log', 'r') as file:
        logs_list = file.read().split('\n')

    # Filtring:
    logs = []
    i = 0
    length = len(logs_list)
    jump_steps = 0
    regex_match = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \+\d{4}\] \[\d+\] \[\w+\]'
    for line in logs_list:
        if not line:
            continue

        # Jump File related errors.
        if jump_steps:
            jump_steps -= 1
            continue

        if 'File "' in line:
            jump_steps += 2
            continue

        if line.startswith('From decorator') or line.startswith('Error while'):
            continue

        if re.match(regex_match, line):
            continue

        # If search criterion is set
        if contain:
            # Performing an insensitive case search.
            if contain.lower() in line.lower():
                i += 1
                logs.append(f"{i}: {line}")
        else:
            i += 1
            logs.append(f"{i}: {line}")

    # Applying Pagination.
    if A and A.isdigit() and B and B.isdigit():
        logs = logs[-int(A):-int(B)]

    return jsonify(logs)
>>>>>>> Stashed changes

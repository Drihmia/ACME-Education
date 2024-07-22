#!/usr/bin/python3
"""Define the State API"""
import bcrypt
from flask import jsonify, request
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    set_access_cookies, set_refresh_cookies,
)
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views
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

    teacher = storage.query(Teacher).filter(Teacher.email == data.
                                            get('email')).first()

    if not teacher:
        return jsonify({'error': 'UNKNOWN TEACHER'}), 404

    if bcrypt.checkpw(data.get('password', '').encode('utf-8'),
                      teacher.password.encode('utf-8')):
        # generate JWT token for teacher with id and user_type.
        access_token = create_access_token(identity={'id': teacher.id,
                                                     'role': 'teacher'})
        refresh_token = create_refresh_token(identity={'id': teacher.id,
                                                       'role': 'teacher'})

        resp =  jsonify({'access_token': access_token,
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

    student = storage.query(Student).filter(Student.email == data.
                                            get('email')).first()

    if not student:
        return jsonify({'error': 'UNKNOWN STUDENT'}), 404

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

        # resp.set_cookie("access_token", access_token, httponly=True)
        # resp.set_cookie("refresh_token", refresh_token,
                        # httponly=True,
                        # secure=True,
                        # samesite='Strict')
        # resp.headers['Authorization'] = f"Bearer {access_token}"
        return resp
    else:
        return jsonify({'status': 'ERROR'}), 401

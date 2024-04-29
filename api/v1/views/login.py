#!/usr/bin/python3
"""Define the State API"""
from flask import jsonify, request
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

    # Hashing the teacher's password and compare it with stored hash
    # +of its original password.
    dec_pass = sha256(data.get("password", "wrong").encode()).hexdigest()
    if teacher.password == dec_pass:
        return jsonify({'status': 'OK'}), 200
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

    # Hashing the student's password and compare it with stored hash
    # +of its original password.
    dec_pass = sha256(data.get("password", "wrong").encode()).hexdigest()
    if student.password == dec_pass:
        return jsonify({'status': 'OK'}), 200
    else:
        return jsonify({'status': 'ERROR'}), 401

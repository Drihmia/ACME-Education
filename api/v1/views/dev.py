#!/usr/bin/python3
"""This module contains teacher'S IP"""
from flask_cors import cross_origin
from flask import jsonify, request
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views
from api.v1.views import role_required
from flask_jwt_extended import  jwt_required, verify_jwt_in_request
from models import storage
from models.dev import Dev
from models.view import (
    Recently_signed_students_by_class,
    Recently_signed_teachers
)
from models.student import Student
from models.teacher import Teacher
from uuid import uuid4

DEV_ENDPOINT = f"devs-{uuid4()}"
print("DEV_ENDPOINT:", f"/{DEV_ENDPOINT}")


@app_views.route(f"/{DEV_ENDPOINT}", methods=['POST'], strict_slashes=False)
@cross_origin()
def create_dev():
    """ Create a new dev

    POST: Create a new teacher
        MUST HAVE: email, first_name, last_name, password, confirm_password
    - example:
        data = { first_name, last_name, email, password, confirm_password }
    """
    # POST's method *******************************************************
    if request.method == 'POST':
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

        # -------------------------------------------------------
        # Check if the teacher's email not in our database.
        if storage.query(Dev).filter(Dev.email == data.
                                         get('email').strip()).first():
            return jsonify({'error': "developor exists"}), 700

        # -------------------------------------------------------
        # Check if the Teacher's email not in our database as a student or as a teacher.
        email = data.get('email').strip()
        if storage.query(Student).filter(Student.email == email).first():
            return jsonify(
                {'error':
                 f"{email} is already registered as a student"}), 409

        if storage.query(Teacher).filter(Teacher.email == data.
                                         get('email').strip()).first():
            return jsonify(
                {'error':
                 f"{email} is already registered as a teacher"}), 409

        if 'first_name' not in data.keys():
            return jsonify({'error': 'Missing first_name'}), 400

        if 'last_name' not in data.keys():
            return jsonify({'error': 'Missing last_name'}), 400

        if 'password' not in data.keys():
            return jsonify({'error': 'Missing password'}), 400

        if 'confirm_password' not in data.keys():
            if data.get('confirm_password'.strip()) != data.get(
                    'password'.strip()):
                return jsonify({'error': 'password do not match'}), 400
            else:
                del data['confirm_password']

        dev = Dev(first_name=data.get('first_name').strip(),
                          last_name=data.get('last_name').strip(),
                          email=data.get('email').strip(),
                          password=data.get('password').strip()
                  )
        try:
            dev.save()
            storage.new(dev)
            storage.save()
        except IntegrityError:
            return jsonify({'error': 'dev exists'}), 400

        dev = dev.to_dict()
        return jsonify(dev), 201


@app_views.route('/recently_signed_students_by_class', methods=['GET'],
                 strict_slashes=False)
@role_required(['dev'])
def recently_signed_students_by_class():
    """
    get the the list of recently registred students by class
    """

    if request.method == 'GET':

        # A list of all recently signed students:
        RSSBCs = storage.query(Recently_signed_students_by_class).all()
        return jsonify([RSSBC.to_dict() for RSSBC in RSSBCs]), 200


@app_views.route('/recently_signed_teachers', methods=['GET'],
                 strict_slashes=False)
@role_required(['dev'])
def recently_signed_teachers():
    """
    get the the list of recently registred teachers
    """

    if request.method == 'GET':

        # A list of all recently signed teachers:
        RSTs = storage.query(Recently_signed_teachers).all()
        return jsonify([RST.to_dict() for RST in RSTs]), 200

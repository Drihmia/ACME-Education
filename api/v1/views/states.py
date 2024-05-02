#!/usr/bin/python3
"""Define the State API"""
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/states/<id>", methods=["GET", 'PUT', 'DELETE'],
                 strict_slashes=False)
def states(id=None):
    """
    GET: Return the list of all avaiable State, if not id is provided,
    otherwise return the spesific state to that id.
    POST: Add a new state
    PUT: Update an exesting state defined by ID in URI
    """
    if request.method == 'GET':
        if not id:
            states = storage.all(State)

            states_dict = [state.to_dict() for state in states.values()]
            return jsonify(states_dict), 200

        state = storage.get(State, id)
        if not state:
            return jsonify({'error': "UNKNOWN STATE"}), 400

        return jsonify(state.to_dict()), 200

    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 422

        if 'name' not in data.keys():
            return jsonify({'error': 'Missing name'}), 400

        state = State(**data)
        try:
            storage.new(state)
            storage.save()
        except IntegrityError:
            return jsonify({'error': 'exists'}), 400

        return jsonify((state.to_dict())), 201

    if request.method == 'PUT':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 422

        state = storage.get(State, id)
        if not state:
            return jsonify({'error': "UNKNOWN STATE"}), 400

        ignore = ['id', 'created_at', 'updated_at']

        for k, v in data.items():
            if k not in ignore:
                setattr(state, k.strip(), v.strip())
        state.save()
        return jsonify(state.to_dict()), 200

    if request.method == 'DELETE':
        state = storage.get(State, id)
        if not state:
            return jsonify({'error': "UNKNOWN STATE"}), 400

        state.delete()
        storage.save()
        return jsonify({}), 200


@app_views.route("/states/<id>/cities", methods=["GET"],
                 strict_slashes=False)
def classes_cities(id=None):
    """
    GET: Return the list of all avaiable cities of that class.
    """

    state = storage.get(State, id)
    if not state:
        return jsonify({'error': "UNKNOWN STATE"}), 400

    cities = state.cities
    cities_dict = [state.to_dict() for state in cities]
    return jsonify(cities_dict), 200

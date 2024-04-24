#!/usr/bin/python3
"""Define the State API"""
from flask import abort, jsonify, request
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


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
            return jsonify(states_dict, 200)

        state = storage.get(State, id)
        if not state:
            abort(404)

        return jsonify(state.to_dict()), 200

    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if 'name' not in data.keys():
            return jsonify({'error': 'Missing name'}), 400

        state = State(**data)
        state.save()
        return jsonify((state.to_dict())), 201

    if request.method == 'PUT':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        state = storage.get(State, id)
        if not state:
            abort(404)

        ignore = ['id', 'created_at', 'updated_at']

        for k, v in data.items():
            if k not in ignore:
                setattr(state, k, v)
        state.save()
        return jsonify(state.to_dict()), 200

    if request.method == 'DELETE':
        state = storage.get(State, id)
        if not state:
            abort(404)

        state.delete()
        storage.save()
        return jsonify({}), 200


@app_views.route("/states/<id>/cities", methods=["GET", "POST"],
                 strict_slashes=False)
def classes_cities(id=None):
    """
    GET: Return the list of all avaiable cities of that class.
    """

    state = storage.get(State, id)
    if not state:
        abort(404)

    if request.method == 'GET':
        cities = state.cities
        cities_dict = [state.to_dict() for state in cities]
        return jsonify(cities_dict), 200

    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if 'name' not in data.keys():
            return jsonify({'error': 'Missing name'}), 400

        data.update({'state_id': id})
        city = City(**data)
        city.save()
        return jsonify((city.to_dict())), 201

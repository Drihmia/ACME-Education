#!/usr/bin/python3
"""Define the City API"""
from flask import abort, jsonify, request
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views
from models import storage
from models.city import City
from models.institution import Institution


@app_views.route("/cities", methods=["GET"], strict_slashes=False)
@app_views.route("/cities/<id>", methods=["GET", "PUT", "DELETE"],
                 strict_slashes=False)
def cities(id=None):
    """
    GET: Return the list of all avaiable cities, if no id is provided,
    otherwise return the spesific city to that id.
    """

    if request.method == 'GET':
        if not id:
            cities = storage.all(City)

            cities_dict = [city.to_dict() for city in cities.values()]
            return jsonify(cities_dict, 200)

        city = storage.get(City, id)
        if not city:
            abort(404)

        return jsonify(city.to_dict()), 200

    if request.method == 'PUT':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        city = storage.get(City, id)
        if not city:
            abort(404)

        ignore = ['id', 'created_at', 'updated_at']

        for k, v in data.items():
            if k not in ignore:
                setattr(city, k, v)
        city.save()
        return jsonify(city.to_dict()), 200

    if request.method == 'DELETE':
        city = storage.get(City, id)
        if not city:
            abort(404)

        city.delete()
        storage.save()
        return jsonify({}), 200


@app_views.route("/cities/<id>/institutions", methods=["GET", "POST"],
                 strict_slashes=False)
def cities_institutions(id=None):
    """
    GET: Return the list of all avaiable institutions of that city.
    POST: Create a new institution
    """

    city = storage.get(City, id)
    if not city:
        abort(404)

    if request.method == 'GET':
        institutions = city.institutions
        institutions_dict = [institution.to_dict() for institution in institutions]
        return jsonify(institutions_dict), 200

    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if 'name' not in data.keys():
            return jsonify({'error': 'Missing name'}), 400

        institution = Institution(**data)
        city.institution.append(institution)  # Many to many relationship#s association
        storage.new(institution)
        storage.new(city)  # I'm not sure if it necessary
        storage.save()
        return jsonify(institution.to_dict()), 201


@app_views.route("/cities/<id>/state", methods=["GET", "POST"],
                 strict_slashes=False)
def cities_state(id=None):
    """
    GET: Return the state of that city.
    """

    city = storage.get(City, id)
    if not city:
        abort(404)

    state = city.state
    state_dict = state.to_dict()
    return jsonify(state_dict), 200

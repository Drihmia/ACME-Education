#!/usr/bin/python3
"""Define the City API"""
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views
from models import storage
from models.city import City


@app_views.route("/cities", methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/cities/<id>", methods=["GET", "PUT", "DELETE"],
                 strict_slashes=False)
def cities(id=None):
    """
    GET: Return the list of all avaiable cities, if no id is provided,
    otherwise return the spesific city to that id.
    POST: create a new  city.
    PUT: update city with the id.
    DELETE: delete city with the id.
    """

    # GET's method.
    if request.method == 'GET':
        if not id:
            cities = storage.all(City)

            cities_dict = [city.to_dict() for city in cities.values()]
            return jsonify(cities_dict), 200

        city = storage.get(City, id)
        if not city:
            return jsonify({'error': "UNKNOWN CITY"}), 400

        return jsonify(city.to_dict()), 200

    # POST's method.
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

        if 'state_id' not in data.keys():
            return jsonify({'error': 'Missing state_id'}), 400

        city = City(**data)
        try:
            storage.new(city)
            storage.save()
        except IntegrityError:
            return jsonify({'error': 'exists'}), 400
        return jsonify((city.to_dict())), 201

    # PUT's method.
    if request.method == 'PUT':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 422

        city = storage.get(City, id)
        if not city:
            return jsonify({'error': "UNKNOWN CITY"}), 400

        ignore = ['id', 'created_at', 'updated_at']

        for k, v in data.items():
            if k not in ignore:
                setattr(city, k, v)
        city.save()
        return jsonify(city.to_dict()), 200

    # DELETE's method.
    if request.method == 'DELETE':
        city = storage.get(City, id)
        if not city:
            return jsonify({'error': "UNKNOWN CITY"}), 400

        city.delete()
        storage.save()
        return jsonify({}), 200


@app_views.route("/cities/<id>/institutions", methods=["GET"],
                 strict_slashes=False)
def cities_institutions(id=None):
    """
    GET: Return the list of all avaiable institutions of that city.
    """

    city = storage.get(City, id)
    if not city:
        return jsonify({'error': "UNKNOWN CITY"}), 400

    if request.method == 'GET':
        institutions = city.institutions
        institutions_dict = [institution.to_dict()
                             for institution in institutions]
        return jsonify(institutions_dict), 200


@app_views.route("/cities/<id>/state", methods=["GET"],
                 strict_slashes=False)
def cities_state(id=None):
    """
    GET: Return the state of that city.
    """

    city = storage.get(City, id)
    if not city:
        return jsonify({'error': "UNKNOWN CITY"}), 400

    state = city.state
    state_dict = state.to_dict()
    return jsonify(state_dict), 200

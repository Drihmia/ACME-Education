#!/usr/bin/python3
"""Define the City API"""
from flask import abort, jsonify
from api.v1.views import app_views
from models import storage
from models.city import City


@app_views.route("/cities", methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/cities/<id>", methods=["GET", "POST"],
                 strict_slashes=False)
def cities(id=None):
    """
    GET: Return the list of all avaiable cities, if no id is provided,
    otherwise return the spesific city to that id.
    """
    if not id:
        cities = storage.all(City)

        cities_dict = [city.to_dict() for city in cities.values()]
        return jsonify(cities_dict, 200)

    city = storage.get(City, id)
    if not city:
        abort(404)

    return jsonify(city.to_dict()), 200


@app_views.route("/cities/<id>/institutions", methods=["GET", "POST"],
                 strict_slashes=False)
def cities_institutions(id=None):
    """
    GET: Return the list of all avaiable institutions of that city.
    """

    city = storage.get(City, id)
    if not city:
        abort(404)

    institutions = city.institutions
    institutions_dict = [institution.to_dict() for institution in institutions]
    return jsonify(institutions_dict), 200


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

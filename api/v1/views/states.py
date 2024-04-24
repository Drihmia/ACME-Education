#!/usr/bin/python3
"""Define the State API"""
from flask import abort, jsonify
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/states/<id>", methods=["GET", "POST"],
                 strict_slashes=False)
def states(id=None):
    """
    GET: Return the list of all avaiable State, if not id is provided,
    otherwise return the spesific state to that id.
    """
    if not id:
        states = storage.all(State)

        states_dict = [state.to_dict() for state in states.values()]
        return jsonify(states_dict, 200)

    state = storage.get(State, id)
    if not state:
        abort(404)

    return jsonify(state.to_dict()), 200


@app_views.route("/states/<id>/cities", methods=["GET", "POST"],
                 strict_slashes=False)
def classes_cities(id=None):
    """
    GET: Return the list of all avaiable cities of that class.
    """

    clas = storage.get(State, id)
    if not clas:
        abort(404)

    cities = clas.cities
    cities_dict = [state.to_dict() for state in cities]
    return jsonify(cities_dict), 200

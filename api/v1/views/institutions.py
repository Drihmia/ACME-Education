#!/usr/bin/python3
"""Define the Institutions API"""
from api.v1.views import app_views
from flask import abort
import json
from models import storage


@app_views.route("/institutions", methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/institutions/<id>", methods=["GET"], strict_slashes=False)
def allInst(id=None):
    """
    GET: Return the list of avaiable institutions if there is not ID.
         Or the list with the specified ID.
    """
    from models.institution import Institution
    insts = storage.all(Institution)
    if id is None:
        data = []
        for elem in insts.values():
            temp = elem.to_dict()
            data.append(temp)
        data = json.dumps(data, indent=2, sort_keys=True) + "\n"
        return (data, 200)
    else:
        seek = "Institution." + id
        try:
            temp = insts[seek].to_dict()
            data = json.dumps(temp, indent=2, sort_keys=True) + "\n"
            return (data, 200)
        except KeyError:
            abort(404)
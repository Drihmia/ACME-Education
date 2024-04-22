#!/usr/bin/python3
"""Define the Classes API"""
from api.v1.views import app_views
from flask import abort
import json
from models import storage


@app_views.route("/classes", methods=["GET", "POST"], strict_slashes=False)
def allClas():
    """
    GET: Return the list of avaiable Classes.
    """
    from models.clas import Clas
    years = storage.all(Clas)
    data = []
    for elem in years.values():
        temp = elem.to_dict()
        data.append(temp)
    data = json.dumps(data, indent=2, sort_keys=True) + "\n"
    return (data, 200)

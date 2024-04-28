#!/usr/bin/python3
"""Define the Lessons API"""
from api.v1.views import app_views
from flask import abort
import json
from models import storage


@app_views.route("/lessons", methods=["GET"], strict_slashes=False)
@app_views.route("/lessons/<id>", methods=["GET"], strict_slashes=False)
def all(id=None):
    """
    GET: Return the list of avaiable lessons if there is not ID.
         Or the list with the specified ID.
    """
    from models.lesson import Lesson
    less = storage.all(Lesson)
    if id is None:
        data = []
        for elem in less.values():
            temp = elem.to_dict()
            data.append(temp)
        data = json.dumps(data, indent=2, sort_keys=True) + "\n"
        return (data), 200
    else:
        seek = "Lesson." + id
        try:
            temp = less[seek].to_dict()
            data = json.dumps(temp, indent=2, sort_keys=True) + "\n"
            return (data), 200
        except KeyError:
            abort(404)

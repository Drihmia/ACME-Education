#!/usr/bin/python3
"""Define the Subjects API"""
from api.v1.views import app_views
from flask import abort, jsonify
import json
from models import storage


@app_views.route("/subjects", methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/subjects/<id>", methods=["GET"], strict_slashes=False)
def allSubs(id=None):
    """
    GET: Return the list of avaiable subjects if there is not ID.
         Or the list with the specified ID.
    """
    from models.subject import Subject
    subs = storage.all(Subject)
    if id is None:
        from models.lesson import Lesson
        less = storage.all(Lesson)
        data = []
        for elem in subs.values():
            temp = elem.to_dict()
            data.append(temp)
        data = json.dumps(data, indent=2, sort_keys=True) + "\n"
        return (data, 200)
    else:
        from models.lesson import Lesson
        seek = id
        data = []
        less = storage.all(Lesson)
        for elem in less.values():
            if elem.subject_id == seek:
                temp = elem.to_dict()
                data.append(temp)
        data = json.dumps(data, indent=2, sort_keys=True) + "\n"
        return (data, 200)


@app_views.route("/<id>/subjects", methods=["GET", "POST"], strict_slashes=False)
def allIsntSubs(id=None):
    """
    GET: Lists all the subjects tought in a particular institute.
    """
    from models.institution import Institution
    if id:
        pass
    else:
        abort(404, "No ID passed")
        

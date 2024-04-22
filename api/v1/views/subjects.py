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
        for elem in less.keys():
            print(elem)
        data = []
        for elem in subs.values():
            temp = elem.to_dict()
            data.append(temp)
        data = json.dumps(data, indent=2, sort_keys=True) + "\n"
        return (data, 200)
    else:
        # seems i forget the way you taught me anout the lesson.subject_id

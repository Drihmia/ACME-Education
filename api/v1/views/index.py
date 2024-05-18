#!/usr/bin/python3
"""Index API"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Status of API"""
    goodStat = {"status": "OK"}
    return jsonify(goodStat), 200


@app_views.route("/endpoints", methods=["GET"], strict_slashes=False)
def endpoints():
    """Status of API"""
    endpoints = {
        "state": {
            "get": {"state": "/states/<state_id>", "states": "/states"},
            "post": "/states",
            "put": "/state/<state_id>",
            "delete": "/states/<state_id>"
        },
        "city": {
            "get": {"city": "/cities/<city_id>", "cities": "/cities"},
            "post": "/cities",
            "put": "/cities/<city_id>",
            "delete": "/cities/<city_id>"
        },
        "institution": {
            "get": {"institution": "/institutions/<institution_id>",
                    "institutions": "/institutions"},
            "post": "/institutions",
            "put": "/institution/<institution_id>",
            "delete": "/institution/<institution_id>"
        },
        "subjects": {
            "get": {"subject": "/subject/<subject_id>",
                    "subjects": "/subjects"}
        },
        "students": {
            "get": {"student": "/students/<student_id>",
                    "students": "/students"},
            "post": "/students",
            "put": "/students/<student_id>",
            "delete": "/students/<student_id>"
        },
        "teachers": {
            "get": {"teacher": "/teachers/<teacher_id>",
                    "teachers": "/teachers"},
            "post": "/teachers",
            "put": "/teachers/<teacher_id>",
            "delete": "/teachers/<teacher_id>"
        },
        "lessons": {
            "get": {"lesson": "/lessons/<lesson_id>",
                    "lessons": "/lessons",
                    "public lessons": "/public_lessons"}
        }
    }

    return jsonify(endpoints), 200

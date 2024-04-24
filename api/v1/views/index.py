#!/usr/bin/python3
"""Index API"""
from api.v1.views import app_views
from flask import jsonify
import json


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Status of API"""
    goodStat = {"status": "OK"}
    return jsonify(goodStat), 200

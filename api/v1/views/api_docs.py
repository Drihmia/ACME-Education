#!/usr/bin/python3
"""This module verify if user's email is valid and fonctionnal"""

from flask import render_template
from api.v1.views import app_views

@app_views.route("/documentations", strict_slashes=False)
def docs():
    """Return documentation page of our API"""
    return render_template("ACME_Education_API_Docs.html"), 200

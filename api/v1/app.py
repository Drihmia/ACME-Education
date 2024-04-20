#!/usr/bin/python3
""" Flask Application """
from flask import Flask, render_template as rentem
from api.v1.views import app_views
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)

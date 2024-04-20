#!/usr/bin/python3
""" Flask Application """
import json
from flask import Flask, render_template as rentem, make_response as res
from api.v1.views import app_views
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """Handle the 404 page"""
    notThere = {"error": "Not found"}
    return res((json.dumps(notThere, indent=2) + "\n"), 404)


app.config["SWAGGER"] = {
    "title": "AirBnB clone Restful API",
    "uiversion": 3
}

Swagger(app)


if __name__ == "__main__":
    """Starts the API"""
    app.run(threaded=True)

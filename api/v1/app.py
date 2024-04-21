#!/usr/bin/python3
""" Flask Application """
from flask import Flask, make_response
from flask_cors import CORS
from flasgger import Swagger
import json
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle the 404 page"""
    notThere = {"error": "Not found"}
    return make_response((json.dumps(notThere, indent=2) + "\n"), 404)


app.config["SWAGGER"] = {
    "title": "AirBnB clone Restful API",
    "uiversion": 3
}

Swagger(app)


if __name__ == "__main__":
    """Starts the API"""
    app.run(threaded=True, debug=True)

#!/usr/bin/python3
""" Flask Application """
from flask import Flask, make_response
from flask_cors import CORS
from flasgger import Swagger
from flask_jwt_extended import JWTManager
import json
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = '96389b9ffb48fcc169bd922991b420f9cb3e27e13a1cc6b188edc28745df08a7'


@app.teardown_appcontext
def close_db(_):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(_):
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
    with app.app_context():
        app.run(threaded=True, debug=True)

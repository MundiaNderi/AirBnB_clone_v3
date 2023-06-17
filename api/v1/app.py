#!/usr/bin/python3
""" Setting up API """

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={"*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Closes the database connection at the end of the request.

    Args:
        exception (Exception): The exception object if any
        occurred during the request.
    """
    storage.close()


@app.errorhandler(404)
def handle_404_error(error):
    """
    Handles 404 errors and returns a JSON response.

    Args:
        error (Exception): The exception object representing the 404 error.

    Returns:
        Response: A Flask JSON response indicating that the requested
        resource was not found.
    """
    response = {"error": "Not found"}
    return make_response(jsonify(response), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = 5000
    app.run(host=host, port=port)

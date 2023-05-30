#!/usr/bin/python3
"""
This script creates a Flask application instance with a blueprint
for API endpoints.

It initializes the Flask app, sets up CORS (Cross-Origin Resource Sharing),
and registers the blueprint for the API endpoints.

Usage: python3 <script_name>.py
"""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
app.url_map.strict_slashes = False
cors = CORS(app, resources={"*": {"origins": "0.0.0.0"}})


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
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST')
    port = int(os.getenv('HBNB_API_PORT'))
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = 5000
    app.run(host=host, port=port)

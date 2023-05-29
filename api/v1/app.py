#!/usr/bin/python3
"""
Script that creates a file with a Flask instance app
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Closes the database connection at the end of the request
    """
    storage.close()


# Handler for 404 errors
@app.errorhandler(404)
def handle_404_error(error):
    """
    Handler for 404 errors
    """
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response


# Run the Flask server
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST')
    port = int(os.getenv('HBNB_API_PORT'))
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = 5000
    app.run(host='0.0.0.0', port=5000)

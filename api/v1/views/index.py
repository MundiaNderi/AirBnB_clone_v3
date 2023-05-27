#!/usr/bin/python3
"""
Script that creates a route on the object app_views that returns a JSON
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

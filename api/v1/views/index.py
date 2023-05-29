#!/usr/bin/python3
"""
Script that creates a route on the API
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

classes = {"amenities": Amenity, "cities": City, "places": Place. "reviews": Review, "states": State, "users": User}


@app_views.route('/status', strict_slashes=False)
def get_status():
    """
    Returns the status of the API.
    """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """
    Returns the stats of the API
    """
    stats = {}
    for key, value in classes.items():
        stats[key] = storage.count(value)

    return jsonify(stats)

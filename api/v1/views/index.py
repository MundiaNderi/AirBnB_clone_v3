#!/usr/bin/python3
"""
Script that creates a route on the API
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    classes = {
        'amenities': 'Amenity',
        'cities': 'City',
        'places': 'Place',
        'reviews': 'Review',
        'states': 'State',
        'users': 'User'
    }

    stats = {}
    for key, value in classes.items():
        count = storage.count(value)
        stats[key] = count

    return jsonify(stats)

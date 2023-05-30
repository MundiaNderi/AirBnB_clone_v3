#!/usr/bin/python3
"""
This script creates a route on the API to retrieve
statistics about various classes.

The route '/stats' accepts a GET request and returns a
JSON response containing the counts of different classes (amenities,
cities, places, reviews, states, and users) in the storage.

Usage: This script should be imported and used within a Flask application.

Example:
    # Assuming this script is named 'stats.py' and resides in the
    'api.v1.views' module from api.v1.views.stats import get_stats

    app_views.add_url_rule('/stats', 'get_stats', get_stats, methods=['GET'])

    This code snippet adds the '/stats' route to the Flask app with
    the 'get_stats' function as the handler.

API Endpoint:
    - GET /stats: Returns statistics about different classes
    as a JSON response.

        Response example:
        {
            "amenities": 10,
            "cities": 20,
            "places": 50,
            "reviews": 30,
            "states": 5,
            "users": 100
        }
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """
    Retrieve statistics about different classes.

    Returns:
        Response: A Flask JSON response containing the counts of various
        classes in the storage.

    Raises:
        None
    """
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

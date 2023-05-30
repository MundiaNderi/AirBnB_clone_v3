#!/usr/bin/python3
"""
This script creates a route on the API to retrieve
statistics about various classes.

The route '/stats' accepts a GET request and returns a
JSON response containing the counts of different classes (amenities,
cities, places, reviews, states, and users) in the storage.

Usage: This script should be imported and used within a Flask application.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json

classes = {"amenities": Amenity, "cities": City, "places": Place, "reviews": Review, "states": State, "users": User}



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
<<<<<<< HEAD
    stats = {}
    for key, value in classes.items():
        stats[key] = storage.count(value)

=======
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
>>>>>>> 77d844361961d1427554d5d245c75019af705630
    return jsonify(stats)

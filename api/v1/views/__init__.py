#!/usr/bin/python3
"""
This script initializes the blueprint for API views.
"""

from api.v1.views.places_amenities import *
from api.v1.views.places_reviews import *
from api.v1.views.places import *
from api.v1.views.users import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.states import *
from api.v1.views.index import *
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
<<<<<<< HEAD

from api.v1.views.index import *

=======
>>>>>>> 77d844361961d1427554d5d245c75019af705630

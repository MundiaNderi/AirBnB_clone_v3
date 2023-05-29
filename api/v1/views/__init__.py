#!/usr/bin/python3
"""
This script initializes the blueprint for API views.
"""


from api.v1.views.places_reviews import *
from api.v1.views.places import *
from api.v1.views.users import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.states import *
from api.v1.views.places_amenities import *
from api.v1.views.index import *
from flask import Blueprint
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


def get(data):
    ''' Sends HTTP GET request '''
    if data['p_id']:
        parent = storage.get(data['p_str'], data['p_id'])
        if parent:
            return jsonify([p.to_dict() for p in
                           getattr(parent, data['p_child'])]), 200
        abort(404)
    if data['_id']:
        found = storage.get(data['str'], data['_id'])
        if found:
            return jsonify(found.to_dict()), 200
        abort(404)
    else:
        return jsonify([x.to_dict() for x in
                       storage.all(data['str']).values()]), 200


def delete(data):
    ''' Sends HTTP DELETE request '''
    found = storage.get(data['str'], data['_id'])
    if found:
        storage.delete(found)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


def post(data):
    ''' Sends HTTP POST request '''
    req = request.get_json()
    if req is None:
        return jsonify({'error': 'Not a JSON'}), 400
    for c in data['check']:
        if c not in req:
            return jsonify({'error': 'Missing {}'.format(c)}), 400
    if data['p_id']:
        if 'user_id' in data['check']:
            if not storage.get('User', req['user_id']):
                abort(404)
        parent = storage.get(data['p_str'], data['p_id'])
        if parent:
            req[data['p_prop']] = data['p_id']
            new = eval(data['str'])(**req)
            new.save()
            return jsonify(new.to_dict()), 201
        abort(404)
    new = eval(data['str'])(**req)
    new.save()
    return jsonify(new.to_dict()), 201


def put(data):
    ''' Sends HTTP PUT request '''
    req = request.get_json()
    if req is None:
        return jsonify({'error': 'Not a JSON'}), 400
    found = storage.get(data['str'], data['_id'])
    if found:
        for k, v in req.items():
            if k not in data['ignore']:
                setattr(found, k, v)
        storage.save()
        return jsonify(found.to_dict()), 200
    else:
        abort(404)


@cities.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if not request.is_json:
        abort(400, description='Not a JSON')

    data = request.get_json()

    # Remove ignored keys
    ignored_keys = ['id', 'state_id', 'created_at', 'updated_at']
    data = {k: v for k, v in data.items() if k not in ignored_keys}

    for key, value in data.items():
        setattr(city, key, value)

    storage.save()

    return jsonify(city.to_dict()), 200

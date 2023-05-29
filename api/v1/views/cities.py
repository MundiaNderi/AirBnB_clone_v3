#!/usr/bin/python3

'''
Create a new view for City objects that handles
all default RestFul API actions.
'''
from flask import Flask, jsonify, request, abort
from models import storage
from models.city import City
from models.state import State
from flask import Blueprint

cities = Blueprint('cities', __name__, url_prefix='/cities')


@cities.route('/', methods=['GET'])
def get_cities():
    cities = storage.all(City).values()
    cities_dict = [city.to_dict() for city in cities]
    return jsonify(cities_dict)


@cities.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    if not request.is_json:
        abort(400, description='Not a JSON')

    data = request.get_json()
    if 'name' not in data:
        abort(400, description='Missing name')

    city = City()
    city.name = data['name']
    city.state_id = state_id
    storage.new(city)
    storage.save()

    return jsonify(city.to_dict()), 201


@cities.route('/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({})

#!/usr/bin/python3
"""
Script that creates a variable app that is an instance of blueprint
"""
from flask import Blueprint
from api.v1.views import index

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

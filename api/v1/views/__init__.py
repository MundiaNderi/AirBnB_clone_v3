#!/usr/bin/python3
"""
<<<<<<< HEAD
Script that creates a variable app that is an instance of blueprint
"""
from flask import Blueprint
from api.v1.views import index

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
=======
Module that updates init
"""
from api.v1.views.states import *
>>>>>>> f66b48369dafe2d4b47d9182bc361305f18bf423

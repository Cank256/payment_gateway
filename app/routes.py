# app/routes.py

from collections import OrderedDict
import json
from flask import make_response
from flask_restful import Api
from app.common.handle_requests import HandleRequests
from app.common.utils import IndexRoute


def create_routes(app):

    api = HandleRequests(app, prefix='/api')

    # Add your routes here
    api.add_resource(IndexRoute, '/', '')

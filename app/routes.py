# app/routes.py

from collections import OrderedDict
import json
from flask import make_response
from flask_restful import Api, Resource
# Import other resources as needed

class Index(Resource):
    def get(self):
        response = OrderedDict([
            ('status', 'success'),
            ('code', 200),
            ('message', 'Welcome to the Gateway'),
            ('data', {})
        ])

        response_json = json.dumps(response)
        return make_response(response_json, 200, {'Content-Type': 'application/json'})

def create_routes(app):
    api = Api(app, prefix='/api')

    # Add your routes here
    api.add_resource(Index, '/')

import os
from app.common.constants import STATUS_CODES
from collections import OrderedDict
from flask import make_response
from flask_restful import Resource
import json


class IndexRoute(Resource):
    """
    A Flask-RESTful resource representing the index route of the API.

    Methods:
        get: Returns a predefined welcome message as a JSON response.
    """
    def get(self):
        return Responses.create(200, {'message': 'Welcome to the Gateway'})

class Responses(Resource):
    """
    A helper class for creating JSON responses in a consistent format.

    Methods:
        create: Creates a JSON response with a given status code and data.
        generate_message: Generates a message string based on the status code.
    """
    def create(code, data=None, extra_info=''):
        """
        Creates a JSON response.

        Args:
            code (int): The HTTP status code for the response.
            data (dict, optional): The data to be included in the response. Defaults to None.
            extra_info (str, optional): Additional information to append to the response message. Defaults to ''.

        Returns:
            Flask response object: A response object with JSON data and the specified status code.
        """
        if not isinstance(code, int):
            raise ValueError(f'Expected an integer for the response code, got {type(code)}')

        message = Responses.generate_message(code, extra_info)
        success = code < 300
        response = OrderedDict([
                ('success', success),
                ('code', code),
                ('message', message),
                ('data', data)
            ])
        response_json = json.dumps(response)
        return make_response(response_json, code, {'Content-Type': 'application/json'})

    def generate_message(code, extra_info=''):
        """
        Generates a message based on the status code.

        Args:
            code (int): The HTTP status code.
            extra_info (str): Additional information to be appended to the message.

        Returns:
            str: A message corresponding to the provided status code.
        """
        messages = {
            STATUS_CODES.OK: "Request completed.",
            STATUS_CODES.SERVICE_UNAVAILABLE: "Service is unavailable.",
            STATUS_CODES.BAD_REQUEST: "Invalid request.",
            STATUS_CODES.METHOD_NOT_ALLOWED: "Method not allowed.",
            STATUS_CODES.HTTP_GATEWAY_TIMEOUT: "Gateway Timedout.",
            STATUS_CODES.INTERNAL_SERVER_ERROR: "Encountered an unexpected condition.",
            STATUS_CODES.UNPROCESSABLE_ENTITY: "Request Failed.",
            STATUS_CODES.NOT_FOUND: "Resource not found."
        }

        # Get the message based on the code, default to a generic message if code is not recognized
        message = messages.get(code, 'Unknown status code.')
        
        # Append extra information if provided
        if extra_info:
            message += f" {extra_info}"

        return message.strip()

def load_service_providers():
        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        PROVIDERS_JSON_PATH = os.path.join(BASE_DIR, '../../.providers.json')
        with open(PROVIDERS_JSON_PATH, 'r') as file:
            data = json.load(file)
        return data['service_providers']
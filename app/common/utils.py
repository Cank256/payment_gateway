from collections import OrderedDict
import json
from flask import make_response
from flask_restful import Resource
from app.common.constants import STATUS_CODES


class IndexRoute(Resource):
    def get(self):
        return Response.create(200, {'message': 'Welcome to the Gateway'})

class Response(Resource):
    def create(code, data=None, extra_info=''):
        if not isinstance(code, int):
            raise ValueError(f"Expected an integer for 'code', got {type(code)}")

        message = Response.generate_message(code, extra_info)
        success = code < 300
        response = OrderedDict([
                ('success', success),
                ('code', code),
                ('message', message),
                ('data', data)
            ])
        response_json = json.dumps(response)
        return make_response(response_json, 200, {'Content-Type': 'application/json'})

    def generate_message(code, extra_info=''):
        messages = {
            STATUS_CODES.OK: "Request completed.",
            STATUS_CODES.SERVICE_UNAVAILABLE: "Service is unavailable.",
            STATUS_CODES.BAD_REQUEST: "Invalid request.",
            STATUS_CODES.HTTP_GATEWAY_TIMEOUT: "Gateway Timedout.",
            STATUS_CODES.INTERNAL_SERVER_ERROR: "Encountered an unexpected condition.",
            STATUS_CODES.UNPROCESSABLE_ENTITY: "Request Failed.",
            STATUS_CODES.NOT_FOUND: "Resource not found."
        }

        # Get the message based on the code, default to a generic message if code is not recognized
        message = messages.get(code, "Unknown status code.")
        
        # Append extra information if provided
        if extra_info:
            message += f" {extra_info}"

        return message.strip()
# app/common/handle_requests.py

import json
from flask import g, request
from flask_restful import Api as OriginalApi
from app.common.constants import STATUS_CODES
from app.common.utils import Responses, generate_gateway_ref
from werkzeug.exceptions import MethodNotAllowed


"""
The class handles the processing of request data and errors
"""
class HandleRequests(OriginalApi):
    def handle_error(self, e):
        # Check if it's a 405 Method Not Allowed error
        if isinstance(e, MethodNotAllowed):
            """*405* `Method Not Allowed`

            Raise if the server used a method the resource does not handle.  For
            example `POST` if the resource is GET only.
            """
            return Responses.create(
                STATUS_CODES.METHOD_NOT_ALLOWED,
                {'message': f'{request.method} method is not allowed for this path.'}
            )

        # For other errors, use the default Flask-RESTful error handling
        return super(HandleRequests, self).handle_error(e)

    def handle_body():
        excluded_paths = [
            '/api/',
            '/api/providers',
            'api/webhook',
        ]

        # Check if the request path is in the excluded paths
        if request.path in excluded_paths or request.path.startswith('/api/transactions'):
            return  # Skip the middleware

        try:
            json_data = request.get_json() or {} 
        except (TypeError, json.JSONDecodeError):
            json_data = {}

        # Extract details from the request
        details = {
            'amount': json_data.get('amount'),
            'application': json_data.get('application'),
            'client_email': json_data.get('client_email'),
            'client_name': json_data.get('client_name'),
            'currency': json_data.get('currency'),
            'description': json_data.get('description'),
            'msisdn': json_data.get('msisdn'),
            'py_ref': json_data.get('py_ref'),
            'redirect_url': json_data.get('redirect_url'),
            'reference': json_data.get('reference'),
            'status': json_data.get('status'),
            'transaction_id': json_data.get('transaction_id'),
            'visa_details': json_data.get('visa_details'),
        }

        # Include gateway_ref in the details
        details['gateway_ref'] = generate_gateway_ref()

        # Clean up details dictionary to remove null or undefined parameters
        details = {k: v for k, v in details.items() if v is not None}

        # Attach details to the request object
        request.details = details

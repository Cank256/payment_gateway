from flask_restful import Api as OriginalApi
from flask import request
from werkzeug.exceptions import MethodNotAllowed, NotFound
from app.common.constants import STATUS_CODES
from app.common.utils import Responses

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

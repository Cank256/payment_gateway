from flask_restful import Api as OriginalApi
from flask import request
from werkzeug.exceptions import MethodNotAllowed, NotFound
from app.common.constants import STATUS_CODES
from app.common.utils import Response

class HandleRequests(OriginalApi):
    def handle_error(self, e):
        # Check if it's a 404 Not Found error
        if isinstance(e, NotFound):
            """*404* `Not Found`

            Raise if a resource does not exist and never existed.
            """
            return Response.create(
                STATUS_CODES.NOT_FOUND,
                {'message': 'The requested resource can\'t be found.'}
            )
        
        # Check if it's a 405 Method Not Allowed error
        if isinstance(e, MethodNotAllowed):
            """*405* `Method Not Allowed`

            Raise if the server used a method the resource does not handle.  For
            example `POST` if the resource is GET only.
            """
            return Response.create(
                STATUS_CODES.METHOD_NOT_ALLOWED,
                {'message': f'{request.method} method is not allowed for this path.'}
            )

        # For other errors, use the default Flask-RESTful error handling
        return super(HandleRequests, self).handle_error(e)

# app/routes.py

from app.common.handle_requests import HandleRequests
from app.common.utils import IndexRoute
from app.services.services import CollectPayment


"""
Function to create and register routes with the Flask application
"""
def create_routes(app):
    # Initialize the custom API handler with the Flask app  
    api = HandleRequests(app, prefix='/api')

    app.before_request(HandleRequests.handle_body)

    # Add your routes here
    api.add_resource(IndexRoute, '/', '')
    api.add_resource(CollectPayment, '/collect')

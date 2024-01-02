# app/__init__.py

from flask import Flask
from app import routes
# other imports as needed

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Adjust as needed

    routes.create_routes(app)  # Register the routes

    return app

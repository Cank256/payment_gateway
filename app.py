# app.py

import pymongo
from app.common.constants import STATUS_CODES
from app.common.utils import Responses
from app.routes import create_routes
import config
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
import os


# Initialize the Flask app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Load configurations based on the current environment
env = os.environ.get('APP_ENV', 'development')
if env == 'production':
    app.config.from_object(config.ProductionConfig)
elif env == 'testing':
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

# Initialize Flask-RESTful API
api = Api(app)

# Register routes with the application
create_routes(app)

# Add 404 error (works only from here)
@app.errorhandler(404)
def page_not_found(e):
    return Responses.create(
        STATUS_CODES.NOT_FOUND,
        {'message': 'The requested resource can\'t be found.'}
    )

mongo = pymongo(app)

# Run the application
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])

import os
import config
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from app.routes import create_routes


# Initialize the Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Load configurations
env = os.environ.get('APP_ENV', 'development')
if env == 'production':
    app.config.from_object(config.ProductionConfig)
elif env == 'testing':
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

# Initialize API
api = Api(app)

# Register the routes
create_routes(app)

# Run the application
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])

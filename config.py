import os


class Config:
    DEBUG = False  # Turn off in production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WEBHOOK_SECRET_KEY = os.environ.get('WEBHOOK_SECRET_KEY')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/gateway_flask')
    PORT = int(os.environ.get('APP_PORT', 8080))

# Additional configuration classes for different environments
class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific configurations

class ProductionConfig(Config):
    DEBUG = False
    # Production-specific configurations

class TestingConfig(Config):
    TESTING = True
    # Testing-specific configurations

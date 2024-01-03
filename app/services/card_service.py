# app/services/card_service.py

from app.common.utils import Responses


def collect(config, data):
    # Implement the collection logic for Flutterwave Card Charge
    # Use 'config' for provider-specific settings and 'data' for request data
    return Responses.create(200, {'message': 'This is Card'})

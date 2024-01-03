from flask import request
from flask_restful import Resource
import importlib
from app.common.utils import Responses, load_service_providers


class CollectPayment(Resource):
    def post(self):
        provider_code = request.headers.get('provider')

        if not provider_code:
            # Handle missing provider header
            return Responses.create(400, {'error': 'The \'provider\' header is not provided.'})

        service_providers = load_service_providers()

        # Split the provider_code by underscores, capitalize each part, and then concatenate
        provider_class_name = ''.join(word.capitalize() for word in provider_code.split('_'))

        if provider_code in service_providers:
            provider_config = service_providers[provider_code]

            try:
                # Dynamically import the module based on provider_code
                service_module = importlib.import_module(f'app.services.{provider_code}_service')
            except ImportError:
                # Handle missing service module
                return Responses.create(400, {'error': 'Service provider not supported'})

            # Dynamically get the class from the module
            try:
                provider_class = getattr(service_module, provider_class_name)
            except AttributeError:
                # Handle missing class in the module
                return Responses.create(400,  {'error': f'Class {provider_class_name} not found in the module'})

            # Call the collect method of the class
            return provider_class.collect(provider_config, request.details)
        else:
            return Responses.create(400, {'error': 'Unknown provider'})


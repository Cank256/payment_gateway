# test_api_route.py

import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()  # Configure your app for testing
    with app.test_client() as client:
        yield client

def test_api_index_route(client):
    response = client.get('/api/')
    assert response.status_code == 200
    assert 'Welcome to the Gateway' in response.get_data(as_text=True)

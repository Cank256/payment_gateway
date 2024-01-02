import unittest
from app import create_app  # Adjust the import according to your project structure

class ApiRouteTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = create_app()  # Pass in any necessary configuration
        self.client = self.app.test_client()

    def test_api_route(self):
        # Test the /api/ route
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the Gateway', str(response.data))

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()

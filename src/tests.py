import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Say something:', response.data)

    def test_form_submission(self):
        response = self.client.post('/', data={'input_text': 'Input test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You\'ve said: Input test... How smart you are! :-)', response.data)

if __name__ == '__main__':
    unittest.main()
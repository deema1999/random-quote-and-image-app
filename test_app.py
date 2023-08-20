import unittest
from app import app


class RandomQuoteAndImageAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test the home page to ensure it is accessible and contains the expected content."""

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Random Quote and Image App", response.data)

    def test_get_random_quote_text(self):
        """Test getting a random quote via the web interface."""

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"quote", response.data)

    def test_get_random_image_url(self):
        """Test getting a random image via the web interface."""

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"image", response.data)

    def test_get_random_quote_with_category(self):
        """Test getting a random quote with a specified category via the web interface."""

        response = self.app.get('/?category=12345')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"quote", response.data)

    def test_get_random_image_with_grayscale(self):
        """Test getting a random image in grayscale via the web interface."""

        response = self.app.get('/?grayscale=on')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"image", response.data)


if __name__ == '__main__':
    unittest.main()

import requests
import random

FORISMATIC_API_URL = "http://api.forismatic.com/api/1.0/"
PICSUM_API_URL = "https://picsum.photos/200/300"


def get_random_quote_text(category=None):
    """Get a random quote from the Forismatic API.

    Args:
        category (int, optional): Specify a category for the quote. Defaults to None.

    Returns:
        str: A random quote.
    """
    try:
        params = {"method": "getQuote", "format": "json", "lang": "en"}
        if category:
            params["key"] = category
        else:
            # Added a random key
            params["key"] = random.randint(1, 999999)

        response = requests.post(FORISMATIC_API_URL, params=params)
        data = response.json()
        return data["quoteText"]
    except (requests.RequestException, KeyError) as e:
        return "An error occurred while fetching the quote."


def get_random_image_url(grayscale=False):
    """Get a random picture from the Picsum Photos API.

    Args:
        grayscale (bool, optional): Convert the picture to grayscale. Defaults to False.

    Returns:
        str: URL of the random picture.
    """
    try:
        if grayscale:
            return PICSUM_API_URL + "?grayscale"
        else:
            return PICSUM_API_URL
    except requests.RequestException as e:
        return "An error occurred while fetching the image."

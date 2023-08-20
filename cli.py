import requests
import argparse
from PIL import Image
from src import *


def show_image_in_cli(image_url):
    """Display an image in the command line.

    Args:
        image_url (str): URL of the image to display.
    """
    response = requests.get(image_url)
    try:
        with Image.open(response.raw) as img:
            img.show()
    except requests.RequestException as e:
        return "An error occurred while fetching the image."


def main():
    """ Main function to handle command line arguments and execute the desired actions."""

    parser = argparse.ArgumentParser(
        description="Get a random quote and image.")
    parser.add_argument("--quote", action="store_true",
                        help="Get a random quote")
    parser.add_argument("--image", action="store_true",
                        help="Get a random image")
    parser.add_argument("--grayscale", action="store_true",
                        help="Get a random grayscale image")
    parser.add_argument("--category", type=str,
                        help="Specify a category for the quote")

    args = parser.parse_args()

    if not any(vars(args).values()):
        quote = get_random_quote_text()
        image_url = get_random_image_url()
        print("Random Quote Text:")
        print(quote)
        print("Random Image URL:")
        print(image_url)
        show_image_in_cli(image_url)
    else:
        if args.quote:
            if args.category:
                category = args.category
            else:
                category = None
            quote = get_random_quote_text(category)
            print("Random Quote Text:")
            print(quote)
        if args.image:
            image_url = get_random_image_url(args.grayscale)
            print("Random Picture URL:")
            print(image_url)
            show_image_in_cli(image_url)


if __name__ == "__main__":
    main()

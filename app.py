from flask import Flask, render_template, request
from src import *

app = Flask(__name__)

@app.route("/")
def index():
    """Main route to handle requests for random quotes and images."""

    quote = get_random_quote_text()
    image_url = get_random_image_url()
     
    if "category" in request.args:
        category = request.args.get("category")
        quote = get_random_quote_text(category=category)

    if "grayscale" in request.args:
        image_url = get_random_image_url(grayscale=True)
    else:
        image_url = get_random_image_url()

    return render_template("index.html", quote=quote, image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)

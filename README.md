
# Random Quote and Image App

This is a Flask web application that allows you to get random quotes and images. You can also specify options like getting an image in grayscale or choose a specific category for the quote.

## Installation

To run this Flask app, it's recommended to set up a virtual environment to manage dependencies. Follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/deema1999/random-quote-and-image-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd random-quote-and-image-app
    ```

3. Create a virtual environment (assuming you have Python 3 installed):

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

5. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:5000` to access the web interface.

3. You can click the "Get Random Quote" and "Get Random Image" buttons to get random quotes and images. You can also specify options like grayscale and category for the quote.

4. To stop the Flask app, press `Ctrl + C` in your terminal.

## Unit Testing

You can run unit tests to ensure the functionality of the app:

```bash
python test_app.py
```

# Random Quote and Image CLI

This is a Python command-line tool that allows you to get a random quote and a random image. You can also specify options like getting an image in grayscale or choose a specific category for the quote.

## Usage

To use this tool, follow the instructions below:

### Command-Line Options

- `--quote`: Get a random quote.
- `--image`: Get a random image.
- `--grayscale`: Convert the image to grayscale (only when used with `--image`).
- `--category`: Specify a category for the quote (only when used with `--quote`).
- `--help`: Get commands list with its description.


### Examples

To get a random quote:
```bash
python cli.py --quote
```

To get a random quote from a specific category (add numeric value):
```bash
python cli.py --quote --category=123456
```

To get a random image:
```bash
python cli.py --image
```

To get a random image in grayscale:
```bash
python cli.py --image --grayscale
```






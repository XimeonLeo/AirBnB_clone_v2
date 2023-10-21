#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display Hello HBNB! """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """ display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """ Display “Python ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
    """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Display “n is a number” only if n is an integer
    """
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

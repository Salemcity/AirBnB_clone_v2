#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index_home():
    """returns HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def index_c(text):
    """returns C <text>!"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index_python(text='is cool'):
    """returns Python <text>!"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

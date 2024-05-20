#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """print C followed by the value of text"""
    text = text.replace("_", " ")
    return (f"C {text}")

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Print Python followed by the value of text"""
    return ("Python {}".format(text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def num(m):
    """print "n is a number" only if its integer"""
    if isinstance(n, int):
        return ("{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

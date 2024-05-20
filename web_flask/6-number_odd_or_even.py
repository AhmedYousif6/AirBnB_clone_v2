#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

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
def num(n):
    """print "n is a number" only if its integer"""
    if isinstance(n, int):
        return ("{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n=None):
    """display html page only if n is an integer"""
    if isinstance(n, int):
        return (render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n=None):
    """display html page only if n an integer"""
    if isinstance(n, int):
        if n % 2:
            even_odd = "odd"
        else:
            even_odd = "even"
        return (render_template("6-number_odd_or_even.html", n=n, even_odd=even_odd)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

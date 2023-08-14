#!/usr/bin/python3
"""
Add replace underscores with spaces.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays 'C' followed by the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Displays 'Python' followed by the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """Displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    if isinstance(n, int):
        parity = "odd" if n % 2 else "even"
        return render_template(
            '6-number_odd_or_even.html', number=n, parity=parity)
    else:
        return "Not Found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

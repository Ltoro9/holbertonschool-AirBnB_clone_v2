#!/usr/bin/python3
"""
    script that starts a Flask web application
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
        print Hello HBNB in flask web app
    """
    return (f"Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def no_hello():
    """
        print HBNB in flask web app
    """
    return (f"HBNB")


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """
        display “C ” followed by the value of the text variable
    """
    return f'C {text.replace("_", " ")}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_not_fun(text="is_cool"):
    """
        display “Python ”, followed by the value of the text variable
        replace underscore _ symbols with a space
    """
    return f'Python {text.replace("_", " ")}'


@app.route("/number/<int:n>", strict_slashes=False)
def i_love_numbers(n):
    """
        display “n is a number” only if n is an integer
    """
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def not_love_numbers_template(n):
    """
        display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def who_am_i(n):
    """
        print n is even|odd
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

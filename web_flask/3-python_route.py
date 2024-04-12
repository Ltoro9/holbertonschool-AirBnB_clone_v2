#!/usr/bin/python3
"""
    script that starts a Flask web application
"""


from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

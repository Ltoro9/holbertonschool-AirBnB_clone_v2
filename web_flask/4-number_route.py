from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return(f"Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def no_hello():
    return(f"HBNB")

@app.route("/c/", strict_slashes=False)
@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text="is_cool"):
    return f'C {text.replace("_", " ")}'

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_not_fun(text="is_cool"):
    return f'Python {text.replace("_", " ")}'

@app.route("/number/<int:n>", strict_slashes=False)
def i_love_numbers(n):
    return f'{n} is a number'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
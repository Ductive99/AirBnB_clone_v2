#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slahes = False


@app.route("/")
def hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    return "C {}".format(text.replace('_', ' '))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text=None):
    if text is None:
        return "Python is cool"
    else:
        return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>")
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_parity(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

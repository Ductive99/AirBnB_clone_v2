#!/usr/bin/python3
"""
Script that starts a Flask web application
web app is listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


#!/usr/bin/python3
"""
Flask Web Application
Integrated with the Storage engines
Listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slahes = False


@app.route("/states_list")
def states():
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    ls = {'states': states}
    return render_template("7-states_list.html", **ls)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

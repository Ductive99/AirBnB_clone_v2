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


@app.route("/cities_by_states")
def cities_states():
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    ls = {'states': all_states}
    return render_template('8-cities_by_states.html', **ls)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.teardown_appcontext
def close_db(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def list_cities_by_state(id):
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('cities.html', state=state, cities=cities)
    else:
        return render_template('not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

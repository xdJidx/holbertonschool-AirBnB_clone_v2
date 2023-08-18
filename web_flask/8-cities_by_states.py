#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import environ

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('cities_by_states.html', states=sorted_states)

if __name__ == '__main__':
    host = environ.get('FLASK_HOST', '0.0.0.0')
    port = int(environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port)

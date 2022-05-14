#!/usr/bin/python3
'''
Flask app for the web static airbnb
'''

from flask import Flask, escape, request, render_template
from models import storage
from models.state import State
import os
app = Flask(__name__)
data = storage.all()


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''Display all state in HTML page'''
    data = storage.all(State)
    data_state = []
    for key, value in data.items():
        data_state.append(value)
    return render_template('8-cities_by_states.html', data_state=data_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

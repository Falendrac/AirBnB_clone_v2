#!/usr/bin/python3
'''
Flask app for the web static airbnb
'''

from flask import Flask, escape, request, render_template
from models import storage
from models.state import State
app = Flask(__name__)
data = storage.all()


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    '''Display all state in HTML page'''
    data = storage.all(State)
    data_state = []
    for key, value in data.items():
        data_state.append(value)
    return render_template('7-states_list.html', data=data_state)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    '''Display one state by id'''
    data = storage.all(State)
    data_state = []
    for key, value in data.items():
        if value.id == id:
            data_state.append(value)
    return render_template('9-states.html', data=data_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

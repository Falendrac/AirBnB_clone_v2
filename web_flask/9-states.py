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
    data_state = {}
    for key in data.keys():
        if isinstance(data[key], State):
            data_state[key] = data[key]
    return render_template('9-states.html', data=data_state)

@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    '''Display one state by id'''
    data_state = {}
    for key in data.keys():
        if data[key].id == id:
            data_state[key] = data[key]
    return render_template('9-states.html', data=data_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

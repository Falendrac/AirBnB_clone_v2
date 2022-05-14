#!/usr/bin/python3
'''
Flask app for the web static airbnb
'''

from flask import Flask, escape, request, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    '''Close the current sqlalchemy session'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Display all state in HTML page'''
    data = storage.all(State)
    data_state = []
    for key, value in data.items():
        data_state.append(value)
    return render_template('7-states_list.html', data=data_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

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


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Display all state in HTML page'''
    data_state = {}
    for key in data.keys():
        if isinstance(data[key], State):
            data_state[key] = data[key]
    return render_template('7-states_list.html', data=data_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

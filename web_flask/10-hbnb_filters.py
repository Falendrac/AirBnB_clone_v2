#!/usr/bin/python3
'''
Flask app for the web static airbnb
'''

from flask import Flask, escape, request, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)
data = storage.all()


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb():
    '''Display hbnb'''
    data_state = {}
    for key in data.keys():
        if isinstance(data[key], State):
            data_state[key] = data[key]
    data_amenities = {}
    for key in data.keys():
        if isinstance(data[key], Amenity):
            data_amenities[key] = data[key]
    return render_template('10-hbnb_filters.html', data_state=data_state, data_amenities=data_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

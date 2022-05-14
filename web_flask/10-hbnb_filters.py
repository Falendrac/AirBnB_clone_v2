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
    data = storage.all(State)
    data_state = []
    for key, value in data.items():
        data_state.append(value)
    data = storage.all(Amenity)
    data_amenities = []
    for key, value in data.items():
        data_amenities.append(value)
    return render_template('10-hbnb_filters.html', data_state=data_state, data_amenities=data_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

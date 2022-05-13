#!/usr/bin/python3
'''
Hello route of flask framework
'''

from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Display Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''Display C and a text'''
    return 'C %s'.format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

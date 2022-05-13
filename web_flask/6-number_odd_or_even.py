#!/usr/bin/python3
'''
Hello route of flask framework
'''

from flask import Flask, escape, request, render_template
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
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def python(text='is cool'):
    '''Display Python and a text'''
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    '''Display if the variable is a number'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Display the html'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''Display the html'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

#!/usr/bin/python3
"""
Simple Flask web application.
The script starts a Flask web application:
    Listening on 0.0.0.0, port 5000
    Routes:
        /: display 'Hello HBNB!'
        /hbnb: display 'HBNB'
        /c/<text>: display 'C ' followed by the value of the text variable
          (replace underscore _ symbols with a space )
        /python/<text>: display 'Python ', followed by the value of the text
          variable (replace underscore _ symbols with a space )
          The default value of text is 'is cool'

"""


from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """
    Route that displays "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route that displays "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "C " + escape(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_route(text="is cool"):
    """
    Route that displays "Python ", followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    If no text is provided, use the default value "is cool".
    """
    return "Python " + escape(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

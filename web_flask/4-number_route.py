#!/usr/bin/python3
"""
Module 4-number_route
    ip 0.0.0.0, port 5000
    Routes:
    '/': display “Hello HBNB!”
    '/hbnb': display “HBNB”
    '/c/<text>': display “C ”
        followed by the value of
        the text variable
        (replace underscore _ symbols with a space )
    '/python/<text>': display “Python ”
        followed by the value of
        the text variable
        (replace underscore _ symbols with a space )
             The default value of text is “is cool”
    '/number/<n>': display "n is a number" only if 'n' is an integer
    use option strict_slashes=False in your route definition
"""


from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """display custom text given
       first route statement ensures it works for:
          curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
          curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """display text only if int given"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

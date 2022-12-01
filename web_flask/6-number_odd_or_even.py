#!/usr/bin/python3
"""
Module 5-number_template
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
    '/number_template/<n>': display a HTML page only if 'n' is an integer:
        H1 tag: "Number: 'n'" inside the tag BODY
    '/number_odd_or_even/<n>': display a HTML page only if 'n' is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
    use option strict_slashes=False in your route definition
"""


from flask import Flask, render_template
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """N as int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """N as int"""
    eo = 'odd'
    if (n % 2 == 0):
        eo = 'even'
    return render_template('6-number_odd_or_even.html', n=n, eo=eo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

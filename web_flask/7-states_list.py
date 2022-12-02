#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list')
def state_list():
    """
    display a HTML page
    H1: "States"
    UL: list of all State objects
       LI: description of one State:
           <state.id>: <B> <state.name> </B>
    """
    state_objs = storage.all("State")
    return render_template("7-states_list.html", states=state_objs)


@app.teardown_appcontext
def teardown(self):
    """
    Tears down the db connection
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

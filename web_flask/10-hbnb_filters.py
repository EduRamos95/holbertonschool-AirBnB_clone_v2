#!/usr/bin/python3
"""
Module: 11-hbnb Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters
"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def filters():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states,amenities=amenities )


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

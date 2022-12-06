#!/usr/bin/python3
"""
Module: 12-hbnb Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb
"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def places():
    """Displays an HTML page with a list of all Places.
    States are sorted by name.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    # users = storage.all("User")
    return render_template("100-hbnb.html",
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

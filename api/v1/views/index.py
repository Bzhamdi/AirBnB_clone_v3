#!/usr/bin/python3
"""task 8"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


app = Flask(__name__)


classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status():
    """status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """status"""
    d = {}
    for cls in classes:
        print(cls)
        a = storage.count(cls)
        d[cls] = a
    return jsonify(d)


if __name__ == "__main__":
    pass

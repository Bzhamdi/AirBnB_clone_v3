#!/usr/bin/python3
"""task 8"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.user import User


app = Flask(__name__)


classes = {
    "amenities": Amenity,
    "cities": City,
    "places": Place,
    "reviews": Review,
    "states": State,
    "users": User
}


@app_views.route('/status', strict_slashes=False)
def status():
    """status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """status"""
    d = {}
    for cls, value in classes.items():
        a = storage.count(value)
        d[cls] = a
    return jsonify(d)


if __name__ == "__main__":
    pass

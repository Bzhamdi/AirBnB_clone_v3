#!/usr/bin/python3
"""task 8"""
from flask import Flask, jsonify
from api.v1.views import app_views


app = Flask(__name__)


@app_views.route('/status', strict_slashes=False)
def status():
    """status"""
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    pass

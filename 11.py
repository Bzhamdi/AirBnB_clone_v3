#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ DELETE /api/v1/places/<place_id>
    """
    place_id = "nop"
    r = requests.delete("http://0.0.0.0:5000/api/v1/places/{}".format(place_id))
    print(r.status_code)
    
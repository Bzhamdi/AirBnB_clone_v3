#!/usr/bin/python3
"""states.py"""

from api.v1.views import app_views
from flask import Flask, abort, jsonify, make_response, request
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.register_blueprint(app_views)


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def retrieveallbystate(state_id):
    """retrieveall by state"""
    li = []
    f = storage.get(State, state_id)
    if f:
        j = f.cities
        for i in j:
            ok = storage.get(City, i.id)
            li.append(ok.to_dict())
        return jsonify(li)
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def retrieveall(city_id):
    """retrieveall"""
    f = storage.get(City, city_id)
    if f:
        return jsonify(f.to_dict())
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def deletebyid(city_id):
    """deletebyid"""
    f = storage.get(City, city_id)
    if f:
        storage.delete(f)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def postcitybyid(state_id):
    """postcitybyid"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    f = storage.get(State, state_id)
    if f is None:
        abort(404)
    if "name" not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    else:
        req_data = request.get_json()
        req_data['state_id'] = state_id
        ct = City(**req_data)
        ct.save()
        return make_response(jsonify(ct.to_dict()), 201)


@app_views.route('cities/<city_id>', methods=['PUT'])
def putcity(city_id):
    """update ct"""

    ct = storage.get(City, city_id)
    if ct is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    req_data = request.get_json()
    ct.name = req_data['name']
    ct.save()
    return jsonify(ct.to_dict())


if __name__ == "__main__":
    pass

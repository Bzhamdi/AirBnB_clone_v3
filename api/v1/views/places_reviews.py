#!/usr/bin/python3
"""placesrev.py"""

from api.v1.views import app_views
from flask import Flask, abort, jsonify, make_response, request
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


app = Flask(__name__)


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def retrAieveal_lbystate(place_id):
    """retrieveall by state"""
    li = []
    f = storage.get(Place, place_id)
    if f:
        j = f.reviews
        for i in j:
            ok = storage.get(Review, i.id)
            li.append(ok.to_dict())
        return jsonify(li)
    else:
        abort(404)


@app_views.route('reviews/<review_id>', methods=['GET'], strict_slashes=False)
def retrAi_eveall(review_id):
    """retrieveall"""
    f = storage.get(Review, review_id)
    if f:
        return jsonify(f.to_dict())
    else:
        abort(404)


@app_views.route('reviews/<review_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def deleAte_byid(review_id):
    """deletebyid"""
    f = storage.get(Review, review_id)
    if f:
        storage.delete(f)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def postcia_tybyid(place_id):
    """postcitybyid"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    f = storage.get(Place, place_id)
    if f is None:
        abort(404)
    if "text" not in request.get_json():
        return make_response(jsonify({'error': 'Missing text'}), 400)
    if "user_id" not in request.get_json():
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    user = storage.get("User", request.get_json()['user_id'])
    if user is None:
        abort(404)
    else:
        req_data = request.get_json()
        req_data['place_id'] = place_id
        ct = Review(**req_data)
        ct.save()
        return make_response(jsonify(ct.to_dict()), 201)


@app_views.route('reviews/<review_id>', methods=['PUT'])
def put_ci_ty(review_id):
    """update ct"""
    check = ['id', 'user_id', 'city_id', 'created_at',
             'updated_at']
    ct = storage.get(Review, review_id)
    if ct is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    req_data = request.get_json()
    for i, j in request.get_json().items():
        if i not in check:
            setattr(ct, i, j)
    ct.save()
    return jsonify(ct.to_dict())


if __name__ == "__main__":
    pass

#!/usr/bin/python3
"""task 8"""
from flask import Flask, jsonify, request, make_response
from api.v1.views import app_views
from models.user import User
from flask import abort
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app_views.route('/users/', methods=['POST'])
def create_users():
    """create  users"""
    e = 'email'
    p = 'password'
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if e not in request.get_json():
        return make_response(jsonify({'error': 'Missing email'}), 400)
    if p not in request.get_json():
        return make_response(jsonify({'error': 'Missing password'}), 400)
    req_data = request.get_json()
    user = User()

    user.password = req_data['password']
    user.first_name = req_data['first_name']
    user.last_name = req_data['last_name']
    user.email = req_data['email']

    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = storage.get("User", user_id)
    """update user"""

    if user is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    user.password = request.get_json()['password']
    user.first_name = request.get_json()['first_name']
    user.last_name = request.get_json()['last_name']
    user.email = request.get_json()['email']
    user.save()
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'])
def deleteByIduser(user_id):
    """ delete by id"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    else:
        storage.delete(user)
        storage.save()
        return jsonify({})


@app_views.route('/users', methods=['GET'])
def getAllusers():
    """get all users"""
    users = []
    allusers = storage.all("User").values()
    for sts in allusers:
        users.append(sts.to_dict())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'])
def getByIduser(user_id):
    users = storage.get("User", user_id)
    if users is None:
        abort(404)
    return jsonify(users.to_dict())

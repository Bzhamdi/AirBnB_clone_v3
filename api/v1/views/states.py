#!/usr/bin/python3
"""task 8"""
from flask import Flask, jsonify, request, make_response
from api.v1.views import app_views
from models.state import State
from flask import abort
from models import storage

app = Flask(__name__)


@app_views.route('/states', methods=['GET'])
def getAll():
    """get all states"""
    states = []
    allstates = storage.all("State").values()
    for sts in allstates:
        states.append(sts.to_dict())
    return jsonify(states)


@app_views.route('/states/<string:state_id>', methods=['GET'])
def getById(state_id):
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'])
def deleteById(state_id):
    """ delete by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()
        return jsonify({})


@app_views.route('states/<state_id>', methods=['PUT'])
def update_state(state_id):
    state = storage.get("State", state_id)
    """update state"""

    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    req_data = request.get_json()

    state.name = req_data['name']
    state.save()
    return jsonify(state.to_dict())


@app_views.route('/states/', methods=['POST'])
def create_state():
    """create  state"""
    n = 'name'
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if n not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    req_data = request.get_json()
    state = State()

    state.name = req_data['name']

    state.save()
    return make_response(jsonify(state.to_dict()), 201)

#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.user import User
from models.city import City


print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(City)))

first_state_id = list(storage.all(City).values())[0].id
print(State)
print("First state: {}".format(storage.get(City, first_state_id)))
#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.city import City


print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))
print("Cit objects: {}".format(storage.count(City)))

first_state_id = list(storage.all(State).values())[0].id
ct = list(storage.all(City).values())[0].id

print("First state: {}".format(storage.get(State, first_state_id)))
print("First ct: {}".format(storage.get(City, ct)))

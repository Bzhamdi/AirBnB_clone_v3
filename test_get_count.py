#!/usr/bin/python3
""" Test .get()
"""
from models import storage
from models.user import User

nb_states = storage.count(User)
if nb_states is None:
    print("None", end="")
print("{}".format(nb_states), end="")
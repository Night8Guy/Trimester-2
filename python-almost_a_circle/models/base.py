#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """
            Assign the public instance attribute id with the provided
            argument
            """
            self.id = id
        else:
            """
            Increment __nb_objects and assign the new value to the public
            instance attribute id
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/python3
"""This module contains the base Class for the AirBnB project."""


class Base:
    """This is the base class.
    The goal of this Class is to manage id attribute
    in all your future classes and to avoid duplicating
    the same code (by extension, same bugs).
    Attributes:
            __nb_objects: number of objects with no id. 
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class instance.
        Args:
                id: id of the object
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects

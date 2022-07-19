#!/usr/bin/python3
""" 
This is Square module doc
"""

class Square:
    """ Represents a Square
    Private instance attribute: size
    Instantiation with optional size.
    """

    __init__(self, size=0):
        """Initializes the data"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

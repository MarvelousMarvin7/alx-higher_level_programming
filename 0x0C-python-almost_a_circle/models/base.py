#!/usr/bin/python3
"""Base class"""


class Base:
    """represents the base of all other classes

    Attributes:
    nb_objects - a private attribute that represent the number of base objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation of class

        Args:
        id - identification of new objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

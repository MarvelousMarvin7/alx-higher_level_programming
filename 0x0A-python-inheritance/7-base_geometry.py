#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry:
    """Geometry Module

    Raise:
    Exception: area() is not implemented
    """

    def area(self):
        """area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer

        Args:
        name: name of geometric space
        value: value of geometric space

        Raise:
        TypeError: <name> must be an integer
        ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry():
    """A geometry module for performeing geometrical calculations"""

    def area(self):
        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        """Check if integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

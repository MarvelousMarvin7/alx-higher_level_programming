#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry():
    """A geometry module for performeing geometrical calculations"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if integer

        Args:
        name - name of parameter
        value - value of parameter

        Raise:
        TypeError: If value is not an integer
        ValueError: if value is less than 1
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

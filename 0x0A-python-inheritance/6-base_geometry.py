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

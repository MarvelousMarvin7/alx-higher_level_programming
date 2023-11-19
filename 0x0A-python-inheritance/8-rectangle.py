#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from 7-base_geometry.py"""

    def __init__(self, width, height):
        """
        Attributes:
        width: width of rectangle
        height: height of rectangle
        """
        self.__width = width
        self.__height = height

        # check if integer
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

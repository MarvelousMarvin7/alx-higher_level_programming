#!/usr/bin/python3
"""Real Definition of a rectangle"""


class Rectangle:
    """
    Initialise with and height with value checks

    Returns:
    Width and Height

    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    """ width fo the triangle"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    """height of the triangle"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

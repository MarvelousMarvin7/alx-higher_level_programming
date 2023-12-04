#!/usr/bin/python3
"""Simple rectangle"""


class Rectangle:
    """Rectangle class developement

    Args:
    width: width of rectangle
    height: Height of rectangle

    Raise: Typerror
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        "Set width"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        "Set height"
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

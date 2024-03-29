#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherirts from BaseGeometry

    Args:
    width - width of rectangle
    height - height of rctangle
    """
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.__height = height

        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

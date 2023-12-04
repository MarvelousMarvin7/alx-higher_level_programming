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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        "Set height"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # area
    def area(self):
        """return area of rectangle"""
        return (self.__width * self.__height)

    # perimeter
    def perimeter(self):
        """return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print rectangle with #"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for h in range(self.__height):
            for w in range(self.__width):
                string += "#"
            if h is not self.__height - 1:
                string += "\n"
        return string

#!/usr/bin/python3
"""Real Definition of a rectangle"""


class Rectangle:
    """
    Initialise with and height with value checks

    Returns:
    Width and Height

    """

    def __init__(self, width=0, height=0):
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

    def area(self):
        """Find area of a triangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Find perimeter of a triangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """print rectangle with '#'"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for h in range(self.__height):
            for w in range(self.__width):
                string += "#"
            if h is not self.__height - 1:
                string += "\n"
        return string

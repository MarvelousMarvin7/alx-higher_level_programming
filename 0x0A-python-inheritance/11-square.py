#!/usr/bin/python3
"""Square #2 class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""

    def __init__(self, size):
        """
        Attributes:
        size: Size of both sides of square
        """
        self.__size = size

        # check if positive integer
        self.integer_validator("size", size)

    def area(self):
        """Implememnt area"""
        return self.__size * self.__size

    def __str__(self):
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string

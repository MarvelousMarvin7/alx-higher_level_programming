#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class Square that inherits from Rectangle"""

    def __init__(self, size):
        """
        Attributes:
        size: size of both sides of square
        """
        self.__size = size

        # check if positive integer
        self.integer_validator("size", size)

        super().__init__(self.__size, self.__size)

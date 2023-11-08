#!/usr/bin/python3
"""Real Definition of a rectangle"""


class Rectangle:
    """
    Initialise with and height with value checks

    Returns:
    Width and Height

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                string += str(self.print_symbol)
            if h is not self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """ return a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """print a message when an instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

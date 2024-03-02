#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constractor of class

        Args:
        width - width of rectangle
        height - height of rectangle
        x - The x coordinate of rectangle
        y - The y coordinate of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y coordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display rectangle with a #"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            print(string)
        [print(string) for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="")for w in range(self.__width)]
            print(string)

    def __str__(self):
        """return string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

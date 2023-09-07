#!/usr/bin/python3
"""A class rectangle that defines it by 3-rectangle.py"""
class Rectangle:
    """Define a class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle with width and height"""
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representation of a rectangle"""
        if (self.__height == 0 or self.__width == 0):
            return ('')
        rectangle_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str = rectangle_str + '#'
            rectangle_str = rectangle_str + '\n'
        return (rectangle_str[:-1])

    def __repr__(self):
        """Return an interanl string of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Retrieves the private instance attribute of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the private instance attribute of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private instance attribute of the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the private instance attribute of the width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return 2 * (self.__width + self.__height)

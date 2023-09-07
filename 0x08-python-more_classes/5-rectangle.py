#!/usr/bin/python3
"""Define a recgtangle class"""
class Rectangle:
    """A class rectangle that defines a rectangle by 4-rectangle.py"""
    def __init__(self, width=0, height=0):
        """Initializing a rectangle"""
        self.width = width
        self.height = height

    def __del__(self):
        """Delete the instance attribute if a string is printed"""
        print("Bye rectangle...")

    @property
    def width(self):
        """It retrieives the private instance attribute for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the privaste instnce attribute for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retteuives the private instance attribute for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the privste instance attribute for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of a rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the string that can be printed in the rectangle"""
        string = ""
        if (self.__width != 0 and self.__height != 0):
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return (string)

    def __repr__(self):
        """Return that string for the rectangple for repr"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

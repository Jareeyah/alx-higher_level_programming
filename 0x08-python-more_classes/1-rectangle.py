#!/usr/bin/python3

"""This defines a class Rectangle"""

class Rectangle:
    """A rectngle class based on 0-rectangle.py"""
    
    def __init__(self, width=0, height=0):
        """Initializing a new rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """It retrieves the private instant property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """It sets the private instance property width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """It retrieves the private instance property height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """It sets the private instance property height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

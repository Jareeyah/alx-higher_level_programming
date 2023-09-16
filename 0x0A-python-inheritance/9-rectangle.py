#!/usr/bin/python3

"""
   A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
   (task based on 8-rectangle.py)
"""
class BaseGeometry:
    """A class that inherits from basegeometry"""
    def area(self):
        """It raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """It validates that value for int is greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of a class rectangle"""
    def __init__(self, width, height):
        """An instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

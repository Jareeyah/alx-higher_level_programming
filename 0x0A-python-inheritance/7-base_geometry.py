#!/usr/bin/python3

"""This is a class BaseGeometry (based on 6-base_geometry.py)."""

class BaseGeometry:
    """A class basegeometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if (type(value) is not int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))

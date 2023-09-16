#!/usr/bin/python3
"""
   A class Square that inherits from Rectangle (9-rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A square inherited from rectangle"""
    def __init__(self, size):
        """An instantiation of the size of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of a square"""
        return self.__size ** 2

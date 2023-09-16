#!/usr/bin/python3
"""A class MyInt that inherits from int"""

class MyInt(int):
    """A class that inherits from int"""

    def __new__(cls, *args, **kwargs):
        """Create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other

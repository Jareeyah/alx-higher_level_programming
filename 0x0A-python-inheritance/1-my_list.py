#!/usr/bin/python3

"""A class MyList that inherits from list"""
class MyList(list):
    """class myList interited from list"""

    def __init__(self):
        """It initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list, but sorted"""
        print(sorted(self))

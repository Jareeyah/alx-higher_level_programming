#!/usr/bin/python3

"""A class MyList that inherits from list"""
class MyList(list):
    """class myList interited from list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))

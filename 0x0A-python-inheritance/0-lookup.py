#!/usr/bin/python3

"""A function that returns the list of available attributes and methods of an objec"""
def lookup(obj):
    """Return the list of available attriutes of an object"""
    return (dir(obj))

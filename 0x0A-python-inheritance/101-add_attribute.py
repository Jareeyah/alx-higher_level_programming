#!/usr/bin/python3
"""A function that adds a new attribute to an object if it's possible"""

def add_attribute(prmObject, prmName, prmValue):
    """ Add a new attribute to an object"""
    if not hasattr(prmObject, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(prmObject, prmName)):
        prmObject.__setattr__(prmName, prmValue)

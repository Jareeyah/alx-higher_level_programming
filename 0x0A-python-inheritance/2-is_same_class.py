#!/usr/bin/python3

"""A function that returns True if the object is
   exactly an instance of the specified class
"""
def is_same_class(obj, a_class):
    """Return true if the object is exactly an instance
       of a class otherwise false"""
    if (type(obj) == a_class):
        return (True)
    else:
        return (False)

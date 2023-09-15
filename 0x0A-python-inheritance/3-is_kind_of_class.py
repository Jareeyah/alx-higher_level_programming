#!/usr/bin/python3

"""
   A function that returns True if the object is an instance of,
   or if the object is an instance of a class that inherited from,
   the specified class
"""
def is_kind_of_class(obj, a_class):
    """Return true if the object instance or is an istance of a class
       that inherited from the specified class otherwise false
    """
    return (isinstance(obj, a_class))

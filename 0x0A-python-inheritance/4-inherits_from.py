#!/usr/bin/python3

"""
   A function that returns True if the object is an instance of a class
   that inherited (directly or indirectly) from the specified class
"""
def inherits_from(obj, a_class):
    """Return true if the object is an instance of a class
       inherited directly or indirectly otherwise false
    """
    return (issubclass(type(obj),  a_class) and type(obj) != a_class)

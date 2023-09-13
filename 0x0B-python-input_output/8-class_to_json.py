#!/usr/bin/python3

"""A function that returns the dictionary description
   with simple data structure
"""

def class_to_json(obj):
    """Return the dictionary description for json serialization"""
    return (obj.__dict__)

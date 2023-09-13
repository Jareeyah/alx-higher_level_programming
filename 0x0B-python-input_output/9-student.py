#!/usr/bin/python3

"""A class Student that defines a student by:
   Public instance attributes:
   first_name
   last_name
   age
"""

class Student:
    """Class to define students instances"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__.copy())

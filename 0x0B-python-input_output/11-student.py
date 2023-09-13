#!/usr/bin/python3

"""A class Student that defines a student by: (based on 10-student.py)
"""
class Student:
    """It defies the stuendt class instn es"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        o = self.__dict__.copy()
        if type(attrs) is list:

            for i in attrs:
                if (type(i) is not str):
                    return (o)

            d_list = {}

            for r in range(len(attrs)):
                for s in o:
                    if (attrs[r] == s):
                        d_list[s] = o[s]
            return d_list

        return (o)

    def reload_from_json(self, json):
        for a in json:
            self.__dict__[a] = json[a]

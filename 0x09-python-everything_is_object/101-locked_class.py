#!/usr/bin/python3

"""A class with no class object or attribute"""
class LockedClass:
    """Prevent user from creating creating new instance"""
    __slots__ = ["first_name"]

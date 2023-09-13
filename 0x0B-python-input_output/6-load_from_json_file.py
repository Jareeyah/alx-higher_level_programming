#!/usr/bin/python3

"""A function that creates an Object from a JSON file"""
import json

def load_from_json_file(filename):
    """Create an object from a json file"""
    with open(filename, "r", encoding="utf-8") as file:
        return (json.load(file))

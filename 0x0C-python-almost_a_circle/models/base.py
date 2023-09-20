#!/usr/bin/python3

"""A first class Base"""

import csv
import json

class Base:
    """Class Bas"""

    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor"""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This is a list of dictionary in the json string"""
        if (list_dictionaries is None or list_dictionaries == []):
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """This saves the instance tf the object to the file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if (list_objs is None or list_objs == []):
                myfile.write('[]')
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                myfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """It loads the list from the json string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """It creates the method of the class"""
        if (dictionary and dictionary != {}):
            if (cls.__name__ == "Rectangle"):
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """this loads from thw file"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as myfile:
                list_dicts = Base.from_json_string(myfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """this ssrialoze from the csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This loads from the csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if (cls.__name__ == "Rectangle"):
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

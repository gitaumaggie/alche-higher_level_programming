#!/usr/bin/python3
"""Define the Base class for the Almost a Circle project."""

import json


class Base:
    """Manage object IDs and JSON serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Assign an explicit ID or generate an automatic one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries into a JSON string."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string into a list of dictionaries."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        dictionaries = [
            obj.to_dictionary() for obj in list_objs
        ]

        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(dictionaries))

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as file:
                dictionaries = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        return [
            cls.create(**dictionary) for dictionary in dictionaries
        ]

#!/usr/bin/python3
"""File storage module"""
import json


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        __objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path) as f:
                self.__objects = json.loads(f)
        except (FileNotFoundError):
            return

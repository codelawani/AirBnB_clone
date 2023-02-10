#!/usr/bin/python3
"""Writes a Class"""

from models.base_model import BaseModel
import json

class FileStorage:
    """creates an Object"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets the key"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
        #self.__objects[obj] = self.__class__.__name__.id

    def save(self):
        """serializes to the JSON file"""
        jsonData = {}
        for key, value in self.__objects.items():
            jsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jsonData, f)
        #with open(self.__file_path, "w") as file:
         #   json.dump(self.__objects, file)
            
    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():
                    newObj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = newObj
            #with open(self.__file_path, "r") as file:
             #   self.__objects = json.load(file)
                
        except FileNotFoundError:
            pass



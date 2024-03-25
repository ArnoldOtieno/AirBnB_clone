#!/usr/bin/python3
"""Definition of class FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls:
            nwObj = {}
            for key, values in self.__objects.items():
                if values.__class__ == cls or values.__class__.__name__ == cls:
                    nwObj[key] = values
            return nwObj
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        nwdct = {}
        for key, value in self.__objects.items():
            nwdct[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(nwdct, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as z:
                for key, value in json.load(z).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

#!/usr/bin/python3
"""
file storge class
"""
from Base import BaseModel
import json
from module.user import User


class FileStorage:
    """
    file storge class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return all objects
        """
        return self.__objects

    def new(self, object):
        """
        make a new objects
        """
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        """
        convert to json string
        """
        with open(self.__file_path, "w") as name:
            json.dump({key: value.to_dict()
                     for key, value in self.__objects.items()}, name)

    def reload(self):
        """
        convert to string
        """
        try:
            with open(self.__file_path, "r") as name:
                Dict = json.loads(name.read())
                for value in Dict.values():
                    clsName = value["__class__"]
                    self.new(eval(clsName)(**value))
        except Exception:
            pass

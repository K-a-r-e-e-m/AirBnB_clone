#!/usr/bin/python3
"""
    class FileStorage
"""
import json
import models


class FileStorage:
    """
        file storage.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Return a dictionary
        """
        return self.__objects

    def new(self, obj):
        """
            name method
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
            convert to json
        """
        dct = {}
        for key, value in FileStorage.__objects.items():
            dct[key] = value.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as name:
            json.dump(dct, name)

    def reload(self):
        """
            convert to string
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as name:
                FileStorage.__objects = json.load(name)
            for key, value in FileStorage.__objects.items():
                class_name = value["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass

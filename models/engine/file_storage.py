#!/usr/bin/python3
'''This module have class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''Serialize and deserializes in json file'''
    __file_path = "file.json"
    __objects = {}
    class_map = {
        'BaseModel': BaseModel
    }

    def all(self):
        """Return a dictionary"""
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        if obj:
            key = f"{self.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, 'r') as json_file:
                obj_dict = json.load(json_file)
                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    obj = self.class_map[class_name](**val)
                    self.__objects[key] = obj
    # We can use eval or globals() instead of a class map.
    # However, eval have a security risk because it can execute arbitrary code.
    # globals() may be confusing, it returns a dictionary containing
    # all global variables, functions, and classes in the current module.
    # Using a class map is a safer and more explicit method to dynamically
    # create instances of classes.
        except Exception:
            pass

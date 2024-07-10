#!/usr/bin/python3
'''Create tests fro file storage Class using unittest'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class TestFileStorage(unittest.TestCase):
    '''Test methods of file storage class'''

    def test_all(self):
        '''Test all method that return a dictionary'''
        inst = FileStorage()
        dic = inst.all()
        self.assertIsInstance(dic, dict)

    def test_all_return(self):
        '''Test all method that return a dictionary'''
        inst = FileStorage()
        dic = inst.all()
        self.assertEqual(type(dic), dict)

    def test_new(self):
        '''Test new method that set in __objects the new obj'''
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        with open('file.json', 'r') as file:
            out_dict = file.read()
            self.assertIn(f'BaseModel.{base.id}', out_dict)

    def test_file_type(self):    
        '''Test type of file'''
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
    
    def test_objects_type(self):
        '''Test type of objects'''
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_all_type(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_save_with_new(self):
        '''Test save method with new instance'''
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        with open('file.json', 'r') as file:
            content = file.read()
            self.assertIn(f'BaseModel.{base.id}', content)
    
    def test_reload_with_new_save(self):
        '''Test reload method when create new instance and save it'''
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        models.storage.reload()
        myObjects =  FileStorage._FileStorage__objects
        self.assertIn(f'BaseModel.{base.id}', myObjects)






if __name__ == '__main_':
    unittest.main()

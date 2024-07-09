#!/usr/bin/python3
'''Create tests fro file storage Class using unittest'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models


class TestFileStorage(unittest.TestCase):
    '''Test methods of file storage class'''

    def test_all(self):
        '''Test all method that return a dictionary'''
        inst = FileStorage()
        dic = inst.all()
        self.assertIsInstance(dic, dict)

    def test_all(self):
        '''Test all method that return a dictionary'''
        inst = FileStorage()
        dic = inst.all()
        self.assertEqual(dic, FileStorage._FileStorage__objects)

    def test_new(self):
        '''Test new method that set in __objects the new obj'''
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        with open('file.json', 'r') as file:
            out_dict = file.read()
            self.assertIn(f'BaseModel.{base.id}', out_dict)

    def test_file(self):    
        '''Test type of file'''
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
    
    def test_objects(self):
        '''Test type of objects'''
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

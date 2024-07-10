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
    def setUp(self):
        '''Setup instance for file storage before each method'''
        self.base = BaseModel()
        self.inst = FileStorage()
        self.user = User()
        self.state = State()
        self.place = Place()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()

    def tearDown(self):
        '''Delete instacne after each method'''
        del self.inst
        del self.base
        del self.user
        del self.state
        del self.place
        del self.city
        del self.amenity
        del self.review

    def test_all(self):
        '''Test all method that return a dictionary'''
        dic = self.inst.all()
        self.assertIsInstance(dic, dict)

    def test_all_return(self):
        '''Test all method that return a dictionary'''
        dic = self.inst.all()
        self.assertEqual(type(dic), dict)

    def test_all_with_arg(self):
        '''Test all that doesn't accept any arguments'''
        with self.assertRaises(TypeError):
            self.inst.all('anything')

    def test_new(self):
        '''Test new method that set in __objects the new obj'''
        models.storage.new(self.base)
        models.storage.save()
        with open('file.json', 'r') as file:
            out_dict = file.read()
            self.assertIn(f'BaseModel.{self.base.id}', out_dict)

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
        models.storage.new(self.base)
        models.storage.new(self.user)
        models.storage.new(self.state)
        models.storage.new(self.place)
        models.storage.new(self.city)
        models.storage.new(self.amenity)
        models.storage.new(self.review)
        models.storage.save()
        with open('file.json', 'r') as file:
            content = file.read()
            self.assertIn(f'BaseModel.{self.base.id}', content)
            self.assertIn(f'User.{self.user.id}', content)
            self.assertIn(f'State.{self.state.id}', content)
            self.assertIn(f'Place.{self.place.id}', content)
            self.assertIn(f'City.{self.city.id}', content)
            self.assertIn(f'Review.{self.review.id}', content)
    
    def test_reload_with_new_save(self):
        '''Test reload method when create new instance and save it'''
        models.storage.new(self.base)
        models.storage.new(self.user)
        models.storage.new(self.state)
        models.storage.new(self.place)
        models.storage.new(self.city)
        models.storage.new(self.amenity)
        models.storage.new(self.review)
        models.storage.save()
        models.storage.reload()
        myObjects =  FileStorage._FileStorage__objects
        self.assertIn(f'BaseModel.{self.base.id}', myObjects)
        self.assertIn(f'User.{self.user.id}', myObjects)
        self.assertIn(f'State.{self.state.id}', myObjects)
        self.assertIn(f'Place.{self.place.id}', myObjects)
        self.assertIn(f'City.{self.city.id}', myObjects)
        self.assertIn(f'Review.{self.review.id}', myObjects)






if __name__ == '__main_':
    unittest.main()

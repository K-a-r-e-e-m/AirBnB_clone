#!/usr/bin/python3
'''test_amenity module for test the class amenity with unittesting'''
import unittest
from models.amenity import Amenity


class Testamenity(unittest.TestCase):
    '''Add tests for amenity class attributes and methods'''
    
    def test_amenity_attributes(self):
        '''Test attributes of the amenity'''
        amenity1 = Amenity()
        self.assertEqual(type(amenity1.name), str)


    def test_amenity_epmty_string(self):
            '''Test attributes of the amenity'''
            amenity1 = Amenity()
            self.assertEqual(amenity1.name, '')

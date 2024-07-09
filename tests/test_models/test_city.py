#!/usr/bin/python3
'''test_city module for test the class city with unittesting'''
import unittest
from models.city import City


class Testcity(unittest.TestCase):
    '''Add tests for city class attributes and methods'''
    
    def test_city_attributes(self):
        '''Test attributes of the city'''
        city1 = City()
        self.assertEqual(type(city1.state_id), str)
        self.assertEqual(type(city1.name), str)


    def test_city_epmty_string(self):
            '''Test attributes of the city'''
            city1 = City()
            self.assertEqual(city1.state_id, '')
            self.assertEqual(city1.name, '')

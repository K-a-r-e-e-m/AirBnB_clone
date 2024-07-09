#!/usr/bin/python3
'''test_place module for test the class place with unittesting'''
import unittest
from models.place import Place


class Testplace(unittest.TestCase):
    '''Add tests for place class attributes and methods'''
    
    def test_place_attributes(self):
        '''Test attributes of the place'''
        place1 = Place()
        self.assertEqual(type(place1.city_id), str)
        self.assertEqual(type(place1.user_id), str)
        self.assertEqual(type(place1.name), str)
        self.assertEqual(type(place1.description), str)
        self.assertEqual(type(place1.number_rooms), int)
        self.assertEqual(type(place1.number_bathrooms), int)
        self.assertEqual(type(place1.max_guest), int)
        self.assertEqual(type(place1.price_by_night), int)
        self.assertEqual(type(place1.latitude), float)
        self.assertEqual(type(place1.longitude), float)
        self.assertEqual(type(place1.amenity_ids), list)

    def test_place_epmty_string(self):
            '''Test attributes of the place'''
            place1 = Place()
            self.assertEqual(place1.city_id, '')
            self.assertEqual(place1.user_id, '')
            self.assertEqual(place1.name, '')
            self.assertEqual(place1.description, '')
            self.assertEqual(place1.number_rooms, 0)
            self.assertEqual(place1.number_bathrooms, 0)
            self.assertEqual(place1.max_guest, 0)
            self.assertEqual(place1.price_by_night, 0)
            self.assertEqual(place1.latitude, 0.0)
            self.assertEqual(place1.longitude, 0.0)
            self.assertEqual(place1.amenity_ids, [])

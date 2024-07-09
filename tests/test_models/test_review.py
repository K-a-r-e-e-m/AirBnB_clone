#!/usr/bin/python3
'''test_review module for test the class review with unittesting'''
import unittest
from models.review import Review


class Testreview(unittest.TestCase):
    '''Add tests for review class attributes and methods'''
    
    def test_review_attributes(self):
        '''Test attributes of the review'''
        review1 = Review()
        self.assertEqual(type(review1.place_id), str)
        self.assertEqual(type(review1.user_id), str)
        self.assertEqual(type(review1.text), str)

    def test_review_epmty_string(self):
            '''Test attributes of the review'''
            review1 = Review()
            self.assertEqual(review1.place_id, '')
            self.assertEqual(review1.user_id, '')
            self.assertEqual(review1.text, '')

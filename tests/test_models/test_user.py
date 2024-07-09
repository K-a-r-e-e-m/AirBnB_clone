#!/usr/bin/python3
'''test_user module for test the class User with unittesting'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''Add tests for user class attributes and methods'''
    
    def test_user_attributes(self):
        '''Test attributes of the user'''
        user1 = User()
        self.assertEqual(type(user1.email), str)
        self.assertEqual(type(user1.password), str)
        self.assertEqual(type(user1.first_name), str)
        self.assertEqual(type(user1.last_name), str)

    def test_user_epmty_string(self):
            '''Test attributes of the user'''
            user1 = User()
            self.assertEqual(user1.email, '')
            self.assertEqual(user1.password, '')
            self.assertEqual(user1.first_name, '')
            self.assertEqual(user1.last_name, '')

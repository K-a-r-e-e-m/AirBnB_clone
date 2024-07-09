#!/usr/bin/python3
'''test_state module for test the class state with unittesting'''
import unittest
from models.state import State


class Teststate(unittest.TestCase):
    '''Add tests for state class attributes and methods'''
    
    def test_state_attributes(self):
        '''Test attributes of the state'''
        state1 = State()
        self.assertEqual(type(state1.name), str)


    def test_state_epmty_string(self):
            '''Test attributes of the state'''
            state1 = State()
            self.assertEqual(state1.name, '')

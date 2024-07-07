#!/usr/bin/python3
'''Create tests fro base model Class using unittest'''
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    '''Test BaseModel class'''

    def setUp(self):
        '''Setup before each test method'''
        self.inst = BaseModel()

    def test_id_type(self):
        '''Test id is an integar number'''
        self.assertTrue(isinstance(self.inst.id, str))

    def test_created_at_type(self):
        '''Test type of created at'''
        self.assertEqual(type(self.inst.created_at), type(datetime.now()))

    def test_updated_at_type(self):
        '''Test type of updated at'''
        self.assertEqual(type(self.inst.updated_at), type(datetime.now()))

    def test_save(self):
        '''test save method'''
        update = self.inst.updated_at
        self.inst.save()
        self.assertNotEqual(update, self.inst.updated_at)

    def test_to_dict(self):
        '''Test the method that return dictionary of instance'''
        out = self.inst.to_dict()
        self.assertEqual(type(out), dict)

    def test_to_dict_created_at(self):
        '''Test the method that return dictionary of instance'''
        out = self.inst.to_dict()
        created = out['created_at']
        self.assertEqual(created, self.inst.created_at.isoformat())

    def test_to_dict_updated_at(self):
        '''Test the method that return dictionary of instance'''
        out = self.inst.to_dict()
        updated = out['updated_at']
        self.assertEqual(updated, self.inst.updated_at.isoformat())


    def test__str__(self):
        '''test String representation of instance'''
        out = f'[{self.inst.__class__.__name__}] ({self.inst.id}) {self.inst.__dict__}'
        self.assertEqual(out, self.inst.__str__())

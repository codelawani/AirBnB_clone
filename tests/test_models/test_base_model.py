#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import uuid
from datetime import datetime
"""Tests the BaseModels"""


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    
    def setUp(self):
        """Sets up test methods"""
        self.bm = BaseModel()

    def test_instance(self):
        """Tests the creation of an instance of BaseModel"""
        self.assertIsInstance(self.bm, BaseModel)

    def test_id(self):
        """Tests the id of the BaseModel instance"""
        self.assertEqual(type(self.bm.id), str)
        self.assertEqual(len(self.bm.id), 36)

    def test_created_at(self):
        """Tests the created_at attribute of the BaseModel instance"""
        self.assertEqual(type(self.bm.created_at), datetime)

    def test_updated_at(self):
        """Tests the updated_at attribute of the BaseModel instance"""
        self.assertEqual(type(self.bm.updated_at), datetime)

    def test_save(self):
        """Tests the save method of the BaseModel instance"""
        prev_update = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(prev_update, self.bm.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method of the BaseModel instance"""
        bm_dict = self.bm.to_dict()
        self.assertEqual(type(bm_dict), dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(type(bm_dict['created_at']), str)
        self.assertEqual(type(bm_dict['updated_at']), str)
        self.assertEqual(bm_dict['id'], self.bm.id)

if __name__ == "__main__":
    unittest.main()

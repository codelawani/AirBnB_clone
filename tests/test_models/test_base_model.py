#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.b = BaseModel()

    def test_init(self):
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(b1.id)
        self.assertTrue(b1.created_at)
        self.assertTrue(b1.updated_at)

    def test_id(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)
        self.assertEqual(len(b1.id), 36)

    def test_unique_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_at(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b2.created_at, datetime)
        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_updated_at(self):
        self.assertIsInstance(self.b.updated_at, datetime)
        previous_update = self.b.created_at
        self.b.name = "betty"
        self.assertNotEqual(previous_update, self.b.updated_at)

    def test_kwargs(self):
        objdict = self.b.to_dict()
        b1 = BaseModel(**objdict)
        self.assertEqual(b1.id, self.b.id)
        self.assertIsNot(b1, self.b)

    def test_str(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.__str__(), str)

    def test_save(self):
        b1 = BaseModel()
        b1.save()

    def test_to_dict(self):
        """Tests the to_dict method of the BaseModel instance"""
        bm_dict = self.b.to_dict()
        self.assertEqual(type(bm_dict), dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(type(bm_dict['created_at']), str)
        self.assertEqual(type(bm_dict['updated_at']), str)
        self.assertEqual(bm_dict['id'], self.b.id)
        self.assertEqual(bm_dict['created_at'],
                         datetime.isoformat(self.b.created_at))
        self.assertEqual(bm_dict['updated_at'],
                         datetime.isoformat(self.b.updated_at))


if __name__ == '__main__':
    unittest.main()

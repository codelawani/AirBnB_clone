import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """creates class"""
        cls.testAmenity = Amenity()
        cls.testAmenity.name = "Amenity Name"

    @classmethod
    def tearDownClass(cls):
        """deletes test class"""
        del cls.testAmenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_and_class_variables(self):
        """tests init and class variables"""
        self.assertTrue(isinstance(self.testAmenity, Amenity))
        self.assertTrue(issubclass(type(self.testAmenity), BaseModel))
        self.assertTrue('name' in self.testAmenity.__dict__)
        self.assertTrue('id' in self.testAmenity.__dict__)
        self.assertTrue('created_at' in self.testAmenity.__dict__)
        self.assertTrue('updated_at' in self.testAmenity.__dict__)

    def test_save(self):
        self.testAmenity.save()
        self.assertTrue(self.testAmenity.updated_at != self.testAmenity.created_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.testAmenity), True)

if __name__ == '__main__':
    unittest.main()

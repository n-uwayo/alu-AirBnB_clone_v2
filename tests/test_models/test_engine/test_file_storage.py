#!/usr/bin/python3
"""Module for testing file storage"""
import unittest
import os
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """Set up test environment"""
        storage.reload()

    def tearDown(self):
        """Remove storage file at the end of tests"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """New object is correctly added to __objects"""
        new = BaseModel()
        new.save()
        key = "{}.{}".format(type(new).__name__, new.id)
        self.assertTrue(key in storage.all())

    def test_all(self):
        """Test the all method"""
        new1 = BaseModel()
        new2 = BaseModel()
        storage.save()
        self.assertEqual(len(storage.all()), 2)

if __name__ == '__main__':
    unittest.main()

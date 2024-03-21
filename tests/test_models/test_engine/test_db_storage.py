#!/usr/bin/python3
"""comment"""


import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
import models
from os import getenv


env = getenv("HBNB_TYPE_STORAGE")


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Set up a new DBStorage instance before each test."""
        self.db_storage = DBStorage()
        self.db_storage.reload()


    # def test_all(self):
    #     """Test the 'all' method."""
    #     test_model = BaseModel()
    #     test_model.save()
    #     objects = self.db_storage.all()
    #     self.assertIn(f"BaseModel.{test_model.id}", objects)



class TestFileStorage(unittest.TestCase):
    @unittest.skipIf(env != 'db', "Test skipped unless env is 'db'")
    def test_all_returns_dict(self):
        """Test if all() method returns a dictionary"""
        objects_dict = models.storage.all()
        self.assertIsInstance(objects_dict, dict)



if __name__ == '__main__':
    unittest.main()
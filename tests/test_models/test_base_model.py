#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))


class Test_save(unittest.TestCase):
    """Unittests for testing save method """

    def test_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)
    def test_str(self):
        """ """
        self.name = 'BaseModel'
        self.value = BaseModel
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id, i.__dict__))



class Test_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method"""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)


if __name__ == "__main__":
    unittest.main()

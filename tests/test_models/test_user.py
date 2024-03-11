#!/usr/bin/python3
"""Tests for the class User """
from tests.test_models.test_base_model import Test_instantiation
from models.user import User

class test_User(Test_instantiation):
    """Tests user"""
    def __init__(self, *args, **kwargs):
        """Intializes user """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Tests first Name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_email(self):
        """Tests email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_last_name(self):
        """Test last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_password(self):
        """Tests password """
        new = self.value()
        self.assertEqual(type(new.password), str)

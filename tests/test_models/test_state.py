#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import Test_instantiation
from models.state import State

class test_state(Test_instantiation):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

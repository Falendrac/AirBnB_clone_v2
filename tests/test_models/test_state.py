#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import storage_Type
from models.state import State
import unittest


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(storage_Type == 'db', "do not test with dbstorage")
    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

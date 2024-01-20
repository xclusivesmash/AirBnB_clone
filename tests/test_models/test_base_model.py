#!/usr/bin/env python3
"""
Module: test_base_model
Description: Performs unit testing on the base model class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    """Testing the base model to check if it is
       working as expected based on code definition.
    """

    @classmethod
    def setUpClass(cls):
        """Set up resources to be used."""
        # from models.base_model import BaseModel
        cls.m = BaseModel()
        return None

    # Check if self.m is part of BaseModel class
    def test_isInstance(self):
        """does the checking."""
        self.assertTrue(isinstance(self.m, BaseModel))
        return None

    # Check if the public attributes are not None.
    def test_isNotNone(self):
        """Checking happens here."""
        self.assertIsNotNone(self.m.id)
        self.assertIsNotNone(self.m.created_at)
        self.assertIsNotNone(self.m.updated_at)
        return None

    # The id properties.
    def test_idIsString(self):
        """test type of id attribute."""
        self.assertEqual(type(self.m.id), str)
        self.assertIsInstance(self.m.id, str)
        return None

    # The type of created_at and updated_at
    def test_datetimeObjects(self):
        """Test if created_at and updated_at are datetime obj."""
        self.assertIsInstance(self.m.created_at, datetime)
        self.assertIsInstance(self.m.updated_at, datetime)
        return None
    
    # Check datatypes of created_at and updated_at after save.
    def test_isStringObjects(self):
        """Checking happens here."""
        d = self.m.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(d["updated_at"], str)
        self.assertIsInstance(d["created_at"], str)
        return None
    
    # Check for equivalence btw. updated_at and created_at
    @unittest.expectedFailure
    def test_equivalence(self):
        """Checking happens here."""
        self.m.save()
        self.assertEqual(self.m.created_at, self.m.updated_at)
        return None

    # remove unused resources.
    @classmethod
    def tearDownClass(cls):
        """Free used up resources."""
        del cls.m
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        return None


if __name__ == "__main__":
    unittest.main()

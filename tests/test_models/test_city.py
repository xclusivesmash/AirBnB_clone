#!/usr/bin/env python3
"""
Module: test_city
Description: Performs unit testing on city class.
"""
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class."""

    @classmethod
    def setUpClass(cls):
        """Set up resources to be used."""
        cls.cty = City()
        cls.cty.id = "aksjhfcckzdvxguayg"
        cls.cty.name = "Berlin"
        return None

    def test_isObjectInstance(self):
        """Checks if self.cty is instance of City."""
        self.assertIsInstance(self.cty, City)
        return None

    def test_id(self):
        """Checks if id is a str."""
        self.assertEqual(type(self.cty.id), str)
        return None

    @classmethod
    def tearDownClass(cls):
        """Remove all used-up resources."""
        del cls.cty
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        return None


if __name__ == "__main__":
    unittest.main()

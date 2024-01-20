#!/usr/bin/env python3
"""
Module: test_amenity
Description: Performs unit testing on amenity class.
"""
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Set up resources to be used."""
        cls.am = Amenity()
        cls.am.name = "Hacky man"
        return None

    def test_isInstanceObject(self):
        """Check is sel.am is instance of Amenity."""
        self.assertIsInstance(self.am, Amenity)
        return None

    def test_attributesFromBaseModel(self):
        """Checks if id, created_at, and updated_at exist."""
        self.assertTrue(hasattr(self.am, "id"))
        self.assertTrue(hasattr(self.am, "created_at"))
        self.assertTrue(hasattr(self.am, "updated_at"))
        return None

    def test_nameType(self):
        """Checks if name is string."""
        self.assertTrue(type(self.am.name), str)
        return None

    @classmethod
    def tearDownClass(cls):
        """Removes used up resources."""
        del cls.am
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        return


if __name__ == "__main__":
    unittest.main()

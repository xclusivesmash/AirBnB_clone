#!/usr/bin/env python3
"""
Module: test_place
Description: Performs unit testing on place clas.
"""
import unittest
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Place class."""

    @classmethod
    def setUpClass(cls):
        """Set up resources to be used."""
        cls.place = Place()
        return None

    def test_isInstanceObject(self):
        """Check is sel.am is instance of Place."""
        self.assertIsInstance(self.place, Place)
        return None

    def test_attributesFromBaseModel(self):
        """Checks if id, created_at, and updated_at exist."""
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        return None

    def test_stringTypes(self):
        """Checks if attrs. are strings."""
        self.assertTrue(type(self.place.city_id), str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        return None

    def test_integerTypes(self):
        """Checks if attrs. are integers."""
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        return None

    def test_floatTypes(self):
        """Checks if attrs. are floats."""
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        return None

    def test_typeOfAmenity_ids(self):
        """Checks if amenity_ids is a list."""
        self.assertIsInstance(self.place.amenity_ids, list)
        return None

    def test_emptyList(self):
        """Checks if self.amenity_ids is empty."""
        self.assertEqual(len(self.place.amenity_ids), 0)
        return None

    @classmethod
    def tearDownClass(cls):
        """Removes used up resources."""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        return


if __name__ == "__main__":
    unittest.main()

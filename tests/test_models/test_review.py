#!/usr/bin/env python3
"""
Module: test_review
Description: Performs unit testing on review class.
"""
import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up resources to be used."""
        cls.rev = Review()
        cls.rev.place_id = "0.00.1"
        cls.rev.user_id = "9168176"
        cls.rev.text = "I give this place a 10/10"
        return None

    def test_isInstanceObject(self):
        """Check is self.rev is instance of Review."""
        self.assertIsInstance(self.rev, Review)
        return None

    def test_attributesFromBaseModel(self):
        """Checks if id, created_at, and updated_at exist."""
        self.assertTrue(hasattr(self.rev, "id"))
        self.assertTrue(hasattr(self.rev, "created_at"))
        self.assertTrue(hasattr(self.rev, "updated_at"))
        return None

    def test_placeIdType(self):
        """Checks if place_id is string."""
        self.assertTrue(type(self.rev.place_id), str)
        return None

    def test_userIdType(self):
        """Checks if user_id is string."""
        self.assertTrue(type(self.rev.user_id), str)
        return None

    def test_textIfString(self):
        """Checks if text is string."""
        self.assertTrue(type(self.rev.text), str)
        return None

    @classmethod
    def tearDownClass(cls):
        """Removes used up resources."""
        del cls.rev
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        return


if __name__ == "__main__":
    unittest.main()

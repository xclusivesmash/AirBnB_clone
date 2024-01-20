#!/usr/bin/env python3
"""
Module: test_user
Description: Performs unit testing on user class.
"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class."""

    @classmethod
    def setUpClass(cls):
        """Set up resources to be used."""
        cls.user = User()
        return None

    def test_isInstanceObject(self):
        """Check is self.user is instance of user."""
        self.assertIsInstance(self.user, User)
        return None

    def test_attributesFromBaseModel(self):
        """Checks if id, created_at, and updated_at exist."""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        return None

    def test_stringTypes(self):
        """Checks if attrs. are string."""
        self.assertTrue(type(self.user.email), str)
        self.assertTrue(type(self.user.password), str)
        self.assertTrue(type(self.user.first_name), str)
        self.assertTrue(type(self.user.last_name), str)
        return None

    @classmethod
    def tearDownClass(cls):
        """Removes used up resources."""
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        return


if __name__ == "__main__":
    unittest.main()

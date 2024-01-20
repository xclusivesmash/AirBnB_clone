#!/usr/bin/env python3
"""
Module: test_state
Description: Performs unit testing on state class.
"""
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class."""

    @classmethod
    def setUpClass(cls):
        """Set up resources to be used."""
        cls.state = State()
        cls.state.name = "Washington, DC"
        return None

    def test_isInstanceObject(self):
        """Check is sel.am is instance of State."""
        self.assertIsInstance(self.state, State)
        return None

    def test_attributesFromBaseModel(self):
        """Checks if id, created_at, and updated_at exist."""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        return None

    def test_nameType(self):
        """Checks if name is string."""
        self.assertTrue(type(self.state.name), str)
        return None

    @classmethod
    def tearDownClass(cls):
        """Removes used up resources."""
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        return


if __name__ == "__main__":
    unittest.main()

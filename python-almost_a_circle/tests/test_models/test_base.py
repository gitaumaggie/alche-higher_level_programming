#!/usr/bin/python3
"""Provide unit tests for the Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test automatic and explicit ID assignment."""

   
    def test_automatic_id(self):
        """Test that Base assigns an automatic ID."""
        Base._Base__nb_objects = 0

        first = Base()

        self.assertEqual(first.id, 1)

    def test_incrementing_id(self):
        """Test that automatic IDs increment by one."""
        Base._Base__nb_objects = 0

        first = Base()
        second = Base()
        third = Base()

        self.assertEqual(first.id, 1)
        self.assertEqual(second.id, 2)
        self.assertEqual(third.id, 3)

    def test_explicit_id(self):
        """Verify that a supplied ID is preserved."""
        instance = Base(89)
        self.assertEqual(instance.id, 89)

    def test_to_json_none(self):
        """Test JSON serialization of None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty_list(self):
        """Test JSON serialization of an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_dictionary(self):
        """Test JSON serialization of a dictionary list."""
        result = Base.to_json_string([{"id": 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_returns_string(self):
        """Verify that JSON serialization returns a string."""
        result = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(result, str)

    def test_from_json_none(self):
        """Test deserialization of None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty_list(self):
        """Test deserialization of an empty JSON list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_dictionary(self):
        """Test deserialization of a JSON dictionary list."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_returns_list(self):
        """Verify that deserialization returns a list."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()

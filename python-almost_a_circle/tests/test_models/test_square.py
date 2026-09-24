#!/usr/bin/python3
"""Provide unit tests for the Square class."""

import json
import os
import tempfile
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square initialization, methods and file handling."""

    def test_inheritance(self):
        """Verify that Square inherits from Rectangle and Base."""
        square = Square(4)
        self.assertIsInstance(square, Rectangle)
        self.assertIsInstance(square, Base)

    def test_one_argument(self):
        """Test initialization using size only."""
        square = Square(4)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_two_arguments(self):
        """Test initialization with size and x."""
        square = Square(4, 2)
        self.assertEqual(square.x, 2)

    def test_three_arguments(self):
        """Test initialization with size, x and y."""
        square = Square(4, 2, 3)
        self.assertEqual(square.y, 3)

    def test_four_arguments(self):
        """Test initialization with an explicit ID."""
        square = Square(4, 2, 3, 89)
        self.assertEqual(square.id, 89)

    def test_invalid_size_type(self):
        """Reject a size that is not an integer."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("4")

    def test_invalid_x_type(self):
        """Reject an invalid x coordinate."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, "2")

    def test_invalid_y_type(self):
        """Reject an invalid y coordinate."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 2, "3")

    def test_negative_size(self):
        """Reject a negative size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-4)

    def test_zero_size(self):
        """Reject a size of zero."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_x(self):
        """Reject a negative x coordinate."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(4, -2)

    def test_negative_y(self):
        """Reject a negative y coordinate."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(4, 2, -3)

    def test_size_setter(self):
        """Verify that size updates width and height."""
        square = Square(4)
        square.size = 7
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_area(self):
        """Verify the inherited area method."""
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_string_representation(self):
        """Verify the square's string representation."""
        square = Square(4, 2, 3, 89)
        self.assertEqual(str(square), "[Square] (89) 2/3 - 4")

    def test_to_dictionary(self):
        """Verify square dictionary conversion."""
        square = Square(4, 2, 3, 89)
        self.assertEqual(
            square.to_dictionary(),
            {"id": 89, "size": 4, "x": 2, "y": 3}
        )

    def test_update_without_arguments(self):
        """Verify that an empty update changes nothing."""
        square = Square(4, 2, 3, 89)
        square.update()
        self.assertEqual(
            square.to_dictionary(),
            {"id": 89, "size": 4, "x": 2, "y": 3}
        )

    def test_update_id(self):
        """Update the ID using one positional argument."""
        square = Square(4)
        square.update(89)
        self.assertEqual(square.id, 89)

    def test_update_id_size(self):
        """Update the ID and size."""
        square = Square(4)
        square.update(89, 7)
        self.assertEqual((square.id, square.size), (89, 7))

    def test_update_three_arguments(self):
        """Update the ID, size and x."""
        square = Square(4)
        square.update(89, 7, 2)
        self.assertEqual(
            (square.id, square.size, square.x),
            (89, 7, 2)
        )

    def test_update_four_arguments(self):
        """Update all square attributes."""
        square = Square(4)
        square.update(89, 7, 2, 3)
        self.assertEqual(
            square.to_dictionary(),
            {"id": 89, "size": 7, "x": 2, "y": 3}
        )

    def test_update_keyword_id(self):
        """Update the ID using a keyword."""
        square = Square(4)
        square.update(id=89)
        self.assertEqual(square.id, 89)

    def test_update_keyword_two_attributes(self):
        """Update the ID and size using keywords."""
        square = Square(4)
        square.update(id=89, size=7)
        self.assertEqual((square.id, square.size), (89, 7))

    def test_update_keyword_three_attributes(self):
        """Update three attributes using keywords."""
        square = Square(4)
        square.update(id=89, size=7, x=2)
        self.assertEqual(
            (square.id, square.size, square.x),
            (89, 7, 2)
        )

    def test_update_keyword_four_attributes(self):
        """Update all attributes using keywords."""
        square = Square(4)
        square.update(id=89, size=7, x=2, y=3)
        self.assertEqual(
            square.to_dictionary(),
            {"id": 89, "size": 7, "x": 2, "y": 3}
        )

    def test_create(self):
        """Reconstruct a square from dictionary attributes."""
        square = Square.create(id=89, size=4, x=2, y=3)
        self.assertIsInstance(square, Square)
        self.assertEqual(
            square.to_dictionary(),
            {"id": 89, "size": 4, "x": 2, "y": 3}
        )

    def test_save_to_file_none(self):
        """Save None as an empty JSON list."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                Square.save_to_file(None)

                with open("Square.json", encoding="utf-8") as file:
                    self.assertEqual(json.load(file), [])
            finally:
                os.chdir(previous)

    def test_save_to_file_empty_list(self):
        """Save an empty list as JSON."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                Square.save_to_file([])

                with open("Square.json", encoding="utf-8") as file:
                    self.assertEqual(json.load(file), [])
            finally:
                os.chdir(previous)

    def test_save_to_file_square(self):
        """Save a square to a JSON file."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                square = Square(4, 2, 3, 89)
                Square.save_to_file([square])

                with open("Square.json", encoding="utf-8") as file:
                    self.assertEqual(
                        json.load(file),
                        [{"id": 89, "size": 4, "x": 2, "y": 3}]
                    )
            finally:
                os.chdir(previous)

    def test_load_from_missing_file(self):
        """Return an empty list when no JSON file exists."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                self.assertEqual(Square.load_from_file(), [])
            finally:
                os.chdir(previous)

    def test_load_from_existing_file(self):
        """Load a saved square as a new object."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                original = Square(4, 2, 3, 89)
                Square.save_to_file([original])
                loaded = Square.load_from_file()

                self.assertEqual(len(loaded), 1)
                self.assertIsInstance(loaded[0], Square)
                self.assertIsNot(loaded[0], original)
                self.assertEqual(
                    loaded[0].to_dictionary(),
                    original.to_dictionary()
                )
            finally:
                os.chdir(previous)


if __name__ == "__main__":
    unittest.main()

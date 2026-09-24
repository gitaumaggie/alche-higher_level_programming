
#!/usr/bin/python3
"""Provide unit tests for the Rectangle class."""
import os
import tempfile
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test rectangle initialization and attribute validation."""

    def test_inheritance(self):
        """Verify that Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_two_arguments(self):
        """Test initialization with width and height."""
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_three_arguments(self):
        """Test initialization with a horizontal position."""
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 0)

    def test_four_arguments(self):
        """Test initialization with both coordinates."""
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_five_arguments(self):
        """Test initialization with an explicit ID."""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.id, 5)

    def test_invalid_width_type(self):
        """Reject a width that is not an integer."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_invalid_height_type(self):
        """Reject a height that is not an integer."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_invalid_x_type(self):
        """Reject a horizontal position that is not an integer."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_invalid_y_type(self):
        """Reject a vertical position that is not an integer."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_negative_width(self):
        """Reject a negative width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """Reject a negative height."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_zero_width(self):
        """Reject a width of zero."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Reject a height of zero."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_negative_x(self):
        """Reject a negative horizontal position."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        """Reject a negative vertical position."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_boolean_width(self):
        """Reject a boolean width."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)

    def test_float_height(self):
        """Reject a floating-point height."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2.5)

    def test_attribute_update(self):
        """Verify that valid attributes can be changed."""
        rectangle = Rectangle(1, 2)
        rectangle.width = 5
        rectangle.height = 6
        rectangle.x = 3
        rectangle.y = 4

        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)


        
    def test_area(self):
        """Verify that area returns width multiplied by height."""
        rectangle = Rectangle(4, 3)
        self.assertEqual(rectangle.area(), 12)

    def test_string_representation(self):
        """Verify the formatted string representation."""
        rectangle = Rectangle(4, 3, 2, 1, 89)
        self.assertEqual(
            str(rectangle),
            "[Rectangle] (89) 2/1 - 4/3"
        )

    def test_display_without_offsets(self):
        """Verify display without horizontal or vertical offsets."""
        rectangle = Rectangle(3, 2)
        output = StringIO()

        with redirect_stdout(output):
            rectangle.display()

        self.assertEqual(output.getvalue(), "###\n###\n")

    def test_display_with_x(self):
        """Verify display with a horizontal offset."""
        rectangle = Rectangle(3, 2, 2)
        output = StringIO()

        with redirect_stdout(output):
            rectangle.display()

        self.assertEqual(output.getvalue(), "  ###\n  ###\n")

    def test_display_with_x_and_y(self):
        """Verify display with both coordinate offsets."""
        rectangle = Rectangle(3, 2, 2, 1)
        output = StringIO()

        with redirect_stdout(output):
            rectangle.display()

        self.assertEqual(
            output.getvalue(),
            "\n  ###\n  ###\n"
        )

    def test_to_dictionary(self):
        """Verify that rectangle attributes are converted to a dict."""
        rectangle = Rectangle(4, 3, 2, 1, 89)

        self.assertEqual(
            rectangle.to_dictionary(),
            {
                "id": 89,
                "width": 4,
                "height": 3,
                "x": 2,
                "y": 1
            }
        )

    def test_update_without_arguments(self):
        """Verify that an empty update leaves attributes unchanged."""
        rectangle = Rectangle(4, 3, 2, 1, 89)
        rectangle.update()

        self.assertEqual(
            rectangle.to_dictionary(),
            {
                "id": 89,
                "width": 4,
                "height": 3,
                "x": 2,
                "y": 1
            }
        )

    def test_update_id(self):
        """Verify updating the ID using one positional argument."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(89)
        self.assertEqual(rectangle.id, 89)

    def test_update_id_width(self):
        """Verify updating the ID and width."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(89, 1)
        self.assertEqual((rectangle.id, rectangle.width), (89, 1))

    def test_update_id_width_height(self):
        """Verify updating the first three attributes."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(89, 1, 2)

        self.assertEqual(
            (rectangle.id, rectangle.width, rectangle.height),
            (89, 1, 2)
        )

    def test_update_four_arguments(self):
        """Verify updating the ID, width, height and x."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(89, 1, 2, 3)

        self.assertEqual(
            (rectangle.id, rectangle.width, rectangle.height, rectangle.x),
            (89, 1, 2, 3)
        )

    def test_update_five_arguments(self):
        """Verify updating all five attributes."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(89, 1, 2, 3, 4)

        self.assertEqual(
            rectangle.to_dictionary(),
            {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        )

    def test_update_keyword_id(self):
        """Verify updating the ID using a keyword argument."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(**{"id": 89})
        self.assertEqual(rectangle.id, 89)

    def test_update_keyword_id_width(self):
        """Verify updating the ID and width using keywords."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(**{"id": 89, "width": 1})

        self.assertEqual((rectangle.id, rectangle.width), (89, 1))

    def test_update_keyword_three_attributes(self):
        """Verify updating three attributes using keywords."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(**{"id": 89, "width": 1, "height": 2})

        self.assertEqual(
            (rectangle.id, rectangle.width, rectangle.height),
            (89, 1, 2)
        )

    def test_update_keyword_four_attributes(self):
        """Verify updating four attributes using keywords."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(
            **{"id": 89, "width": 1, "height": 2, "x": 3}
        )

        self.assertEqual(
            (rectangle.id, rectangle.width, rectangle.height, rectangle.x),
            (89, 1, 2, 3)
        )

    def test_update_keyword_five_attributes(self):
        """Verify updating all attributes using keywords."""
        rectangle = Rectangle(4, 3, 2, 1, 5)
        rectangle.update(
            **{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        )

        self.assertEqual(
            rectangle.to_dictionary(),
            {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        )

        
    def test_create_with_id(self):
        """Create a rectangle with an explicit ID."""
        rectangle = Rectangle.create(id=89)
        self.assertEqual(rectangle.id, 89)

    def test_create_with_width(self):
        """Create a rectangle with an updated width."""
        rectangle = Rectangle.create(id=89, width=4)
        self.assertEqual(rectangle.width, 4)

    def test_create_with_height(self):
        """Create a rectangle with updated dimensions."""
        rectangle = Rectangle.create(id=89, width=4, height=3)
        self.assertEqual(rectangle.height, 3)

    def test_create_with_x(self):
        """Create a rectangle with a horizontal offset."""
        rectangle = Rectangle.create(
            id=89, width=4, height=3, x=2
        )
        self.assertEqual(rectangle.x, 2)

    def test_create_with_all_attributes(self):
        """Create a rectangle with all its attributes."""
        rectangle = Rectangle.create(
            id=89, width=4, height=3, x=2, y=1
        )

        self.assertEqual(
            rectangle.to_dictionary(),
            {"id": 89, "width": 4, "height": 3, "x": 2, "y": 1}
        )


    def test_save_to_file_none(self):
        """Save None as an empty JSON list."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                Rectangle.save_to_file(None)

                with open("Rectangle.json", encoding="utf-8") as file:
                    self.assertEqual(file.read(), "[]")
            finally:
                os.chdir(previous)

    def test_save_to_file_empty_list(self):
        """Save an empty list to a JSON file."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                Rectangle.save_to_file([])

                with open("Rectangle.json", encoding="utf-8") as file:
                    self.assertEqual(file.read(), "[]")
            finally:
                os.chdir(previous)

    def test_save_to_file_rectangle(self):
        """Save a rectangle to a JSON file."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                rectangle = Rectangle(4, 3, 2, 1, 89)
                Rectangle.save_to_file([rectangle])

                with open("Rectangle.json", encoding="utf-8") as file:
                    data = Base.from_json_string(file.read())

                self.assertEqual(
                    data,
                    [{"id": 89, "width": 4, "height": 3,
                      "x": 2, "y": 1}]
                )
            finally:
                os.chdir(previous)

    def test_load_from_missing_file(self):
        """Return an empty list when no JSON file exists."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                self.assertEqual(Rectangle.load_from_file(), [])
            finally:
                os.chdir(previous)

    def test_load_from_existing_file(self):
        """Reconstruct rectangles from an existing JSON file."""
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)

                original = Rectangle(4, 3, 2, 1, 89)
                Rectangle.save_to_file([original])
                loaded = Rectangle.load_from_file()

                self.assertEqual(len(loaded), 1)
                self.assertIsInstance(loaded[0], Rectangle)
                self.assertIsNot(loaded[0], original)
                self.assertEqual(
                    loaded[0].to_dictionary(),
                    original.to_dictionary()
                )
            finally:
                os.chdir(previous)

if __name__ == "__main__":
    unittest.main()


#!/usr/bin/python3
"""Provide unit tests for the Rectangle class."""

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


if __name__ == "__main__":
    unittest.main()

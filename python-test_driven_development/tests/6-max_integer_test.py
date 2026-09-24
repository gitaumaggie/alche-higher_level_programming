
#!/usr/bin/python3
"""Unit tests for the max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the behavior of max_integer with different lists."""

    def test_ordered_list(self):
        """Test a list in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_ordered_list(self):
        """Test a list in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unordered_list(self):
        """Test a list containing unordered integers."""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_maximum_at_beginning(self):
        """Test when the largest integer comes first."""
        self.assertEqual(max_integer([10, 2, 5, 3]), 10)

    def test_maximum_in_middle(self):
        """Test when the largest integer is in the middle."""
        self.assertEqual(max_integer([2, 8, 3, 1]), 8)

    def test_maximum_at_end(self):
        """Test when the largest integer comes last."""
        self.assertEqual(max_integer([1, 3, 5, 9]), 9)

    def test_single_element(self):
        """Test a list containing one integer."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test the default empty list."""
        self.assertIsNone(max_integer())

    def test_negative_integers(self):
        """Test a list containing only negative integers."""
        self.assertEqual(max_integer([-5, -2, -10]), -2)

    def test_mixed_integers(self):
        """Test a mixture of positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, -3, 8]), 8)

    def test_zero(self):
        """Test a list containing zero."""
        self.assertEqual(max_integer([-3, 0, -1]), 0)

    def test_duplicate_maximum(self):
        """Test a list containing repeated maximum values."""
        self.assertEqual(max_integer([5, 9, 3, 9]), 9)

    def test_identical_elements(self):
        """Test a list whose elements are identical."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_floats(self):
        """Test a list containing floating-point numbers."""
        self.assertEqual(max_integer([2.5, 3.7, 1.2]), 3.7)

    def test_mixed_floats_and_integers(self):
        """Test a list containing integers and floats."""
        self.assertEqual(max_integer([2, 5.5, 3, 4.2]), 5.5)

    def test_large_integers(self):
        """Test a list containing very large integers."""
        self.assertEqual(max_integer([10, 1000000, 999]), 1000000)

    def test_two_elements(self):
        """Test a list containing two elements."""
        self.assertEqual(max_integer([3, 8]), 8)

    def test_original_list_unchanged(self):
        """Test that the function does not modify the input list."""
        numbers = [3, 1, 5, 2]
        self.assertEqual(max_integer(numbers), 5)
        self.assertEqual(numbers, [3, 1, 5, 2])

    def test_invalid_mixed_types(self):
        """Test that incomparable values raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 3])


if __name__ == '__main__':
    unittest.main()

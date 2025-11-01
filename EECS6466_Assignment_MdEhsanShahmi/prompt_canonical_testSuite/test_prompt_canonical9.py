#python
import unittest
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result


class TestRollingMax(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        self.assertEqual(rolling_max([5]), [5])

    def test_all_increasing_elements(self):
        """Test with a list where elements are strictly increasing."""
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_decreasing_elements(self):
        """Test with a list where elements are strictly decreasing."""
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

    def test_mixed_positive_numbers(self):
        """Test with a mixed list of positive numbers, including drops and rises."""
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_with_duplicate_maximums(self):
        """Test with duplicate numbers, some of which are the current maximum."""
        self.assertEqual(rolling_max([5, 5, 3, 7, 7, 2]), [5, 5, 5, 7, 7, 7])

    def test_negative_numbers(self):
        """Test with a list containing only negative numbers."""
        self.assertEqual(rolling_max([-5, -2, -8, -1]), [-5, -2, -2, -1])

    def test_list_with_zeros(self):
        """Test with a list containing zero."""
        self.assertEqual(rolling_max([0, -1, 2, 0, 3]), [0, 0, 2, 2, 3])

    def test_mixed_positive_negative_zero(self):
        """Test with a mix of positive, negative, and zero values."""
        self.assertEqual(rolling_max([-10, 5, 0, -3, 8, 1]), [-10, 5, 5, 5, 8, 8])

    def test_longer_sequence(self):
        """Test with a longer sequence to ensure robustness."""
        self.assertEqual(rolling_max([1, 3, 2, 5, 4, 7, 6, 9, 8, 10]), [1, 3, 3, 5, 5, 7, 7, 9, 9, 10])


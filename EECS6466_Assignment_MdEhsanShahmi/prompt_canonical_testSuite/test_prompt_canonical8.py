#python
import unittest
from typing import List, Tuple

# NOTE: The sum_product function itself is NOT provided here, as per the prompt.
# If you want to run these tests, you would need to define sum_product in the same
# file or import it from another module. For example:
#
# def sum_product(numbers: List[int]) -> Tuple[int, int]:
#     s = 0
#     p = 1
#     for num in numbers:
#         s += num
#         p *= num
#     return (s, p)

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

class TestSumProduct(unittest.TestCase):

    def test_01_empty_list(self):
        """Test with an empty list."""
        # Expected: (0, 1) as per docstring
        self.assertEqual(sum_product([]), (0, 1))

    def test_02_positive_integers(self):
        """Test with a list of positive integers."""
        # Expected: (1 + 2 + 3 + 4, 1 * 2 * 3 * 4) = (10, 24) as per docstring
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_03_single_positive_element(self):
        """Test with a list containing a single positive integer."""
        # Expected: (5, 5)
        self.assertEqual(sum_product([5]), (5, 5))

    def test_04_single_negative_element(self):
        """Test with a list containing a single negative integer."""
        # Expected: (-3, -3)
        self.assertEqual(sum_product([-3]), (-3, -3))

    def test_05_list_with_zero(self):
        """Test with a list containing zero, which should make the product zero."""
        # Expected: (1 + 2 + 0 + 4, 1 * 2 * 0 * 4) = (7, 0)
        self.assertEqual(sum_product([1, 2, 0, 4]), (7, 0))

    def test_06_all_negative_integers(self):
        """Test with a list of all negative integers."""
        # Expected: (-1 + -2 + -3, -1 * -2 * -3) = (-6, -6)
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_07_mixed_positive_and_negative(self):
        """Test with a mix of positive and negative integers."""
        # Expected: (1 + -2 + 3, 1 * -2 * 3) = (2, -6)
        self.assertEqual(sum_product([1, -2, 3]), (2, -6))

    def test_08_all_zeros(self):
        """Test with a list containing only zeros."""
        # Expected: (0 + 0 + 0, 0 * 0 * 0) = (0, 0)
        self.assertEqual(sum_product([0, 0, 0]), (0, 0))

    def test_09_larger_positive_numbers(self):
        """Test with a larger list of positive integers."""
        # Expected: (10 + 20 + 30, 10 * 20 * 30) = (60, 6000)
        self.assertEqual(sum_product([10, 20, 30]), (60, 6000))

    def test_10_complex_mixed_list(self):
        """Test with a more complex list including positive, negative, and zero."""
        # Expected: (5 + -10 + 2 + 0 + -3, 5 * -10 * 2 * 0 * -3)
        # Sum: 5 - 10 + 2 + 0 - 3 = -6
        # Product: 0 due to the presence of 0
        self.assertEqual(sum_product([5, -10, 2, 0, -3]), (-6, 0))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


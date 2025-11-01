#python
import unittest
from typing import List

# Ground truth solution function
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result


class TestIntersperse(unittest.TestCase):

    def test_01_empty_list(self):
        """Test case 1: An empty input list."""
        numbers = []
        delimiter = 4
        expected = []
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_02_single_element_list(self):
        """Test case 2: A list with a single element."""
        numbers = [1]
        delimiter = 4
        expected = [1]
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_03_standard_case_positive_delimiter(self):
        """Test case 3: Standard case with multiple elements and a positive delimiter (from example)."""
        numbers = [1, 2, 3]
        delimiter = 4
        expected = [1, 4, 2, 4, 3]
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_04_multiple_elements_negative_delimiter(self):
        """Test case 4: Multiple elements with a negative delimiter."""
        numbers = [1, 2, 3]
        delimiter = -5
        expected = [1, -5, 2, -5, 3]
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_05_list_with_negative_numbers(self):
        """Test case 5: List containing negative numbers."""
        numbers = [-1, -2, -3]
        delimiter = 0
        expected = [-1, 0, -2, 0, -3]
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_06_list_with_zero_elements(self):
        """Test case 6: List containing zero as an element."""
        numbers = [0, 1, 0, 2]
        delimiter = 5
        expected = [0, 5, 1, 5, 0, 5, 2]
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_07_delimiter_is_zero(self):
        """Test case 7: Delimiter itself is zero."""
        numbers = [1, 2, 3]
        delimiter = 0
        expected = [1, 0, 2, 0, 3]
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_08_list_with_duplicate_numbers(self):
        """Test case 8: List containing duplicate numbers."""
        numbers = [1, 1, 2, 2, 3]
        delimiter = 9
        expected = [1, 9, 1, 9, 2, 9, 2, 9, 3]
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_09_delimiter_same_as_list_element(self):
        """Test case 9: Delimiter value is also present as an element in the list."""
        numbers = [5, 6, 7]
        delimiter = 5
        expected = [5, 5, 6, 5, 7]
        self.assertEqual(intersperse(numbers, delimiter), expected)

    def test_10_longer_list(self):
        """Test case 10: A longer list to ensure performance/correctness with more elements."""
        numbers = [10, 20, 30, 40, 50, 60]
        delimiter = 100
        expected = [10, 100, 20, 100, 30, 100, 40, 100, 50, 100, 60]
        self.assertEqual(intersperse(numbers, delimiter), expected)

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

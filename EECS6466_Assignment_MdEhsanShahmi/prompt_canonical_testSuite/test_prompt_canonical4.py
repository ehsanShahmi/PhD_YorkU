#python
import unittest
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculates the Mean Absolute Deviation (MAD) of a list of numbers.

    The Mean Absolute Deviation is the average of the absolute differences
    between each data point and the mean of the dataset.

    Args:
        numbers: A list of floating-point numbers.

    Returns:
        The Mean Absolute Deviation as a float.

    Raises:
        ZeroDivisionError: If the input list `numbers` is empty.
    """
    if not numbers:
        raise ZeroDivisionError("Cannot calculate MAD for an empty list.")
        
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_basic_example(self):
        """
        Test case from the prompt's example.
        Numbers: [1.0, 2.0, 3.0, 4.0]
        Mean: 2.5
        Differences: |1-2.5|=1.5, |2-2.5|=0.5, |3-2.5|=0.5, |4-2.5|=1.5
        MAD: (1.5 + 0.5 + 0.5 + 1.5) / 4 = 4.0 / 4 = 1.0
        """
        numbers = [1.0, 2.0, 3.0, 4.0]
        expected_mad = 1.0
        # Call the function (assumed to be available)
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_single_element_list(self):
        """
        Test with a list containing a single element.
        Mean = element itself. Differences from mean will all be 0.
        Numbers: [5.0]
        Mean: 5.0
        Differences: |5.0 - 5.0| = 0.0
        MAD: 0.0 / 1 = 0.0
        """
        numbers = [5.0]
        expected_mad = 0.0
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_all_elements_identical(self):
        """
        Test with a list where all elements are the same.
        Mean is the element value, so all differences should be 0.
        Numbers: [7.0, 7.0, 7.0, 7.0, 7.0]
        Mean: 7.0
        Differences: |7.0 - 7.0| = 0.0 (for all)
        MAD: 0.0
        """
        numbers = [7.0, 7.0, 7.0, 7.0, 7.0]
        expected_mad = 0.0
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_two_distinct_elements(self):
        """
        Test with a simple list of two distinct elements.
        Numbers: [1.0, 3.0]
        Mean: (1.0 + 3.0) / 2 = 2.0
        Differences: |1.0 - 2.0|=1.0, |3.0 - 2.0|=1.0
        MAD: (1.0 + 1.0) / 2 = 1.0
        """
        numbers = [1.0, 3.0]
        expected_mad = 1.0
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_negative_numbers(self):
        """
        Test with a list containing negative numbers.
        Numbers: [-1.0, 0.0, 1.0]
        Mean: (-1.0 + 0.0 + 1.0) / 3 = 0.0
        Differences: |-1.0 - 0.0|=1.0, |0.0 - 0.0|=0.0, |1.0 - 0.0|=1.0
        MAD: (1.0 + 0.0 + 1.0) / 3 = 2.0 / 3
        """
        numbers = [-1.0, 0.0, 1.0]
        expected_mad = 2.0 / 3.0
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_floating_point_numbers(self):
        """
        Test with a list of more complex floating-point numbers.
        Numbers: [0.5, 1.5, 2.5, 3.5]
        Mean: (0.5 + 1.5 + 2.5 + 3.5) / 4 = 8.0 / 4 = 2.0
        Differences: |0.5-2.0|=1.5, |1.5-2.0|=0.5, |2.5-2.0|=0.5, |3.5-2.0|=1.5
        MAD: (1.5 + 0.5 + 0.5 + 1.5) / 4 = 4.0 / 4 = 1.0
        """
        numbers = [0.5, 1.5, 2.5, 3.5]
        expected_mad = 1.0
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_large_numbers(self):
        """
        Test with larger numbers.
        Numbers: [100.0, 200.0, 300.0]
        Mean: (100.0 + 200.0 + 300.0) / 3 = 600.0 / 3 = 200.0
        Differences: |100-200|=100, |200-200|=0, |300-200|=100
        MAD: (100.0 + 0.0 + 100.0) / 3 = 200.0 / 3.0
        """
        numbers = [100.0, 200.0, 300.0]
        expected_mad = 200.0 / 3.0
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_mixed_positive_negative_zero(self):
        """
        Test with a mix of positive, negative, and zero values.
        Numbers: [-2.0, -1.0, 0.0, 1.0, 2.0]
        Mean: (-2 - 1 + 0 + 1 + 2) / 5 = 0.0 / 5 = 0.0
        Differences: |-2-0|=2, |-1-0|=1, |0-0|=0, |1-0|=1, |2-0|=2
        MAD: (2.0 + 1.0 + 0.0 + 1.0 + 2.0) / 5 = 6.0 / 5 = 1.2
        """
        numbers = [-2.0, -1.0, 0.0, 1.0, 2.0]
        expected_mad = 1.2
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_list_with_zero(self):
        """
        Test with numbers including zero, but not centered at zero.
        Numbers: [0.0, 10.0, 20.0]
        Mean: (0.0 + 10.0 + 20.0) / 3 = 30.0 / 3 = 10.0
        Differences: |0-10|=10, |10-10|=0, |20-10|=10
        MAD: (10.0 + 0.0 + 10.0) / 3 = 20.0 / 3.0
        """
        numbers = [0.0, 10.0, 20.0]
        expected_mad = 20.0 / 3.0
        actual_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(actual_mad, expected_mad, places=7)

    def test_empty_list_raises_error(self):
        """
        Test for an empty list. Calculating the mean of an empty list
        involves division by zero, which should typically raise an error.
        A common Python behavior for sum()/len() on an empty list is ZeroDivisionError.
        """
        numbers = []
        with self.assertRaises(ZeroDivisionError):
            mean_absolute_deviation(numbers)

# This allows running the tests directly from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#python
import unittest

def truncate_number(number: float) -> float:
    """ 
    Truncates a positive floating-point number to its decimal part.

    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0

class TestTruncateNumber(unittest.TestCase):
    """
    Test suite for the 'truncate_number' function.
    Tests various positive floating-point numbers to ensure the decimal
    part is correctly returned.
    """

    def test_example_from_prompt(self):
        """
        Test case directly from the function's docstring example.
        Input: 3.5, Expected Output: 0.5
        """
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=9)

    def test_basic_float_one(self):
        """
        Test with a simple positive floating-point number.
        Input: 1.23, Expected Output: 0.23
        """
        self.assertAlmostEqual(truncate_number(1.23), 0.23, places=9)

    def test_large_integer_part(self):
        """
        Test with a number having a significantly large integer part.
        Input: 1000.789, Expected Output: 0.789
        """
        self.assertAlmostEqual(truncate_number(1000.789), 0.789, places=9)

    def test_small_decimal_part(self):
        """
        Test with a number where the decimal part is very small.
        Input: 5.01, Expected Output: 0.01
        """
        self.assertAlmostEqual(truncate_number(5.01), 0.01, places=9)

    def test_large_decimal_part(self):
        """
        Test with a number where the decimal part is close to 1.
        Input: 2.9999, Expected Output: 0.9999
        """
        self.assertAlmostEqual(truncate_number(2.9999), 0.9999, places=9)

    def test_number_with_zero_decimal(self):
        """
        Test a positive integer number (where the decimal part is effectively 0).
        Input: 7.0, Expected Output: 0.0
        """
        self.assertAlmostEqual(truncate_number(7.0), 0.0, places=9)

    def test_number_with_zero_integer_part(self):
        """
        Test a number where the integer part is 0 (i.e., 0 < number < 1).
        Input: 0.12345, Expected Output: 0.12345
        """
        self.assertAlmostEqual(truncate_number(0.12345), 0.12345, places=9)

    def test_number_close_to_zero(self):
        """
        Test a very small positive floating-point number.
        Input: 0.000000001, Expected Output: 0.000000001
        """
        self.assertAlmostEqual(truncate_number(0.000000001), 0.000000001, places=9)

    def test_number_with_many_decimal_places(self):
        """
        Test a number with a precise and long decimal part.
        Input: 9.123456789, Expected Output: 0.123456789
        """
        self.assertAlmostEqual(truncate_number(9.123456789), 0.123456789, places=9)

    def test_another_large_number_with_decimals(self):
        """
        Test with another large number and a simple decimal.
        Input: 987654321.1, Expected Output: 0.1
        """
        self.assertAlmostEqual(truncate_number(987654321.1), 0.1, places=9)

# This allows the test suite to be run from the command line
if __name__ == '__main__':
    unittest.main()

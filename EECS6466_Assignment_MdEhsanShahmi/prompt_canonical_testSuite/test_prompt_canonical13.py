#python
import unittest

def greatest_common_divisor(a, b):
    """
    Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    The GCD is the largest positive integer that divides both a and b without leaving a remainder.
    Standard behavior implies gcd(a, b) = gcd(|a|, |b|) and gcd(N, 0) = |N|, gcd(0, 0) = 0.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    # Handle negative inputs by taking their absolute values
    a = abs(a)
    b = abs(b)

    # Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

class TestGreatestCommonDivisor(unittest.TestCase):
    """
    A test suite for the greatest_common_divisor function.
    Assumes greatest_common_divisor(a, b) returns an int representing
    the greatest common divisor of a and b. Standard behavior implies
    gcd(a, b) = gcd(|a|, |b|) and gcd(N, 0) = |N|, gcd(0, 0) = 0.
    """

    def test_positive_primes_coprime(self):
        """
        Test case from prompt: gcd(3, 5) should be 1.
        Two small prime numbers that are coprime.
        """
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_positive_common_multiple(self):
        """
        Test case from prompt: gcd(25, 15) should be 5.
        Two positive numbers with a common factor greater than 1.
        """
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_one_number_is_multiple_of_other(self):
        """
        Test when one number is a multiple of the other: gcd(10, 5) should be 5.
        The smaller number is the GCD.
        """
        self.assertEqual(greatest_common_divisor(10, 5), 5)

    def test_different_composite_numbers(self):
        """
        Test with two different composite numbers: gcd(12, 18) should be 6.
        A general case for two distinct composite numbers.
        """
        self.assertEqual(greatest_common_divisor(12, 18), 6)

    def test_both_numbers_are_equal(self):
        """
        Test when both numbers are the same: gcd(7, 7) should be 7.
        The number itself is the GCD.
        """
        self.assertEqual(greatest_common_divisor(7, 7), 7)

    def test_one_number_is_zero_positive_first(self):
        """
        Test when the first number is zero and the second is positive: gcd(0, 5) should be 5.
        According to standard GCD definition where gcd(N, 0) = |N|.
        """
        self.assertEqual(greatest_common_divisor(0, 5), 5)

    def test_one_number_is_zero_positive_second(self):
        """
        Test when the second number is zero and the first is positive: gcd(5, 0) should be 5.
        According to standard GCD definition where gcd(N, 0) = |N|.
        """
        self.assertEqual(greatest_common_divisor(5, 0), 5)

    def test_both_numbers_are_zero(self):
        """
        Test when both numbers are zero: gcd(0, 0) should be 0.
        This is a common convention for GCD.
        """
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_one_negative_one_positive(self):
        """
        Test with one negative and one positive number: gcd(-6, 9) should be 3.
        GCD is typically defined for non-negative results, often gcd(a,b) = gcd(|a|, |b|).
        """
        self.assertEqual(greatest_common_divisor(-6, 9), 3)

    def test_both_numbers_are_negative(self):
        """
        Test with both numbers negative: gcd(-10, -15) should be 5.
        GCD is typically defined for non-negative results, often gcd(a,b) = gcd(|a|, |b|).
        """
        self.assertEqual(greatest_common_divisor(-10, -15), 5)


if __name__ == '__main__':
    # To run these tests:
    # 1. Ensure the 'greatest_common_divisor' function is defined or imported
    #    in the scope where this script is executed.
    # 2. Save this code as a Python file (e.g., test_gcd.py).
    # 3. Run from your terminal: python -m unittest test_gcd.py
    unittest.main()

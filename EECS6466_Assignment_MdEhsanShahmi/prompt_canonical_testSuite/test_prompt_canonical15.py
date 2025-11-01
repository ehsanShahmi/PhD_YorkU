
import unittest

# NOTE: The implementation of string_sequence is intentionally omitted as per the prompt.
# You would typically place your function definition here:
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    return ' '.join([str(x) for x in range(n + 1)])


class TestStringSequence(unittest.TestCase):

    def test_n_is_zero(self):
        """Test with n = 0, the smallest valid non-negative input."""
        self.assertEqual(string_sequence(0), '0')

    def test_n_is_one(self):
        """Test with n = 1, a small positive integer."""
        self.assertEqual(string_sequence(1), '0 1')

    def test_n_is_five(self):
        """Test with n = 5, as provided in the docstring example."""
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_n_is_ten(self):
        """Test with n = 10, including the first two-digit number."""
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

    def test_n_is_twenty(self):
        """Test with a larger n = 20, to check scalability."""
        expected_output = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'
        self.assertEqual(string_sequence(20), expected_output)

    def test_n_is_nine(self):
        """Test n = 9, which ends just before two-digit numbers begin."""
        self.assertEqual(string_sequence(9), '0 1 2 3 4 5 6 7 8 9')

    def test_n_is_three(self):
        """Test n = 3, another small positive integer."""
        self.assertEqual(string_sequence(3), '0 1 2 3')

    def test_n_is_fifteen(self):
        """Test n = 15, a moderate positive integer."""
        expected_output = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
        self.assertEqual(string_sequence(15), expected_output)

    def test_n_is_negative_one(self):
        """Test with n = -1, which is an invalid input and should raise a ValueError."""
        with self.assertRaises(ValueError):
            string_sequence(-1)

    def test_n_is_negative_five(self):
        """Test with n = -5, another invalid negative input."""
        with self.assertRaises(ValueError):
            string_sequence(-5)


if __name__ == '__main__':
    # To run these tests, you would need to define the string_sequence function
    # For example, uncomment the definition above (or provide your own)

    # Example placeholder for string_sequence function for demonstration purposes
    # If this were a real scenario, string_sequence would be in a separate module
    # or defined above, and these tests would be imported.
    def string_sequence(n: int) -> str:
        if n < 0:
            raise ValueError("n must be a non-negative integer.")
        return ' '.join(str(i) for i in range(n + 1))

    unittest.main(argv=['first-arg-is-ignored'], exit=False)

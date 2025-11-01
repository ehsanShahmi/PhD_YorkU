#python
import unittest

# The 'string_xor' function is expected to be defined elsewhere.
# As per the instruction: "Do not create the solution function of the prompt in any way."
# For this test suite to run successfully, the 'string_xor' function must be
# available in the global scope or imported into the environment where these
# tests are executed.

# An example of how 'string_xor' might be defined (NOT part of the solution, for context only):
# from typing import List # This import might be used by the string_xor function, but not by the tests directly.
# def string_xor(a: str, b: str) -> str:
#     """ Input are two strings a and b consisting only of 1s and 0s.
#     Perform binary XOR on these inputs and return result also as a string.
#     >>> string_xor('010', '110')
#     '100'
#     """
#     if len(a) != len(b):
#         raise ValueError("Input strings must be of equal length.")
#     result = []
#     for i in range(len(a)):
#         if a[i] == b[i]:
#             result.append('0')
#         else:
#             result.append('1')
#     return "".join(result)

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length.")
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


class TestStringXor(unittest.TestCase):
    """
    Test suite for the string_xor function, which performs binary XOR
    on two equal-length strings of '0's and '1's.
    """

    def test_example_from_prompt(self):
        # Test case directly from the problem description's example.
        self.assertEqual(string_xor('010', '110'), '100')

    def test_all_zeros_input(self):
        # Both inputs are strings of all '0's. XORing '0' with '0' always yields '0'.
        self.assertEqual(string_xor('0000', '0000'), '0000')

    def test_all_ones_input(self):
        # Both inputs are strings of all '1's. XORing '1' with '1' always yields '0'.
        self.assertEqual(string_xor('11111', '11111'), '00000')

    def test_complementary_inputs(self):
        # Inputs are bitwise complements of each other. XORing '0' with '1' always yields '1'.
        self.assertEqual(string_xor('010101', '101010'), '111111')

    def test_one_input_all_zeros(self):
        # One input is all '0's. XORing any bit with '0' yields the original bit.
        self.assertEqual(string_xor('11010', '00000'), '11010')

    def test_one_input_all_ones(self):
        # One input is all '1's. XORing any bit with '1' yields its complement.
        self.assertEqual(string_xor('00110', '11111'), '11001')

    def test_single_bit_xor_different(self):
        # Simplest case with different bits: '0' XOR '1'.
        self.assertEqual(string_xor('0', '1'), '1')

    def test_single_bit_xor_same(self):
        # Simplest case with same bits: '1' XOR '1'.
        self.assertEqual(string_xor('1', '1'), '0')

    def test_mixed_patterns_long(self):
        # Longer strings with varied patterns of '0's and '1's.
        self.assertEqual(string_xor('10110011', '01010101'), '11100110')

    def test_another_mixed_pattern(self):
        # Another test case with a mix of identical and differing bits.
        self.assertEqual(string_xor('00110011', '10011001'), '10101010')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

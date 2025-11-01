#####python
def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times

import unittest

# Do not create the solution function of the prompt in any way, as per the instructions.
# The 'how_many_times' function is expected to be defined elsewhere
# or imported into the environment where these tests are executed.
#
# For example, if you were to run these tests, you would need to
# either define the function directly above this point:
#
# def how_many_times(string: str, substring: str) -> int:
#     # ... your implementation here ...
#     pass
#
# Or import it from a module:
# from your_module import how_many_times

class TestHowManyTimes(unittest.TestCase):
    """
    A complete test suite for the 'how_many_times' function,
    which finds overlapping occurrences of a substring in a string.
    """

    def test_01_empty_string_non_empty_substring(self):
        """
        Test case from the prompt: an empty main string should always yield 0 occurrences,
        regardless of the substring.
        >>> how_many_times('', 'a')
        0
        """
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_02_non_empty_string_empty_substring(self):
        """
        Test with an empty substring. Assuming a 'find' operation implies the substring
        must have content, so an empty substring is not "found".
        Note: Python's built-in `str.count('')` behaves differently, returning `len(s) + 1`.
        This test expects 0 for a more common interpretation of "finding" a pattern.
        """
        self.assertEqual(how_many_times('abc', ''), 0)

    def test_03_substring_longer_than_string(self):
        """
        Test when the substring is longer than the main string.
        It should not be possible to find a longer substring.
        """
        self.assertEqual(how_many_times('a', 'aa'), 0)

    def test_04_no_occurrences_at_all(self):
        """
        Test case where the substring does not appear in the string at all,
        without any potential for overlap.
        """
        self.assertEqual(how_many_times('hello', 'world'), 0)

    def test_05_single_occurrence_no_overlap(self):
        """
        Test for a single, non-overlapping occurrence of the substring.
        """
        self.assertEqual(how_many_times('banana', 'nan'), 1)

    def test_06_multiple_non_overlapping_occurrences(self):
        """
        Test for multiple distinct occurrences that do not overlap with each other
        for the given pattern.
        """
        self.assertEqual(how_many_times('ababab', 'ab'), 3)

    def test_07_simple_overlapping_from_prompt(self):
        """
        Test case from the prompt: simple overlapping substring.
        'aa' in 'aaaa' can be found at index 0, index 1, and index 2.
        >>> how_many_times('aaaa', 'aa')
        3
        """
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_08_complex_overlapping_long_substring(self):
        """
        Test with a longer substring causing significant overlap.
        'aaa' in 'aaaaa' can be found at index 0, index 1, and index 2.
        """
        self.assertEqual(how_many_times('aaaaa', 'aaa'), 3)

    def test_09_overlapping_with_alternating_characters(self):
        """
        Test with a more complex overlapping pattern where characters alternate.
        'aba' in 'ababa' can be found at index 0 and index 2.
        """
        self.assertEqual(how_many_times('ababa', 'aba'), 2)

    def test_10_case_sensitivity(self):
        """
        Test to confirm the function is case-sensitive. 'py' should not be found in 'Python'.
        Standard string operations are typically case-sensitive unless specified otherwise.
        """
        self.assertEqual(how_many_times('Python', 'py'), 0)

# This block allows the tests to be run when the script is executed directly.
if __name__ == '__main__':
    # When running this script, ensure the 'how_many_times' function is accessible
    # (e.g., defined in the same file or imported).
    # If the function is not defined, a NameError will occur, which is the expected
    # outcome given the instruction to *not* provide the function's implementation.
    unittest.main()

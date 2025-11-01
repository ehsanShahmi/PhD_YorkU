#python
import unittest
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Given a list of strings, return the longest string.
    If there are multiple strings with the same maximum length, return the first one encountered.
    If the list is empty, return None.
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

class TestLongestString(unittest.TestCase):

    def test_01_empty_list_returns_none(self):
        """
        Test case: An empty list should return None.
        """
        self.assertIsNone(longest([]))

    def test_02_single_string_list(self):
        """
        Test case: A list with a single string should return that string.
        """
        self.assertEqual(longest(['hello']), 'hello')

    def test_03_distinct_lengths_ascending(self):
        """
        Test case: Strings with distinct lengths, increasing order.
        """
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_04_distinct_lengths_descending(self):
        """
        Test case: Strings with distinct lengths, decreasing order.
        """
        self.assertEqual(longest(['longest', 'short', 'medium']), 'longest')

    def test_05_all_same_length_tie_breaking(self):
        """
        Test case: All strings have the same maximum length.
                   Should return the first one encountered.
        """
        self.assertEqual(longest(['apple', 'banana', 'cherry']), 'apple')

    def test_06_mixed_lengths_tie_breaking(self):
        """
        Test case: Mixed lengths, with multiple strings tied for the longest.
                   Should return the first one encountered.
        """
        # 'short' (5), 'banana' (6), 'kiwi' (4), 'orange' (6), 'apple' (5)
        # Max length is 6. 'banana' appears before 'orange'.
        self.assertEqual(longest(['short', 'banana', 'kiwi', 'orange', 'apple']), 'banana')

    def test_07_all_empty_strings(self):
        """
        Test case: A list containing only empty strings.
                   The first empty string should be returned.
        """
        self.assertEqual(longest(['', '', '']), '')

    def test_08_includes_empty_string_and_others(self):
        """
        Test case: A list containing a mix of empty and non-empty strings.
        """
        self.assertEqual(longest(['', 'a', 'bb', 'ccc']), 'ccc')

    def test_09_mixed_case_strings(self):
        """
        Test case: Strings with mixed casing. Length comparison should be case-insensitive.
                   (Length is character count, not affected by case).
        """
        self.assertEqual(longest(['hello', 'WORLD', 'python']), 'python')

    def test_10_strings_representing_numbers(self):
        """
        Test case: Strings that represent numbers. Length should be based on digit count.
        """
        self.assertEqual(longest(['1', '123', '12', '12345']), '12345')

if __name__ == '__main__':
    unittest.main()

#python
import unittest
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    return [x for x in strings if substring in x]


class TestFilterBySubstring(unittest.TestCase):

    # Test Case 1: An empty list of strings should always result in an empty list.
    def test_empty_list(self):
        strings: List[str] = []
        substring: str = 'a'
        expected: List[str] = []
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 2: No strings in the list contain the given substring.
    def test_no_matches(self):
        strings: List[str] = ['bcd', 'cde', 'defg']
        substring: str = 'a'
        expected: List[str] = []
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 3: All strings in the list contain the given substring.
    def test_all_matches(self):
        strings: List[str] = ['banana', 'apple', 'grape']
        substring: str = 'a'
        expected: List[str] = ['banana', 'apple', 'grape']
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 4: A mix of strings, some matching the substring, some not.
    def test_mixed_matches(self):
        strings: List[str] = ['hello', 'world', 'hi', 'python']
        substring: str = 'o'
        expected: List[str] = ['hello', 'world', 'python']
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 5: The substring is an empty string. All strings (including empty ones)
    # are expected to contain an empty substring.
    def test_empty_substring(self):
        strings: List[str] = ['abc', 'def', '', 'ghi']
        substring: str = ''
        expected: List[str] = ['abc', 'def', '', 'ghi']
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 6: Checks for case sensitivity. 'ap' should match 'apple' but not 'Apple'
    # unless the string itself contains 'ap'.
    def test_case_sensitivity(self):
        strings: List[str] = ['Apple', 'apple', 'Banana', 'APRICOT', 'Aplomb']
        substring: str = 'ap'
        expected: List[str] = ['apple', 'APRICOT'] # 'apple' contains 'ap', 'APRICOT' contains 'AP' (case-sensitive)
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 7: Substring appears at the beginning, middle, and end of different words.
    def test_substring_positions(self):
        strings: List[str] = ['testing', 'contest', 'festive', 'fast']
        substring: str = 'st'
        expected: List[str] = ['testing', 'contest', 'festive', 'fast']
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 8: The substring itself contains spaces, and the list contains such strings.
    def test_substring_with_spaces(self):
        strings: List[str] = ['hello world', 'goodbye universe', 'hello', 'world', 'hello there world']
        substring: str = 'hello world'
        expected: List[str] = ['hello world', 'hello there world']
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 9: The input list contains an empty string, and the substring is not empty.
    # The empty string should not be matched unless the substring is also empty.
    def test_list_with_empty_string(self):
        strings: List[str] = ['alpha', '', 'beta', 'alphabet']
        substring: str = 'alpha'
        expected: List[str] = ['alpha', 'alphabet']
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)

    # Test Case 10: Substring contains special characters, and some strings match it.
    def test_special_characters_in_substring(self):
        strings: List[str] = ['user_name', 'user-id-123', 'user_id', 'admin_user', 'user-name']
        substring: str = 'user-'
        expected: List[str] = ['user-id-123', 'user-name']
        actual = filter_by_substring(strings, substring)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

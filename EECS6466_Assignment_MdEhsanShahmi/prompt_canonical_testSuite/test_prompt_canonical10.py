#python
import unittest

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        """
        Test Case 1: An empty string should result in an empty string palindrome.
        """
        self.assertEqual(make_palindrome(''), '')

    def test_already_palindrome_odd_length(self):
        """
        Test Case 2: A string that is already an odd-length palindrome.
        It should return itself.
        """
        self.assertEqual(make_palindrome('madam'), 'madam')

    def test_already_palindrome_even_length(self):
        """
        Test Case 3: A string that is already an even-length palindrome.
        It should return itself.
        """
        self.assertEqual(make_palindrome('level'), 'level')

    def test_single_character_string(self):
        """
        Test Case 4: A single character string, which is inherently a palindrome.
        It should return itself.
        """
        self.assertEqual(make_palindrome('a'), 'a')

    def test_simple_non_palindrome_example(self):
        """
        Test Case 5: A simple non-palindrome string, as per the prompt's example.
        'cat' -> 'catac'
        """
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_non_palindrome_with_multi_char_palindromic_suffix_example(self):
        """
        Test Case 6: A non-palindrome with a multi-character palindromic suffix,
        as per the prompt's example.
        'cata' -> 'catac' (longest palindromic suffix is 'ata')
        """
        self.assertEqual(make_palindrome('cata'), 'catac')

    def test_simple_non_palindrome_no_suffix(self):
        """
        Test Case 7: A simple non-palindrome where the longest palindromic suffix
        is just the last character.
        'abcd' -> 'abcdcba' (longest palindromic suffix is 'd')
        """
        self.assertEqual(make_palindrome('abcd'), 'abcdcba')

    def test_two_character_non_palindrome(self):
        """
        Test Case 8: A two-character non-palindrome.
        'xy' -> 'xyx' (longest palindromic suffix is 'y')
        """
        self.assertEqual(make_palindrome('xy'), 'xyx')

    def test_longer_non_palindrome_no_complex_suffix(self):
        """
        Test Case 9: A longer non-palindrome where the longest palindromic suffix
        is just the last character.
        'hello' -> 'hellolleh' (longest palindromic suffix is 'o')
        """
        self.assertEqual(make_palindrome('hello'), 'hellolleh')

    def test_complex_prefix_with_single_char_suffix(self):
        """
        Test Case 10: A string with a somewhat complex prefix before a
        single-character palindromic suffix.
        'google' -> 'googlelgoog' (longest palindromic suffix is 'e')
        """
        self.assertEqual(make_palindrome('google'), 'googlelgoog')

if __name__ == '__main__':
    # To run these tests, you would typically have the make_palindrome function
    # defined in the same file or imported. For example:

    # def is_palindrome(s: str) -> bool:
    #     return s == s[::-1]

    # def make_palindrome(string: str) -> str:
    #     if not string:
    #         return ""
    #
    #     longest_palindrome_suffix_len = 0
    #     for i in range(len(string)):
    #         suffix = string[i:]
    #         if is_palindrome(suffix):
    #             longest_palindrome_suffix_len = len(suffix)
    #             break
    #
    #     # The prefix that needs to be reversed and appended
    #     prefix_to_reverse = string[:-longest_palindrome_suffix_len]
    #
    #     return string + prefix_to_reverse[::-1]

    unittest.main(argv=['first-arg-is-ignored'], exit=False)

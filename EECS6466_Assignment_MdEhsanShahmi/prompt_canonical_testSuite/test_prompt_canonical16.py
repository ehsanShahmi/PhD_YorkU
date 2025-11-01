
import unittest

def count_distinct_characters(string: str) -> int:
    """
    Counts the number of distinct characters in a given string, treating
    uppercase and lowercase versions of the same letter as the same character.
    Spaces, numbers, and symbols are counted as distinct characters.

    For example:
    - count_distinct_characters('xyzXYZ') == 3 ('x', 'y', 'z')
    - count_distinct_characters('Jerry') == 4 ('j', 'e', 'r', 'y')
    - count_distinct_characters('') == 0
    - count_distinct_characters('AaA') == 1
    """
    return len(set(string.lower()))


# IMPORTANT: As per the prompt's instruction, the function 'count_distinct_characters'
# is NOT defined here. These test cases assume 'count_distinct_characters' would be
# imported or available in the global scope when this test suite is executed.
# If you run this file directly, it will result in a NameError because the function
# is not defined within this file.

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string, expecting 0 distinct characters."""
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        """Test with a string containing a single character, expecting 1."""
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_all_same_characters_case_insensitive(self):
        """Test with characters that are identical when case is ignored."""
        self.assertEqual(count_distinct_characters('aAaAaA'), 1)

    def test_mixed_case_distinct_from_prompt_example_1(self):
        """Test case directly from the prompt's first example."""
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)

    def test_mixed_case_distinct_from_prompt_example_2(self):
        """Test case directly from the prompt's second example."""
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_all_distinct_alphabetic_characters_mixed_case(self):
        """Test with a string containing all 26 distinct letters (lowercase and uppercase)."""
        self.assertEqual(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

    def test_string_with_repeats_and_mixed_case(self):
        """Test with a longer word containing repeats and mixed casing."""
        # 'P', 'r', 'o', 'g', 'a', 'm', 'i', 'n' -> 8 distinct (case-insensitive)
        self.assertEqual(count_distinct_characters('Programming'), 8)

    def test_with_spaces_and_special_characters(self):
        """Test with a string including spaces, punctuation, and letters."""
        # 'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd', '!' -> 9 distinct (case-insensitive)
        self.assertEqual(count_distinct_characters('hello world!'), 9)

    def test_numbers_and_symbols_only(self):
        """Test with a string consisting only of numbers and symbols, with some repeats."""
        # '1', '2', '3', '!', '@', '#' -> 6 distinct
        self.assertEqual(count_distinct_characters('123!@#112'), 6)

    def test_unicode_characters(self):
        """Test with a string containing distinct Unicode characters."""
        # '你好世界你好' should yield '你', '好', '世', '界' -> 4 distinct
        self.assertEqual(count_distinct_characters('你好世界你好'), 4)

if __name__ == '__main__':
    # To run these tests successfully, you would typically have the
    # 'count_distinct_characters' function imported from another module, e.g.:
    # from your_solution_file import count_distinct_characters

    # As the function is not defined here (per instructions), running this
    # will result in a NameError. This block is included for standard unittest format.
    unittest.main()

#```python
import unittest
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Given a string representing a piece of music, return a list of integers
    where each integer represents the duration of a note in beats.

    The music string is a sequence of note representations separated by spaces.
    Each note can be one of the following:
    - 'o': A whole note, duration 4 beats.
    - 'o|': A half note, duration 2 beats.
    - '.|': A quarter note, duration 1 beat.

    If the input string is empty, return an empty list.
    Invalid note representations or malformed strings are not expected.

    For example:
    parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    parse_music('o') == [4]
    parse_music('') == []
    parse_music('o| .|') == [2, 1]
    """
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]

class TestParseMusic(unittest.TestCase):

    def test_01_docstring_example(self):
        """Test case from the function's docstring."""
        music_string = 'o o| .| o| o| .| .| .| .| o o'
        expected_beats = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_02_empty_string(self):
        """Test with an empty input string."""
        music_string = ''
        expected_beats = []
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_03_single_whole_note(self):
        """Test with a single whole note."""
        music_string = 'o'
        expected_beats = [4]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_04_single_half_note(selfself):
        """Test with a single half note."""
        music_string = 'o|'
        expected_beats = [2]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_05_single_quarter_note(self):
        """Test with a single quarter note."""
        music_string = '.|'
        expected_beats = [1]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_06_all_whole_notes(self):
        """Test a sequence consisting only of whole notes."""
        music_string = 'o o o o o'
        expected_beats = [4, 4, 4, 4, 4]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_07_all_half_notes(self):
        """Test a sequence consisting only of half notes."""
        music_string = 'o| o| o|'
        expected_beats = [2, 2, 2]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_08_all_quarter_notes(self):
        """Test a sequence consisting only of quarter notes."""
        music_string = '.| .| .| .| .| .|'
        expected_beats = [1, 1, 1, 1, 1, 1]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_09_mixed_short_sequence(self):
        """Test a short, mixed sequence of different note types."""
        music_string = 'o .| o|'
        expected_beats = [4, 1, 2]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_10_complex_mixed_sequence_with_repetition(self):
        """Test a longer, complex mixed sequence with repeated patterns."""
        music_string = '.| o o| .| o o| .| o o|'
        expected_beats = [1, 4, 2, 1, 4, 2, 1, 4, 2]
        self.assertEqual(parse_music(music_string), expected_beats)

# This is the standard boilerplate to run the tests.
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
#```
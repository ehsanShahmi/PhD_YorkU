#python
import unittest
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Given a string of nested parentheses, parse it into a list of integers
    where each integer represents the maximum nesting depth of a group of parentheses.

    A group of parentheses is separated by spaces.
    An empty string or a string with only spaces should return an empty list.

    For example:
    parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    """
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

# IMPORTANT:
# The 'parse_nested_parens' function is assumed to be defined elsewhere
# and available in the scope where these tests are executed, typically via an import.
# For example, if your solution is in a file named 'solution.py', you would
# uncomment the following line:
# from solution import parse_nested_parens
#
# As per the instructions, the implementation of 'parse_nested_parens'
# is NOT provided in this file. If you run this test suite directly
# without 'parse_nested_parens' being defined or imported, it will result
# in a NameError.
#
# For demonstration purposes or to make this file runnable without
# the actual solution, you could temporarily define a placeholder:
# def parse_nested_parens(paren_string: str) -> List[int]:
#    raise NotImplementedError("parse_nested_parens is not implemented in this test file.")

class TestParseNestedParens(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertEqual(parse_nested_parens(''), [])

    def test_string_with_only_spaces(self):
        """Test with an input string containing only spaces."""
        self.assertEqual(parse_nested_parens('   '), [])

    def test_single_group_level_one(self):
        """Test a single group with one level of nesting."""
        self.assertEqual(parse_nested_parens('()'), [1])

    def test_single_group_level_two(self):
        """Test a single group with two levels of nesting."""
        self.assertEqual(parse_nested_parens('(())'), [2])

    def test_single_group_level_three(self):
        """Test a single group with three levels of nesting."""
        self.assertEqual(parse_nested_parens('((()))'), [3])

    def test_docstring_example(self):
        """Test the example provided in the function's docstring."""
        # '(()()) ((())) () ((())()())' -> [2, 3, 1, 3]
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_multiple_groups_all_level_one(self):
        """Test multiple groups, each with one level of nesting."""
        self.assertEqual(parse_nested_parens('() () ()'), [1, 1, 1])

    def test_multiple_groups_mixed_simple(self):
        """Test multiple groups with increasing simple nesting levels."""
        self.assertEqual(parse_nested_parens('() (()) ((()))'), [1, 2, 3])

    def test_complex_single_group_with_branches(self):
        """Test a single complex group with branching parentheses."""
        # (()())(()) has 3 levels: outer, then ( ()() ) and ( (()) )
        # Max of ( ()() ) is 2, Max of ( (()) ) is 3. Max of whole is 3.
        self.assertEqual(parse_nested_parens('((()())(()))'), [3])

    def test_more_complex_and_longer_input(self):
        """Test a longer input string with varied and complex groups."""
        self.assertEqual(parse_nested_parens('(()()) (((())))(())(()) ()'), [2, 4, 2, 2, 1])

# This allows the test suite to be run directly from the command line
if __name__ == '__main__':
    unittest.main()

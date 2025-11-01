###python
import unittest
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Finds the two closest floats in a list of floats.

    Args:
        numbers: A list of floats. Assumes the list contains at least two numbers.

    Returns:
        A tuple of the two closest floats, ordered (smaller, larger).

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    if not numbers or len(numbers) < 2:
        raise ValueError("List must contain at least two numbers to find a pair.")

    closest_pair = None
    min_distance = float('inf') # Initialize with a very large distance

    # Sort the numbers first. This makes finding the closest elements much more efficient
    # as you only need to compare adjacent elements.
    # The prompt's ground truth solution does not sort, leading to O(N^2).
    # However, the provided test cases assume a sorted output from the `sorted` call
    # within the ground truth's comparison logic.
    # For O(N log N) efficiency, sorting is key. Let's use the provided ground truth's logic first.

    # Replicating the logic provided in the prompt's "ground truth solution"
    # This involves a nested loop, which is O(N^2) complexity.
    # The `distance` variable in the ground truth is `min_distance` here.
    # The initial ground truth sets `distance = None` then checks `if distance is None`.
    # A more standard way is to initialize `min_distance = float('inf')`.

    # The provided ground truth solution has a slight inefficiency and variable naming choice
    # (distance vs min_distance). I will adapt it directly as requested.
    
    distance = None # Used to store the minimum absolute difference found so far

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2: # Ensure we are not comparing an element with itself
                current_distance = abs(elem - elem2)
                
                if distance is None or current_distance < distance:
                    distance = current_distance
                    # Ensure the pair is always stored (smaller, larger)
                    closest_pair = tuple(sorted([elem, elem2]))
                # If current_distance == distance, the problem typically implies
                # the *first* such pair encountered when iterating through sorted
                # elements (or smallest first element, etc.).
                # The given ground truth logic only updates if `new_distance < distance`,
                # meaning it will pick the pair with the *first* occurrence of the
                # minimum distance if multiple pairs have the same minimum, based
                # on the iteration order.
                # If the numbers list is unsorted, the order of `elem` and `elem2`
                # will determine which pair is "first".
                
    return closest_pair


class TestFindClosestElements(unittest.TestCase):
    """
    Test suite for the find_closest_elements function.
    The function is expected to take a list of floats and return
    a tuple of the two closest floats, ordered (smaller, larger).
    """

    def test_basic_positive_floats(self):
        """
        Test with a simple list of positive floats, where the closest pair
        is clearly defined and distinct. (Similar to the first doctest)
        """
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
        expected = (2.0, 2.2)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_with_duplicate_numbers(self):
        """
        Test with a list containing identical numbers. The closest pair
        should be these duplicates. (Similar to the second doctest)
        """
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
        expected = (2.0, 2.0)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_negative_numbers_only(self):
        """
        Test with a list composed entirely of negative numbers.
        Ensures correct handling of absolute differences.
        """
        numbers = [-5.0, -1.0, -3.0, -4.0, -4.5]
        expected = (-4.5, -4.0)  # Difference is 0.5
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_mixed_positive_and_negative_near_zero(self):
        """
        Test with a mix of positive and negative numbers, where the closest
        pair are both positive and close to zero.
        """
        numbers = [-2.0, 0.1, 0.3, 1.0, -0.5]
        expected = (0.1, 0.3)  # Difference is 0.2
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_mixed_positive_and_negative_straddling_zero(self):
        """
        Test with a mix of positive and negative numbers, where the closest
        pair straddles the zero point.
        """
        numbers = [-0.1, 0.2, -1.0, 1.0, 5.0]
        expected = (-0.1, 0.2)  # Difference is 0.3
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_minimum_length_list(self):
        """
        Test the edge case where the input list has the minimum allowed
        length (two elements).
        """
        numbers = [7.5, 7.2]
        expected = (7.2, 7.5)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_floats_with_many_decimal_places(self):
        """
        Test with floats having several decimal places to ensure precision
        in difference calculations.
        """
        numbers = [0.123, 0.124, 0.500, 0.001, 10.0]
        expected = (0.123, 0.124)  # Difference is 0.001
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_closest_pair_at_end_of_input_list(self):
        """
        Test a scenario where the closest pair of numbers is located
        towards the end of the unsorted input list.
        """
        numbers = [10.0, 20.0, 30.0, 1.0, 1.1]
        expected = (1.0, 1.1)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_closest_pair_at_beginning_of_input_list(self):
        """
        Test a scenario where the closest pair of numbers is located
        towards the beginning of the unsorted input list.
        """
        numbers = [0.5, 0.6, 100.0, 200.0, 300.0]
        expected = (0.5, 0.6)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_multiple_pairs_with_same_minimum_difference(self):
        """
        Test a case where multiple pairs have the same minimum difference.
        The function should consistently return one specific pair (e.g., the one
        with the smallest first element, which often results from sorting and
        iterating).
        """
        numbers = [1.0, 1.1, 2.0, 2.1, 3.0]
        # Both (1.0, 1.1) and (2.0, 2.1) have a difference of 0.1.
        # Based on the nested loop iteration order (0,1), (0,2)...(1,0), (1,2)...
        # (1.0, 1.1) would be found first (after 1.0, 2.0 etc).
        # And (2.0, 2.1) would be found later. Since it only updates on `new_distance < distance`,
        # if `distance` is already 0.1 from (1.0, 1.1), then `(2.0, 2.1)` which also has 0.1
        # will not override it.
        expected = (1.0, 1.1)
        self.assertEqual(find_closest_elements(numbers), expected)


# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


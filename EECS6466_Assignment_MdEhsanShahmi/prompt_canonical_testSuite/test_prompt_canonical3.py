#python
import unittest
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False


class TestBelowZero(unittest.TestCase):
    """
    Test suite for the 'below_zero' function.
    """

    def test_1_all_deposits_never_below_zero(self):
        """
        Test case with only positive operations (deposits). Balance should never fall below zero.
        """
        operations = [10, 20, 30, 5]
        self.assertFalse(below_zero(operations))

    def test_2_mixed_operations_always_positive(self):
        """
        Test case with mixed deposits and withdrawals, but balance always remains positive or zero.
        """
        operations = [5, -2, 3, -1, 4]
        self.assertFalse(below_zero(operations))

    def test_3_balance_drops_below_zero_mid_sequence(self):
        """
        Test case where the balance clearly drops below zero at one point.
        Example from the prompt.
        """
        operations = [1, 2, -4, 5]
        self.assertTrue(below_zero(operations))

    def test_4_balance_reaches_zero_then_positive(self):
        """
        Test case where the balance drops to exactly zero, but then recovers without going negative.
        """
        operations = [10, -5, -5, 3, 2]
        self.assertFalse(below_zero(operations))

    def test_5_balance_reaches_zero_then_negative(self):
        """
        Test case where the balance drops to exactly zero, and then immediately goes negative.
        """
        operations = [10, -5, -5, -1, 4]
        self.assertTrue(below_zero(operations))

    def test_6_large_initial_deposit_then_large_withdrawal_causes_negative(self):
        """
        Tests if a large initial deposit can still be overcome by subsequent large withdrawals.
        """
        operations = [100, -50, -60, 20]  # Balance: 100 -> 50 -> -10 (True)
        self.assertTrue(below_zero(operations))

    def test_7_large_initial_deposit_then_large_withdrawal_stays_positive(self):
        """
        Tests if a large initial deposit correctly prevents the balance from going negative
        despite significant withdrawals.
        """
        operations = [100, -50, -40, -5]  # Balance: 100 -> 50 -> 10 -> 5 (False)
        self.assertFalse(below_zero(operations))

    def test_8_empty_operations_list(self):
        """
        Test case with an empty list of operations. Balance remains at zero.
        """
        operations = []
        self.assertFalse(below_zero(operations))

    def test_9_multiple_consecutive_negative_operations(self):
        """
        Test case with several consecutive withdrawals leading to a negative balance.
        """
        operations = [10, -2, -3, -6, 1]  # Balance: 10 -> 8 -> 5 -> -1 (True)
        self.assertTrue(below_zero(operations))

    def test_10_first_operation_is_negative(self):
        """
        Test case where the very first operation is a withdrawal, immediately making the balance negative.
        """
        operations = [-5, 10, -2]  # Balance: -5 (True)
        self.assertTrue(below_zero(operations))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

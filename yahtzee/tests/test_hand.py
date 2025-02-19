#!/usr/bin/env python3
""" Module for testing the class Die """

import unittest
import random
from src.hand import Hand


class TestDie(unittest.TestCase):
    """
    Test cases for the hand module.
    """

    def test_hand_without_value(self):
        """Test creating a Hand object without passing any arguments to the constructor."""
        random.seed(1)
        hand = Hand()
        # Ceheck five dice
        self.assertEqual(len(hand.dice), 5)
        self.assertEqual(hand.to_list(), [2, 5, 1, 3, 1])

    def test_hand_with_value_to_list(self):
        """Test creating a Hand object by passing a list of dice values to the constructor
        and verifying that the to_list() method returns the correct list of values."""
        hand = Hand([3, 5, 2, 6, 1])

        # Verify that to_list() returns the correct list of dice values
        self.assertEqual(hand.to_list(), [3, 5, 2, 6, 1])


if __name__ == "__main__":
    unittest.main()

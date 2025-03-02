#!/usr/bin/env python3
""" Module for testing the Hand Class """

import unittest
import random
from src.hand import Hand


class TestHand(unittest.TestCase):
    """
    Test cases for the hand module.
    """

    def test_hand_without_value(self):
        """Test creating a Hand object without passing any arguments to the constructor."""
        random.seed(1)
        hand = Hand()
        # Ceheck five dice
        self.assertEqual(hand.to_list(), [2, 5, 1, 3, 1])

    def test_hand_size(self):
        """Test that the Hand contains the correct number of dice."""
        random.seed(1)
        hand = Hand()

        # Check if the hand has 5 dice
        self.assertEqual(len(hand.dice), 5)

    def test_roll_in_range(self):
        """Test that after rolling, all dice values are within the valid range (1-6)."""
        random.seed(4)
        hand = Hand([1, 2, 3, 4, 5])
        hand.roll()

        # Check if dice values are within the valid range
        for die in hand.dice:
            self.assertGreaterEqual(die.get_value(), 1)
            self.assertLessEqual(die.get_value(), 6)

    def test_hand_with_value_to_list(self):
        """Test creating a Hand object by passing a list of dice values to the constructor
        and verifying that the to_list() method returns the correct list of values."""
        hand = Hand([3, 5, 2, 6, 1])

        # Verify that to_list() returns the correct list of dice values
        self.assertEqual(hand.to_list(), [3, 5, 2, 6, 1])

    def test_roll_selected_dice(self):
        """Test rolling only selected dice while keeping the rest unchanged."""
        random.seed(2)
        hand = Hand([1, 2, 3, 4, 5])
        hand.roll([1, 3])
        # Verify that selected dice dint get rolled
        expected_values = [1, hand.dice[1], 3, hand.dice[3], 5]
        self.assertEqual(hand.to_list(), expected_values)

    def test_roll_all_dice(self):
        """Test rolling all dice when no argument is passed."""
        random.seed(3)
        hand = Hand([1, 2, 3, 4, 5])
        hand.roll()
        # Verify that selected all dice got rolled
        self.assertNotEqual(hand.to_list(), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()

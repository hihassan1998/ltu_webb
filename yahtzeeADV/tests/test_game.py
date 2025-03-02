#!/usr/bin/env python3
""" Module for testing the class games most critical logic """

import unittest
from src.hand import Hand
from src.scoreboard import Scoreboard


class TestDieAndScoreborad(unittest.TestCase):
    """
    Test cases for the hand module.
    """

    def test_hand_roll_to_list(self):
        """Test that to_list() returns the correct values and roll() changes only unindexed dice."""
        dice_values = [1, 2, 3, 4, 5]
        print("uncontrolled hand:", dice_values)
        hand = Hand(dice_values)
        # Roll dice at index 0 and 1
        hand.roll([2, 3])
        new_dice_values = hand.to_list()
        print("Controlled hand", new_dice_values)

        # check if the new dice values are changed
        self.assertNotEqual(new_dice_values[2], dice_values[2])
        self.assertNotEqual(new_dice_values[3], dice_values[3])

        # check if the older dice values remain same
        self.assertEqual(new_dice_values[0], dice_values[0])
        self.assertEqual(new_dice_values[1], dice_values[1])
        self.assertEqual(new_dice_values[4], dice_values[4])

    def test_roll_of_all_dice(self):
        """
        Test that rolling all dice without arguments changes all dice so even if,
        test_hand_roll_to_list fails we are sure the dice are rolling.
        """
        # Sending in dice values
        dice_values = [1, 2, 3, 4, 5]
        hand = Hand(dice_values)
        hand.roll()

        rolled_values = hand.to_list()

        # Check, all dice have changed
        self.assertNotEqual(rolled_values, dice_values)

    def test_add_points(self):
        """
        Test that points are correctly added for a rule and
        that the correct exception is raised on second attempt of adding the points to that rule.
        """
        scoreboard = Scoreboard()  # Creating an instance inside the test
        hand = Hand([1, 2, 3, 4, 5])
        scoreboard.add_points("Large Straight", hand)
        desired_point = 40

        # check if points are added on first try
        self.assertEqual(scoreboard.get_points(
            'Large Straight'), desired_point)

        # check if points are added on second try , should  raise a ValueError
        with self.assertRaises(ValueError):
            scoreboard.add_points("Large Straight", hand)


if __name__ == "__main__":
    unittest.main()

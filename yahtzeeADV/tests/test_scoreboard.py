#!/usr/bin/env python3
""" Module for testing the Scoreboard Class """

import unittest
from src.hand import Hand
from src.scoreboard import Scoreboard
from src.rules import Ones, Twos


class TestScoreboard(unittest.TestCase):
    """
    Test cases for the scoreboard module.
    """

    def test_add_points(self):
        """
        Test that points are correctly added for a rule and
        that the correct exception is raised on second attempt of adding the points to that rule.
        """
        scoreboard = Scoreboard()  # Creating an instance inside the test
        hand = Hand([1, 2, 3, 4, 5])
        scoreboard.add_points("Large Straight", hand)
        expected_points = 40

        # if points added on first try
        self.assertEqual(scoreboard.get_points(
            'Large Straight'), expected_points)

        # if points are added on second try , should  raise a ValueError
        with self.assertRaises(ValueError):
            scoreboard.add_points("Large Straight", hand)

    def test_get_total_points(self):
        """Test that get_total_points returns the correct sum of assigned points."""
        scoreboard = Scoreboard()
        hand = Hand([1, 1, 1, 2, 2])

        scoreboard.add_points("Ones", hand)
        scoreboard.add_points("Twos", hand)
        # print('first score for Ones: ',Ones().points(hand))
        # print('Second score for twos: ',Twos().points(hand))
        expected_points = Ones().points(hand) + Twos().points(hand)
        # Check if results are as expected
        self.assertEqual(scoreboard.get_total_points(), expected_points)


if __name__ == "__main__":
    unittest.main()

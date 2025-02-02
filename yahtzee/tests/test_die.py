#!/usr/bin/env python3
""" Module for testing the class Die """

import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    def test_die_with_value(self):
        """Testing that the die gives prdicted/seeded values"""
        die = Die(4)
        self.assertEqual(die.get_value(), 4)

    def test_less_than_min_val(self):
        """Testing that the die stays in the range of possible outcomes. (Min_val)"""
        die = Die(0)
        self.assertEqual(die.get_value(), Die.MIN_ROLL_VALUE)

    def test_more_than_max_val(self):
        """Testing that the die stays in the range of possible outcomes. (Max_val)"""
        die = Die(100)
        self.assertEqual(die.get_value(), Die.MAX_ROLL_VALUE)

    def test_random_roll(self):
        """Testing that rolling the die changes its value."""
        die = Die(3)
        initial_value = die.get_value()
        die.roll()
        self.assertNotEqual(die.get_value(), initial_value)

    def test_get_name(self):
        """Testing that die;s names match its value."""
        die = Die(1)
        self.assertEqual(die.get_name(), "one")
        die = Die(2)
        self.assertEqual(die.get_name(), "two")
        die = Die(3)
        self.assertEqual(die.get_name(), "three")
        die = Die(4)
        self.assertEqual(die.get_name(), "four")
        die = Die(6)
        self.assertEqual(die.get_name(), "six")
    
    def test_die_without_value(self):
        """Testing that the die gives prdicted/seeded values without entering a value to the call"""
        random.seed(1)
        die = Die()
        self.assertEqual(die.get_value(), 2)

if __name__ == "__main__":
    unittest.main()

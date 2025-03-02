#!/usr/bin/env python3
"""
This module contains the Die class.

The Die class represents a single die that can be rolled to generate random values between 1 and 6.
It also provides methods to get the value and name of the die and
to roll the die again with a new random value.
"""
import random


class Die:
    """
    Represents a single die, with methods to get its value, roll it, and get its name.
    """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6

    def __init__(self, value=None):
        """
        Initializes a die with a random value between 1 and 6, or a specific value.

        Args:
            value (int, optional): The value of the die. Defaults to None.
        """
        if value is None:
            self._value = random.randint(
                self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        elif value > self.MAX_ROLL_VALUE:
            self._value = self.MAX_ROLL_VALUE
        elif value < self.MIN_ROLL_VALUE:
            self._value = self.MIN_ROLL_VALUE
        else:
            self._value = value

    def get_name(self):
        """
        Returns the name of the die based on its value.

        Returns:
            str: The name corresponding to the die’s value (e.g., 1 = 'one', 2 = 'two', etc.).
        """
        names = ["one", "two", "three", "four", "five", "six"]
        return names[self._value - 1]

    def get_value(self):
        """
        Returns the current value of the die.

        Returns:
            int: The die's value between 1 and 6.
        """
        return self._value

    def roll(self):
        """
        Rolls the die and assigns it a new random value between 1 and 6.
        """
        self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)

    def __eq__(self, other):
        """
        Compares this Die object with another Die object or an integer.
        Args:
            other (Die or int): The object to compare with.

        Returns:
            bool: True if values are the same, False otherwise.
        """
        if isinstance(other, Die):
            return self._value == other._value
        if isinstance(other, int):
            return self._value == other
        return False

    def __str__(self):
        """
        Returns a string representation of the die’s value.

        Returns:
            str: The string representation of the die's value.
        """
        return str(self._value)

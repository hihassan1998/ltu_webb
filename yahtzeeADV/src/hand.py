#!/usr/bin/env python3
"""
This module contains the Hand class.

The Hand class represents a collection of dice, which can be rolled together or individually.
It provides methods to roll the dice and display the results,
as well as to represent the hand of dice as a string.
"""
from src.die import Die


class Hand:
    """
    Represents a hand of dice. It can create a hand of 5 dice, roll the dice, 
    and return a string representation of the hand.

    Attributes:
        dice (list): A list of Die objects representing the dice in the hand.
    """

    def __init__(self, dice_values=None):
        """
        Initializes a hand of dice.

        Args:
            dice_values (list, optional): A list of values to initialize the dice. Defaults to None.
        """
        self.dice = []
        if dice_values is None:
            for _ in range(5):
                self.dice.append(Die())
        else:
            for value in dice_values:
                self.dice.append(Die(value))

        # Print the dice values right after initialization
        # amke changes here to not initalize with diffrent hands on every press of button to  roll
        # Make changes to store values of the dice Server Side e.g; in the app.py
        # print("Initial dice values: ", self.to_list())

    def roll(self, indexes=None):
        """
        Rolls the dice in the hand.

        Args:
            indexes (list, optional): A list of indexes of the dice to roll. Defaults to None.
        """
        if indexes is None:
            for die in self.dice:
                die.roll()
        else:
            for index in indexes:
                self.dice[index].roll()
        # Printing the list of dice values after the roll
        # print("Dice values after rolling: ", self.to_list())

    def to_list(self):
        """
        Returns a list of values for each die in the hand.

        Returns:
            list: A list of integers representing the dice values.
        """
        dice_values = []
        for die in self.dice:
            dice_values.append(die.get_value())
        return dice_values

    def __str__(self):
        """
        Returns a string representation of the hand of dice.

        Returns:
            str: A comma-separated string of each die in the hand.
        """
        die_strings = []

        for die in self.dice:
            die_strings.append(str(die))
        return ", ".join(die_strings)

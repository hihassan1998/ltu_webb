#!/usr/bin/env python3
"""
This module contains the Rule classes.

The Rule classes representsthe rules to calculate the score accived,
according to any one of the subclasses and rules of the yahtzee game.

"""
from abc import ABC, abstractmethod
from src.hand import Hand


class Rule(ABC):
    """Base class for all Yahtzee rules."""

    def __init__(self, name=""):
        """
        Initializes the base class with an empty name.
        """
        self.name = name

    @abstractmethod
    def points(self, hand: Hand) -> int:
        """
        Calculate the score for this rule based on the given hand of dice.
        Args:
            hand (Hand): The hand of dice to evaluate.
        Returns:
            int: The calculated score for this rule.
        """
        raise NotImplementedError("Subclasses implement this method")

    def __str__(self):
        """Return a string representation of the rule."""
        return f"Rule: {self.name}"


class SameValueRule(Rule):
    """
    Represents rules that count occurrences of a specific value in the dice hand.
    """

    def __init__(self, value, name):
        """
        Initializes the rule with a specific value and name.

        Args:
            value (int): The dice value to count.
            name (str): The name of the rule.
        """
        super().__init__()
        self.value = value
        self.name = name

    def points(self, hand):
        """
        Counts the occurrences of the specific value in the hand and calculates the score.

        Args:
            hand (Hand): The hand to evaluate.

        Returns:
            int: The calculated score.
        """
        count = hand.to_list().count(self.value)
        if count > 0:
            return count * self.value
        return 0


class Ones(SameValueRule):
    """Rule for scoring Ones (1s) in Yahtzee."""

    def __init__(self):
        """Initializes the Ones rule with value 1."""
        super().__init__(1, "Ones")
        self.name = "Ones"


class Twos(SameValueRule):
    """Rule for scoring Twos (2s) in Yahtzee."""

    def __init__(self):
        """Initializes the Twos rule with value 2."""
        super().__init__(2, "Twos")
        self.name = "Twos"


class Threes(SameValueRule):
    """Rule for scoring Twos (3s) in Yahtzee."""

    def __init__(self):
        """Initializes the Threes rule with value 3."""
        super().__init__(3, "Threes")
        self.name = "Threes"


class Fours(SameValueRule):
    """Rule for scoring Fours (4s) in Yahtzee."""

    def __init__(self):
        """Initializes the Fours rule with value 4."""
        super().__init__(4, "Fours")
        self.name = "Fours"


class Fives(SameValueRule):
    """Rule for scoring Fives (5s) in Yahtzee."""

    def __init__(self):
        """Initializes the Fives rule with value 5."""
        super().__init__(5, "Fives")
        self.name = "Fives"


class Sixes(SameValueRule):
    """Rule for scoring sixes (6s) in Yahtzee."""

    def __init__(self):
        """Initializes the Sixes rule with value 6."""
        super().__init__(6, "Sixes")
        self.name = "Sixes"


class ThreeOfAKind(Rule):
    """Rule for scoring Three of a Kind in Yahtzee."""

    def __init__(self):
        """Initializes the Three of a Kind rule."""
        super().__init__()
        self.name = "Three Of A Kind"

    def points(self, hand):
        """
        Checks if there are three of the same value and returns the sum of the hand.

        Args:
            hand (Hand): The hand to evaluate.

        Returns:
            int: The sum of the hand if three of the same value exist, otherwise 0.
        """
        values = hand.to_list()
        for value in set(values):
            if values.count(value) >= 3:
                return sum(values)
        return 0


class FourOfAKind(Rule):
    """Rule for scoring Four of a Kind in Yahtzee."""

    def __init__(self):
        """Initializes the Four of a Kind rule."""
        super().__init__()
        self.name = "Four Of A Kind"

    def points(self, hand):
        """
        Checks if there are four of the same value and returns the sum of the hand.

        Args:
            hand (Hand): The hand to evaluate.

        Returns:
            int: The sum of the hand if four of the same value exist, otherwise 0.
        """
        values = hand.to_list()
        for value in set(values):
            if values.count(value) >= 4:
                return sum(values)
        return 0


class FullHouse(Rule):
    """Rule for scoring a Full House in Yahtzee."""

    def __init__(self):
        """Initializes the Full House rule."""
        super().__init__()
        self.name = "Full House"

    def points(self, hand):
        """
        Checks if the hand is a Full House (three of one value and two of another).

        Args:
            hand (Hand): The hand to evaluate.

        Returns:
            int: 25 if Full House, otherwise 0.
        """
        values = hand.to_list()
        unique_values = set(values)
        if len(unique_values) == 2 and (values.count(values[0]) in [2, 3]):
            return 25
        return 0


class SmallStraight(Rule):
    """Rule for scoring a Small Straight in Yahtzee."""

    def __init__(self):
        """Initializes the Small Straight 
        rule."""
        super().__init__()
        self.name = "Small Straight"

    def points(self, hand):
        """
        Checks if the hand contains a Small Straight (sequence of four consecutive numbers).

        Args:
            hand (Hand): The hand to evaluate.

        Returns:
            int: 30 if Small Straight, otherwise 0.
        """
        values = set(hand.to_list())
        straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
        for straight in straights:
            if straight.issubset(values):
                return 30
        return 0


class LargeStraight(Rule):
    """Rule for scoring a Large Straight in Yahtzee."""

    def __init__(self):
        """Initializes the Large Straight rule."""
        super().__init__()
        self.name = "Large Straight"

    def points(self, hand):
        """
        Checks if the hand contains a Large Straight (sequence of five consecutive numbers).

        Args:
            hand (Hand): The hand to evaluate.

        Returns:
            int: 40 if Large Straight, otherwise 0.
        """
        values = set(hand.to_list())
        if values in [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]:
            return 40
        return 0


class Yahtzee(Rule):
    """Rule for scoring Yahtzee in Yahtzee."""

    def __init__(self):
        """Initializes the Yahtzee rule."""
        super().__init__()
        self.name = "Yahtzee"

    def points(self, hand):
        """
        Checks if all dice in the hand have the same value (Yahtzee) and returns 50 points.

        Args:
            hand (Hand): The hand to evaluate.

        Returns:
            int: 50 points if all dice are the same, otherwise 0.
        """
        # values = hand.to_list()
        values = set(hand.to_list())

        if len(values) == 1:
            return 50

        # if len(set(values)) == 1:  # All dice have the same value
        #     return 50
        return 0


class Chance(Rule):
    """Rule for scoring Chance in Yahtzee."""

    def __init__(self):
        """Initializes the Chance rule."""
        super().__init__()
        self.name = "Chance"

    def points(self, hand):
        """
        Returns the sum of the dice in the hand for the Chance rule.

        Args:
            hand (Hand): The hand to evaluate.

        Returns:
            int: The sum of all dice values in the hand.
        """
        return sum(hand.to_list())

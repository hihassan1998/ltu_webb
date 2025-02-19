#!/usr/bin/env python3
"""
This module contains the Scoreboard class.

The Scoreboard class is responsible for tracking the scores of different rules in the Yahtzee game.
It provides methods for calculating the total points,
adding points based on specific rules, and checking if the game is finished.
The class also allows for creating a Scoreboard object from a dictionary of rule names and scores.
"""
# from src.hand import Hand
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes, Chance, Yahtzee
from src.rules import ThreeOfAKind, FourOfAKind, FullHouse, SmallStraight, LargeStraight


class Scoreboard:
    """A class to represent the scoreboard of the game."""

    def __init__(self):
        """
        Constructor for the Scoreboard.
        Tracks points for each rule. -1 indicates the rule hasn't been used yet.
        """
        self._scores = {
            "Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
            "ThreeOfAKind": -1, "FourOfAKind": -1, "FullHouse": -1, "SmallStraight": -1,
            "LargeStraight": -1, "Chance": -1, "Yahtzee": -1
        }
        self._hand = None

    @property
    def rules_and_scores_dict(self):
        """Property to access the scores for each game rule."""
        return self._scores

    def get_total_points(self, hand=None):
        """
        Returns the sum of all assigned points without modifying the scoreboard.

        Args:
            hand (Hand): The current hand of dice,
            which is used to calculate the points for each rule.

        Returns:
            int: The total sum of all assigned points.
        """
        if hand is None:
            hand = self._hand

        total_points = 0
        self.add_points(None, hand)
        for _, score in self._scores.items():
            if score != -1:
                total_points += score
        return total_points

    def add_points(self, hand_rule, hand, force_replace=False):
        """

        Add points for each rule based on the current hand.

        Args:
            hand_rule (Rule): The rule to apply to the current hand, used to calculate points.

            hand (Hand): The current hand of dice, used to calculate points for each rule.

            force_replace (bool, optional): If True, previous assigned points will be replaced.
            Defaults to False.
        """
        if hand_rule is None:
            return
        if hand is None:
            return

        rules = [Ones(), Twos(), Threes(), Fours(), Fives(), Sixes(),
                 ThreeOfAKind(), FourOfAKind(), FullHouse(), SmallStraight(),
                 LargeStraight(), Chance(), Yahtzee()]

        for rule in rules:
            if rule.name == hand_rule:
                score = rule.points(hand)
                # print(f"Applying rule: {hand_rule}, Score: {score}")
                if self.get_points(hand_rule) != -1 and not force_replace:
                    raise ValueError(
                        f"Points for {hand_rule} are already assigned.")
                if score != -1:
                    self._scores[hand_rule] = score
                    # print(f"Updated score for {hand_rule}: {score}")
                return

        raise ValueError(f"Invalid rule: {hand_rule}")

    def get_points(self, rule_name):
        """
        Returns the points for a specific rule. If the rule has no points, -1 is returned.
        Args:
            rule_name (str): The name of the rule to fetch the score for.

        Returns:
            int: The score for the rule, or -1 if the rule has no points assigned.
        """
        return self._scores.get(rule_name, -1)

    def finished(self):
        """
        Returns True if all rules have points, otherwise False.
        Returns:
            bool: True if all rules have been scored, otherwise False.
        """
        for points in self._scores.values():
            if points == -1:
                return False
            if points == 0:
                return True
        return True

    @classmethod
    def from_dict(cls, points):
        """
        Creates a Scoreboard object from a dictionary of rules and points.
        Args:
            points (dict): A dictionary where the keys are rule names and
            the values are the scores for those rules.

        Returns:
            Scoreboard: A new Scoreboard object populated with the provided scores.
        """
        scoreboard = cls()
        for rule_name, score in points.items():
            if rule_name in scoreboard._scores:
                scoreboard._scores[rule_name] = score
        return scoreboard

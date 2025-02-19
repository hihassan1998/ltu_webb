#!/usr/bin/env python3
"""
This module contains the helper functions for the game logic.

"""
from src.hand import Hand


def initialize_session(session):
    """Initialize session variables if not already set."""
    if 'hand' not in session:
        session['hand'] = Hand().to_list()
        session['roll_counter'] = 0
        session['used_rules'] = []
        session['used_rules_scores'] = {}


def update_scores(hand, rules, scoreboard, session):
    """Calculate the scores for each rule and update the scoreboard."""
    scores = scoreboard.rules_and_scores_dict
    for rule in rules:
        rule_name = rule.name.replace(' ', '')
        if rule_name not in session['used_rules']:
            score = rule.points(hand)
            scores[rule_name] = score
    scoreboard.from_dict(scores)

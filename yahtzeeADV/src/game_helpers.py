#!/usr/bin/env python3
"""
This module contains the helper functions for the game logic.

"""
from pathlib import Path
from src.hand import Hand
from src.leaderboard import Leaderboard
from flask import session
from src.queue import Queue


def initialize_session(game_session):
    """Initialize session variables if not already set."""
    if 'hand' not in session:
        game_session['hand'] = Hand().to_list()
        game_session['roll_counter'] = 0

        # Initialize player queue
        if 'players_queue' not in session:
            session['players_queue'] = Queue()

        # Initialize player_scores to track each player's used rules and scores
        if 'player_scores' not in session:
            session['player_scores'] = {
                player: {
                    'used_rules': [],  # Rules used by this player
                    'used_rules_scores': {}  # Scores for rules used by this player
                }
                for player in session['players_queue']
            }


def update_scores(hand, rules, scoreboard, game_session, current_player):
    """Calculate the scores for each rule and update the scoreboard."""
    current_player = game_session['players_queue'][0]
    # Get the current player using peek
    used_rules = game_session['player_scores'][current_player]['used_rules']

    scores = scoreboard.rules_and_scores_dict
    for rule in rules:
        rule_name = rule.name.replace(' ', '')
        if rule_name not in game_session['player_scores'][current_player]['used_rules']:
            score = rule.points(hand)
            scores[rule_name] = score
    scoreboard.from_dict(scores)


def get_leaderboard_data(game_session):
    """
    Helper function to load the leaderboard and calculate relevant data.
    """
    filename = Path("leaderboard.txt")

    # Load leaderboard
    leaderboard_obj = Leaderboard.load(filename)
    entries = leaderboard_obj.entries
    total_entries = leaderboard_obj.entries.size()
    total_points = sum(game_session['used_rules_scores'].values())
    # total_points = sum(game_session['player_scores'][current_player]['used_rules_scores'].values())
    total_points = game_session.get('total_points', 0)

    return leaderboard_obj, entries, total_entries, total_points


# def update_scores(hand, rules, scoreboard, game_session,current_player):
#     """Calculate the scores for each rule and update the scoreboard."""
#     used_rules = game_session['player_scores'][current_player]['used_rules']

#     scores = scoreboard.rules_and_scores_dict
#     for rule in rules:
#         rule_name = rule.name.replace(' ', '')
#         if rule_name not in game_session['player_scores'][current_player]['used_rules']:
#             score = rule.points(hand)
#             scores[rule_name] = score
#     scoreboard.from_dict(scores)

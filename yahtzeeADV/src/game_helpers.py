#!/usr/bin/env python3
"""
This module contains the helper functions for the game logic.

"""
from pathlib import Path
from src.hand import Hand
from src.leaderboard import Leaderboard
from flask import session
from src.queue import Queue
from src.sort import recursive_insertion


def initialize_session(game_session):
    """Initialize session variables if not already set."""
    # Redirect to select-players if players are not set

    if 'roll_counter' not in game_session:
        game_session['roll_counter'] = 0

    # Initialize session variables if not set
    if 'hand' not in game_session:
        game_session['hand'] = Hand().to_list()
        game_session['roll_counter'] = 0

        # Initialize player queue
        if 'players_queue' not in game_session:
            game_session['players_queue'] = Queue()

        # Initialize player_scores to track each player's used rules and scores
        if 'player_scores' not in game_session:
            game_session['player_scores'] = {
                player: {
                    'used_rules': [],
                    'used_rules_scores': {}
                }
                for player in game_session['players_queue']
            }

    if game_session.get("must_switch", False):
        game_session['players_queue'].append(game_session['players_queue'].pop(0))
        game_session['must_switch'] = False  # Reset switch flag
        game_session.modified = True
        # Get the current player
    players_queue = session['players_queue']
    current_player = players_queue[0] if players_queue else None
    print("Current player playing now: ", current_player)

    # Get player-specific used rules and scores
    used_rules = session['player_scores'][current_player]['used_rules']
    used_rules_scores = session['player_scores'][current_player]['used_rules_scores']
    session.modified = True
    
    
    return used_rules,used_rules_scores,current_player,players_queue

def is_game_over(players_queue, game_session, rules):
    """
    Checks if the game is over based on the rules and player progress.
    """
    for player in players_queue:
        if len(game_session['player_scores'][player]['used_rules']) != len(rules):
            return False
    return True

def update_scores(hand, rules, scoreboard, game_session, current_player):
    """Calculate the scores for each rule and update the scoreboard."""
    current_player = game_session['players_queue'][0]
    used_rules = game_session['player_scores'][current_player]['used_rules']

    scores = scoreboard.rules_and_scores_dict
    for rule in rules:
        rule_name = rule.name.replace(' ', '')
        if rule_name not in used_rules:
            score = rule.points(hand)
            scores[rule_name] = score
    scoreboard.from_dict(scores)


def get_leaderboard_data(game_session):
    """
    Helper function to load the leaderboard and calculate relevant data.
    """
    filename = Path("leaderboard.txt")
    # current_player = session['players_queue'][0] if session.get('players_queue') else None
    # if current_player:
    #     total_points = sum(session['player_scores'][current_player]['used_rules_scores'].values())
    # else:
    #     total_points = 0

    # Load leaderboard
    leaderboard_obj = Leaderboard.load(filename)
    entries = leaderboard_obj.entries
    total_entries = leaderboard_obj.entries.size()
    # total_points = sum(game_session['used_rules_scores'].values())
    if 'players_queue' in session:
        players_queue = session['players_queue']
        total_points = max(
            sum(session['player_scores'][player]['used_rules_scores'].values()) for player in players_queue
        ) if players_queue else 0
    else:
        total_points = 0

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

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Minimal Yatzee Flask application, including useful error handlers.
"""
import traceback
from pathlib import Path
from flask import Flask, render_template, request, session, redirect, url_for
from src.hand import Hand
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes, Yahtzee
from src.rules import ThreeOfAKind, FourOfAKind, FullHouse, SmallStraight, LargeStraight, Chance
from src.scoreboard import Scoreboard
from src.game_helpers import initialize_session, update_scores, get_leaderboard_data,is_game_over
from src.leaderboard import Leaderboard
from src.sort import recursive_insertion
from src.queue import Queue
from src.player import Player
from src.unorderedlist import UnorderedList

app = Flask(__name__)
app.debug = True
app.secret_key = "my_secret_key"


@app.route('/select-players', methods=['GET', 'POST'])
def select_players():
    # Initialize the queue for GET requests
    if 'players_queue' not in session:
        session['players_queue'] = []

    if request.method == 'POST':
        num_players = int(request.form['num_players'])
        session['num_players'] = num_players
        session['players_queue'] = []

        # Add player names to the players_queue list
        for i in range(num_players):
            player_name = f"Player {i + 1}"
            # Add the player to the queue
            session['players_queue'].append(player_name)

        print(f"Session players_queue after POST: {session['players_queue']}")

        return redirect(url_for('main'))

    return render_template('start.html')


@app.route("/", methods=['GET', 'POST'])
def main():
    """
    Handles the main game logic for Yahtzee.
    """
    # Redirect to select-players if players are not set
    if 'players_queue' not in session or not session['players_queue']:
        return redirect(url_for('select_players'))
    
    used_rules,used_rules_scores,current_player,players_queue = initialize_session(session)

    rules = get_rules()
    hand = Hand(session['hand'])
    scoreboard = Scoreboard()
    error_message = None

    # Handle rolling dice
    if (request.method == 'POST'
            and request.form.get('chosen_dice') and session['roll_counter'] < 3):
        chosen_indices = [int(index)
                          for index in request.form.getlist('chosen_dice')]
        hand.roll(chosen_indices)
        session['roll_counter'] += 1
        session['hand'] = hand.to_list()

    # Handle scoring
    elif request.method == 'POST' and request.form.get('rule_name'):
        if session.get('must_switch', False):
            error_message = "You must switch players before submitting a new score!"

        rule_name = request.form['rule_name'].replace(' ', '')
        # Ensure rule is not reused for the current player
        if rule_name in used_rules:
            error_message = f"Rule '{rule_name}' has already been used by {current_player}!"
        else:
            rule_class = globals().get(rule_name)
            if rule_class:
                rule_instance = rule_class()
                try:
                    # Calculate the score for the rule
                    rule_score = rule_instance.points(hand)
                    # Update player-specific used rules and scores
                    used_rules.append(rule_name)
                    used_rules_scores[rule_name] = rule_score
                    # Mark that this turn is complete
                    session['must_switch'] = True
                    # Roll dice after scoring if the game is not over
                    if len(used_rules) < len(rules):
                        hand.roll()
                        print("hand:", hand)
                        session['roll_counter'] = 0
                        session['hand'] = hand.to_list()
                except ValueError as e:
                    error_message = str(e)
            else:
                error_message = f"Invalid rule: {rule_name}"

    # Calculate the scores for each rule (for the current player)
    update_scores(hand, rules, scoreboard, session, current_player)
    # scores = scoreboard.rules_and_scores_dict
    # for rule in rules:
    #     rule_name = rule.name.replace(' ', '')
    #     if rule_name not in used_rules:
    #         score = rule.points(hand)
    #         scores[rule_name] = score
    # scoreboard.from_dict(scores)

    # Ensure the session player_scores is updated before rotating
    session['player_scores'][current_player]['used_rules'] = used_rules
    session['player_scores'][current_player]['used_rules_scores'] = used_rules_scores

    # Calculate total points for the current player
    # print("format to add total points: ", used_rules_scores)
    total_points = sum(used_rules_scores.values())
    # print(total_points)

    # Debugging:
    # print(f"DEBUG: Current Player = {current_player}")
    # print(
    #     f"DEBUG: Used Rules = {session['player_scores'].get(current_player, {}).get('used_rules', 'Not Set')}")
    # print(
    #     f"DEBUG: Used Rules Scores = {session['player_scores'].get(current_player, {}).get('used_rules_scores', 'Not Set')}")
    # Check if the game is over for all players
    game_over=is_game_over(players_queue, session, rules)
    # game_over = all(len(session['player_scores'][player]['used_rules']) == len(rules) for player in players_queue)
    # highest_total_points = max(
    #     sum(session['player_scores'][player]['used_rules_scores'].values()) for player in players_queue
    # )
    highest_total_points, player_with_highest = get_highest_total_points_and_player(players_queue, session)
    print(highest_total_points,"the player who has this score:", player_with_highest)
    
    return render_template(
        'index.html',
        hand=hand,
        roll_counter=session['roll_counter'],
        score=scoreboard.rules_and_scores_dict,
        total_points=total_points,
        used_rules=used_rules,
        error_message=error_message,
        used_rules_scores=session['player_scores'][current_player]['used_rules_scores'],
        game_over=game_over,
        current_player=current_player,
        players=players_queue,
        highest_total_points=highest_total_points,
        player_with_highest=player_with_highest,
        must_switch=session.get('must_switch', False)
    )

def get_highest_total_points_and_player(players_queue, session):
    """
    Calculates the highest total points and the player who has that score.
    """
    highest_total_points = 0
    player_with_highest = None
    
    for player in players_queue:
        player_total_points = sum(session['player_scores'][player]['used_rules_scores'].values())
        if player_total_points > highest_total_points:
            highest_total_points = player_total_points
            player_with_highest = player

    return highest_total_points, player_with_highest



@app.route("/switch_player", methods=['POST'])
def switch_player():
    """
    Handles switching to the next player.
    """
    if 'players_queue' in session and session['players_queue']:
        # Rotate the queue to the next player
        session['players_queue'].append(session['players_queue'].pop(0))
        session['must_switch'] = False
        session.modified = True

    return redirect(url_for('main'))


def get_rules():
    """
    A helper function that returns a list of rule instances for the Yahtzee game.

    Returns:
        list: List of rule objects.
    """
    return [
        Ones(), Twos(), Threes(), Fours(), Fives(), Sixes(),
        ThreeOfAKind(), FourOfAKind(), FullHouse(), SmallStraight(),
        LargeStraight(), Chance(), Yahtzee()
    ]


@app.route("/reset", methods=['GET', 'POST'])
def reset():
    """
    Reset the game session to start a new game.
    """
    session.clear()
    return redirect(url_for('main'))


@app.route("/about")
def about():
    """
    Route for the about page
    """
    return render_template("about.html")


@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    """
    Display the leaderboard page with the current entries and total points.
    """
    if 'used_rules_scores' not in session:
        session['used_rules_scores'] = {}

    leaderboard_obj, entries, total_entries, total_points = get_leaderboard_data(
        session)

    print("List of entries obj -> list: ", list(entries))

    # Recursively sort the UnorderedList (entries)
    recursive_insertion(entries)
    print("After recursion: ", list(entries))

    sorted_entries_with_index = []
    for index, entry in enumerate(entries):
        sorted_entries_with_index.append((index, entry))

    return render_template(
        "leaderboard.html",
        total_points=total_points,
        leaderboard=leaderboard_obj,
        entries=sorted_entries_with_index,
        total_entries=total_entries,
    )


@app.route('/delete_mode', methods=['POST'])
def delete_mode():
    """
    Toggle the delete mode on the leaderboard page.
    """
    session['delete_mode'] = not session.get('delete_mode', False)
    return redirect(url_for('leaderboard'))


@app.route('/leaderboard/<int:index>', methods=['POST'])
def delete_entry(index):
    """
    Delete a specific leaderboard entry at its index.
    """
    leaderboard_obj = Leaderboard.load("leaderboard.txt")
    
    recursive_insertion(leaderboard_obj.entries)
    
    leaderboard_obj.remove_entry(index)

    return redirect(url_for('leaderboard'))


@app.route('/leaderboard', methods=['POST'])
def add_entry():
    """
    Add a new entry to the leaderboard with the player's name and score.
    """
    leaderboard_obj, _, _, total_points = get_leaderboard_data(session)

    player_name = request.form['player_name']
    # only ad the score of maximum points from both paleyrs
    # highscore = max(totalpoints1,totalpoints2)
    leaderboard_obj.add_entry(player_name, total_points)
    leaderboard_obj.save(Path("leaderboard.txt"))

    session['player_name_submitted'] = True

    return redirect(url_for('leaderboard'))


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()

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
# import random
from src.scoreboard import Scoreboard
# import src.rules
from src.game_helpers import initialize_session, update_scores, get_leaderboard_data
from src.leaderboard import Leaderboard
from src.sort import insertion_sort, recursive_insertion
from src.unorderedlist import UnorderedList

app = Flask(__name__)
app.debug = True
app.secret_key = "my_secret_key"


@app.route("/", methods=['GET', 'POST'])
def main():
    """
    Handles the main game logic for Yahtzee.
    It processes dice rolls, scoring, and updates the session.
    It initializes the game, rolls dice based on user input,
    calculates scores, and ends the game when all rules are scored.

    Returns:
        str: Renders HTML template for the Yahtzee game.
    """
    rules = get_rules()
    initialize_session(session)

    # Create hand using stored values
    hand = Hand(session['hand'])
    # print("Initial dice values:", hand)
    scoreboard = Scoreboard()
    error_message = None

    # Handle rolling dice
    if (request.method == 'POST'
            and request.form.get('chosen_dice') and session['roll_counter'] < 3):
        chosen_indices = []
        for index in request.form.getlist('chosen_dice'):
            chosen_indices.append(int(index))
        # print("chose indices:", chosen_indices)
        hand.roll(chosen_indices)
        session['roll_counter'] += 1
        session['hand'] = hand.to_list()

    # Handle scoring
    elif request.method == 'POST' and request.form.get('rule_name'):
        rule_name = request.form['rule_name'].replace(' ', '')

        # Ensure rule is not reused
        if rule_name in session['used_rules']:
            # print("Rule name from post duplicate error:", rule_name)
            error_message = f"Rule '{rule_name}' has already been used!"
        else:
            rule_class = globals().get(rule_name)

            if rule_class:
                rule_instance = rule_class()
                try:
                    # Calculate the score for the rule
                    rule_score = rule_instance.points(hand)

                    # Update session data
                    session['used_rules'].append(rule_name)
                    session['used_rules_scores'][rule_name] = rule_score

                    # Roll dice after scoring if the game is not over
                    if len(session['used_rules_scores']) < len(rules):
                        hand.roll()
                        session['roll_counter'] = 0
                        session['hand'] = hand.to_list()
                        # print("After new roll values:", session['hand'])

                except ValueError as e:
                    error_message = str(e)
            else:
                error_message = f"Invalid rule: {rule_name}"
    # Reset roll
    if request.args.get('roll'):
        print("Rolling dice again from GET method...")
        hand.roll()
        session['roll_counter'] = 0
        session['hand'] = hand.to_list()
    # Calculate the scores for each rule
    update_scores(hand, rules, scoreboard, session)

    # Calculate total points
    total_points = sum(session['used_rules_scores'].values())
    # Store total points in session
    session['total_points'] = total_points
    game_over = len(session['used_rules_scores']) == len(rules)
    # # DDEBUGG
    # print("Used rules:", session['used_rules'])
    # print("Used rules scores:", session['used_rules_scores'])
    # print("Ending roll dice values:", hand)

    return render_template(
        'index.html',
        hand=hand,
        roll_counter=session['roll_counter'],
        score=scoreboard.rules_and_scores_dict,
        total_points=total_points,
        used_rules=session['used_rules'],
        error_message=error_message,
        used_rules_scores=session['used_rules_scores'],
        game_over=game_over
    )


def get_rules():
    """
    A helper fuction that returns a list of rule instances for the Yahtzee game.

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
    # return redirect("/~hahi24/dbwebb-kurser/oopython/me/kmom04/yahtzee3/app.cgi")
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
    leaderboard_obj, entries, total_entries, total_points = get_leaderboard_data(
        session)
    print("-1.basic unsorted entries as list :", list(leaderboard_obj.entries))
    entries_with_index = []
    for index, entry in enumerate(entries):
        entries_with_index.append((index, entry))
    print("-2.Unosrted entries with index:", entries_with_index)   
    
    recursive_insertion(leaderboard_obj.entries)
    sorted_entries = leaderboard_obj.entries.print_list()
    print("-3.Result of sorted list:", sorted_entries)
    
    sorted_entries_with_index = []
    for index, entry in enumerate(entries):
        sorted_entries_with_index.append((index, entry))
    print("-4.Sorted entries with index:", sorted_entries_with_index)
    
    return render_template(
        "leaderboard.html",
        total_points=total_points,
        leaderboard=leaderboard_obj,
        # entries=entries_with_index,
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


@app.route('/leaderboard', methods=['POST'])
def add_entry():
    """
    Add a new entry to the leaderboard with the player's name and score.
    """
    # filename = Path("leaderboard.txt")

    leaderboard_obj, _, _, total_points = get_leaderboard_data(session)
    # leaderboard = Leaderboard.load(filename)

    player_name = request.form['player_name']

    leaderboard_obj.add_entry(player_name, total_points)
    leaderboard_obj.save(Path("leaderboard.txt"))

    session['player_name_submitted'] = True

    return redirect(url_for('leaderboard'))


@app.route('/leaderboard/<int:index>', methods=['POST'])
def delete_entry(index):
    """
    Delete a specific leaderboard entry at its index.
    """
    leaderboard_obj = Leaderboard.load("leaderboard.txt")
    leaderboard_obj.remove_entry(index)

    return redirect(url_for('leaderboard'))


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    # pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    # pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()

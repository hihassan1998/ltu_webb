#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Minimal Yatzee Flask application, including useful error handlers.
"""
import traceback
from flask import Flask, render_template, request, session, redirect
from src.hand import Hand
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes, Yahtzee
from src.rules import ThreeOfAKind, FourOfAKind, FullHouse, SmallStraight, LargeStraight, Chance
# import random
from src.scoreboard import Scoreboard
# import src.rules
from src.game_helpers import initialize_session, update_scores

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
    print("Initial dice values:", hand)
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
                        print("After new roll values:", session['hand'])

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
    game_over = len(session['used_rules_scores']) == len(rules)
    # # DDEBUGG
    # print("Used rules:", session['used_rules'])
    # print("Used rules scores:", session['used_rules_scores'])
    print("Ending roll dice values:", hand)

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


@app.route("/reset")
def reset():
    """
    Reset the game session to start a new game.
    """
    session.clear()
    return redirect("/")


@app.route("/about")
def about():
    """
    Route for the about page
    """
    return render_template("about.html")


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

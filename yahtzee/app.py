#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Yatzee Flask application, including useful error handlers.
"""
import traceback
from flask import Flask, render_template, request
from src.hand import Hand

app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET'])
def index():
    hand = Hand()
    roll = request.args.get('roll', False)  # Check if roll triggg
    if roll:
        # If 'roll' is set to True, roll the dice
        print(hand)
        hand.roll()
    else:
        hand = Hand()  # Show 5 dice by default
    return render_template('index.html', hand=hand)

@app.route("/about")
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py file for main funtion to run the the 8 FInger 2 Thumbs Game chatbot
"""
from pathlib import Path
import typing_test


def main():
    """
    A funtion to run the 82-Game chatbot that takes in 3 text files
    and runs a typing test on them.
    """

    cwd = Path.cwd()
    easy_file = cwd / "easy.txt"
    medium_file = cwd / "medium.txt"
    hard_file = cwd / "hard.txt"
    score_file = cwd / "score.txt"

    game_img = r"""
     ___    _____ _                                 
    ( _ )  |  ___(_)_ __   __ _  ___ _ __ ___      
    / _ \  | |_  | | '_ \ / _` |/ _ \ '__/ __|     
   | (_) | |  _| | | | | | (_| |  __/ |  \__ \  _  
    \___/  |_|___|_|_| |_|\__, |\___|_| _|___/ (_) 
    |___ \  |_   _| |__  _ |___/ __ ___ | |__  ___  
      __) |   | | | '_ \| | | | '_ ` _ \| '_ \/ __| 
     / __/    | | | | | | |_| | | | | | | |_) \__ \ 
    |_____|   |_| |_| |_|\__,_|_| |_| |_|_.__/|___/ 
    
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(game_img)
        print("Welcome to 8 fingers and 2 thumbs game, "
              "where you get to compete with yourself and learn to type faster.")
        print("| Menu: ty_t2|")
        print("1.Start typing test. (Easy Level)")
        print("2. Start typing test. (Medium Level)")
        print("3.Start typing test. (Hard Level)")
        print("4. Show saved test results.")
        print("Press 'q' to quit.")

        choice = input("Choose an option; 1-4: \n -->")

        try:
            if choice == "1":
                lines = typing_test.read_file(easy_file)
                tot_letters, tot_words = typing_test.words_letters_returned(
                    lines)
                typing_test.start_game(lines, tot_letters, tot_words)

            elif choice == "2":
                lines = typing_test.read_file(medium_file)
                tot_letters, tot_words = typing_test.words_letters_returned(
                    lines)
                typing_test.start_game(lines, tot_letters, tot_words)

            elif choice == "3":
                lines = typing_test.read_file(hard_file)
                tot_letters, tot_words = typing_test.words_letters_returned(
                    lines)
                typing_test.start_game(lines, tot_letters, tot_words)

            elif choice == "4":
                typing_test.show_results(score_file)

            elif choice == "q":
                break

            else:
                print("Wrong choice, choose from the options!")

        except FileNotFoundError as fnf:
            print(
                f"fnfor: {fnf}. File not found. Please ensure the file is not missing.")
        except ValueError as verr:
            print(
                f"Error: {verr}. Check if file is correctly formatted.")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    main()

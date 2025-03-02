#!/usr/bin/env python3
"""
This module contains the Leaderboard class,
which manages the leaderboard of players and their scores.
The class utilizes an UnorderedList to store player names,
and their corresponding scores as tuples.
It provides functionality to load, save, add, and remove leaderboard entries.
"""
from pathlib import Path
from src.unorderedlist import UnorderedList
from src.errors import MissingIndex, MissingValue


class Leaderboard():
    """
    This class handles the leaderboard of players and their scores.
    Uses an UnorderedList to store players and their scores as tuples
    """

    def __init__(self, entries=None):
        """
        Constructor for Leaderboard class.
        If entries is provided, it will populate the UnorderedList with those entries.
        """
        self.entries = UnorderedList()
        if entries:
            for entry in entries:
                self.entries.append(entry)

    @classmethod
    def load(cls, filename: Path):
        """
        Load the leaderboard from a file and return a Leaderboard object.
        Ensures all past entries are added to UnorderedList.
        """
        leaderboard = cls()

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    name, score = line.strip().split(",")
                    leaderboard.entries.append(
                        (name, int(score)))
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty leaderboard.")

        return leaderboard

    def save(self, filename: Path):
        """
        Save the leaderboard entries to the file.
        This writes the current entries from the UnorderedList to the file.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            current = self.entries.head
            while current:
                name, score = current.data
                file.write(f"{name},{score}\n")
                current = current.next

    def add_entry(self, name, score):
        """
        Add a new entry to the leaderboard.
        The entry is added to the UnorderedList and the file is updated.
        """
        self.entries.append((name, score))
        self.save("leaderboard.txt")

    def remove_entry(self, index):
        """
        Remove an entry by its index from the leaderboard.
        This operation modifies the UnorderedList and updates the file.
        """
        try:
            entry_to_remove = self.entries.get(index)
            self.entries.remove(entry_to_remove)
            self.save("leaderboard.txt")
        except MissingIndex as e:
            raise MissingIndex("Index not found in the leaderboard.") from e
        except MissingValue as e:
            raise MissingValue("Value not found in the leaderboard.") from e

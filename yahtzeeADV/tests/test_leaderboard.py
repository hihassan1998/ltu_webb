#!/usr/bin/env python3
""" Module for testing the Leaderboard Class """
import unittest
from unittest.mock import mock_open, patch
from src.leaderboard import Leaderboard


class TestLeaderboard(unittest.TestCase):
    """ Test case class for the Leaderboard class functionality """

    def test_load_leaderboard(self):
        """ Test loading leaderboard data from a file """
        mock_data = "HAssan,150\nBob,200\n"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            leaderboard = Leaderboard.load("leaderboard.txt")

        # Check that the data is loaded correctly into the leaderboard
        self.assertEqual(leaderboard.entries.size(), 2)
        self.assertEqual(leaderboard.entries.get(0), ("HAssan", 150))

    def test_add_entry(self):
        """ Test adding a new entry to the leaderboard and saving to file """
        with patch("builtins.open", mock_open()):
            leaderboard = Leaderboard.load("leaderboard.txt")
            leaderboard.add_entry("Julia", 250)

        with patch("builtins.open", mock_open()) as mocked_file:
            leaderboard.save("leaderboard.txt")

            # Check if the file was opened correctly and the entry was written
            mocked_file.assert_called_once_with(
                "leaderboard.txt", 'w', encoding='utf-8')
            mocked_file().write.assert_any_call("Julia,250\n")

    def test_remove_entry(self):
        """ Test removing an entry from the leaderboard """
        mock_data = "HAssan,150\nBob,200\n"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            leaderboard = Leaderboard.load("leaderboard.txt")
            leaderboard.remove_entry(0)

        # Check that only one entry remains and that it's the right one
        self.assertEqual(leaderboard.entries.size(), 1)
        self.assertEqual(leaderboard.entries.get(0), ("Bob", 200))


if __name__ == "__main__":
    unittest.main()

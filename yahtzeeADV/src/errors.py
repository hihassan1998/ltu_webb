#!/usr/bin/env python3
"""
This module contains the Error handling classes for the Nodes at errorneous indexes.
"""


class MissingIndex(Exception):
    """Exception raised when an index is missing."""


class MissingValue(Exception):
    """Exception raised when a value is missing in the list."""

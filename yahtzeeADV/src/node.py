#!/usr/bin/env python3
"""
This module contains the Node class and the Error handling classes for the Nodes at indexes.
"""


class Node():
    """
    Node class
    """

    def __init__(self, data, next_=None):
        """
        Initialize object with the data and set next to None.
        next will be assigned later when new data needs to be added.
        """
        self.data = data
        self.next = next_

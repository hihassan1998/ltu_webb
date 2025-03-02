#!/usr/bin/env python3
"""
This module contains the queue class.

The queue class is responsible for ......
"""


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        try:
            return self._items.pop(0)

        except IndexError:
            return "Empty list."

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)

    def to_list(self):
        """ Converts the queue to a list. """
        return self._items

    @classmethod
    def from_list(cls, items_list):
        """ Rebuilds the Queue from a list. """
        queue = cls()
        for item in items_list:
            queue.enqueue(item)
        return queue

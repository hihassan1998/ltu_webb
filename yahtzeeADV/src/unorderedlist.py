#!/usr/bin/env python3
"""
This module contains the UnorderedList class, which implements an unordered linked list.
The class provides methods to append, get, set, remove, and manipulate list items.
It also allows support of iteration over the list to skip manual data retrival.
"""
from src.node import Node
from src.errors import MissingIndex, MissingValue


class UnorderedList():
    """
    Represents an unordered list implemented as a linked list.

    Attributes:
        head (Node): The first node in the list. It stores data and points to the next node.
    """

    def __init__(self):
        """
        Implementing a linked list as an unorderedlist.
        """
        self.head = None

    def append(self, data=None):
        """ Adds an item to end of the list. """
        latest_node = Node(data)
        if not self.head:
            self.head = latest_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = latest_node

    def get(self, index):
        """ Gets an item at a specific index. Raises IndexError if out of range. """
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise MissingIndex("Index is missing in the list.")

    def set(self, index, data=None):
        """ Change data at a specific index of the list. """
        current = self.head
        count = 0
        while current:
            if count == index:
                current.data = data
                return
            current = current.next
            count += 1
        raise MissingIndex("Index is missing in the list.")

    def size(self):
        """Returns the length of list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def index_of(self, data):
        """ Returns index for a value """
        current = self.head
        count = 0
        while current:
            if current.data == data:
                return count
            current = current.next
            count += 1
        raise MissingValue("Value is not present in the list.")

    def remove(self, data):
        """
        Removes the items from its first occurence in the list.
        Raises ValueError if item not found.
        """
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        raise MissingValue("Value is not present in the list.")

    def print_list(self):
        """Returns a Python list representation of the linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    # def print_list(self):
    #     """Prints the content of the list."""
    #     current = self.head
    #     while current:
    #         print(current.data, end=' -> ')
    #         current = current.next
    #     print("None")

    def __iter__(self):
        """Allows iteration over the linked list."""
        current = self.head
        while current:
            yield current.data
            current = current.next

#!/usr/bin/env python3
"""
this module conains the Node class.
The class represents a node in a binary search tree.
It provides the methods to check if the node has children, parent, or is a leaf.
It provides the methods to check if the node is a left or right child of its parent.
it provides the methods to comapre two nodes.
"""


class Node:
    """
    The constructor for the Node class
    """

    def __init__(self, key, value, parent=None):
        """
        Initialize the Node with given key, value and optional parent.

        Args:
            key (Object): a comparable object
            value (Object): the value associated with the key
            parent (Node): the parent node
        """
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def has_left_child(self):
        """
        Check if the node has a left child.
        """
        if self.left:
            return True
        else:
            return False

    def has_right_child(self):
        """
        Check if the node has a right child.
        """
        if self.right:
            return True
        else:
            return False

    def has_both_children(self):
        """
        Check if the node has both left and right children.
        """
        if self.has_left_child() and self.has_right_child():
            return True
        else:
            return False

    def has_parent(self):
        """
        Check if the node has a parent.
        """
        if self.parent:
            return True
        else:
            return False

    def is_left_child(self):
        """
        Check if the node is a left child.
        """
        if self.has_parent() and self.parent.left == self:
            return True
        else:
            return False

    def is_right_child(self):
        """
        Check if the node is a right child.
        """
        if self.has_parent() and self.parent.right == self:
            return True
        else:
            return False

    def is_leaf(self):
        """
        Check if the node is a leaf.
        """
        if self.has_left_child() and self.has_right_child():
            return False
        else:
            return True

    def __lt__(self, other):
        """
        Compares two nodes. Check if node's key is less than the other node's key
        """
        return self.key < other.key

    def __gt__(self, other):
        """
        Compares two nodes. Check if node's key is greater than the other node's key
        """
        return self.key > other.key

    def __eq__(self, other):
        """
        Compares two nodes.
        """
        return self.key == other.key

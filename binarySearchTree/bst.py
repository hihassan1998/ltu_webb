#!/usr/bin/env python3
"""
This module contains the Binary Search Tree class.
The class represents a binary search tree data structure.
It provides methods to insert, delete, search, size, and inorder traversal to traverse the tree.
"""
from node import Node


class BinarySearchTree:
    """"
    Constructor for the BinarySearchTree class.
    """

    def __init__(self):
    # def __init__(self, nodes=None):
        """
        Initialize the Binary Search Tree with no root node.
        """
        self.root = None
        self.node_count = 0
        # Tips:
        # comment out if the flexibility of insertinf tuples is needed as well
        # Remove the counter then and comment out the get methods private function too
        # self.node_count = 0
        # if nodes is not None:
        #     for node in nodes:
        #         self.insert(node[0], node[1])

    def insert(self, key, value):
        """
        Inserts a new node into the binary search tree with the given key and value.
        """
        if self.root is None:
            self.root = Node(key, value)
            self.node_count += 1
        else:
            self.insert_recursive(self.root, key, value)
            self.node_count += 1

    def inorder_traversal(self, node=None):
        """
        Performs an inorder traversal of the binary search tree,
        printing the values of each node visited.
        """
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.inorder_traversal(node.left)
            print(node.value)
            if node.right is not None:
                self.inorder_traversal(node.right)

    def inorder_traversal_print(self):
        """Print the values in the tree in sorted order."""
        if self.root is not None:
            self.inorder_traversal(self.root)

    def get(self, key):
        """Returns the value related to the node with the key."""
        node = self._get_recursive(self.root, key)
        if node:
            return node.value
        raise KeyError(f"Key {key} not found.")

    def _get_recursive(self, current_node, key):
        """Recursive helper method to find a node with the given key."""
        if current_node is None:
            return None
        if key < current_node.key:
            return self._get_recursive(current_node.left, key)
        elif key > current_node.key:
            return self._get_recursive(current_node.right, key)
        else:
            return current_node

    def remove(self, key):
        """Remove the node with the given key and return its value."""
        node = self._get_recursive(self.root, key)
        if node is None:
            raise KeyError(f"Key {key} not found.")
        value = node.value
        self._remove_node(node)
        self.node_count -= 1
        return value

    def _remove_node(self, node):
        """Recursive helper method to remove a node from the tree."""
        if node.is_leaf():
            # If leaf node, remove it
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.has_left_child() and node.has_right_child():
            # If both children, find the minimum node (in-order)
            min_node = self._get_min(node.right)
            node.key, node.value = min_node.key, min_node.value
            self._remove_node(min_node)
        else:
            # Node has one child
            child = node.left if node.has_left_child() else node.right
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
            child.parent = node.parent

    def _get_min(self, node):
        """Find the node with the minimum key (leftmost node)."""
        while node.has_left_child():
            node = node.left
        return node

    def size(self):
        """
        Returns the number of nodes in the binary search tree.
        """
        # return self.count_nodes(self.root)
        return self.node_count

    # Helper functions
    # def count_nodes(self, node):
    #     """
    #     Recursively counts the number of nodes in the binary search tree.

    #     Args:
    #         node (Node): The current node to count.

    #     Returns:
    #         int: The number of nodes in the binary search tree.
    #     """
    #     if node is None:
    #         return 0
    #     else:
    #         return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def insert_recursive(self, node, key, value):
        """
        Recursively inserts a new node into the binary search tree with the given key and value.

        Args:
            node (Node): The current node to compare with the given key.
            key (Object): The key of the node to be inserted.
            value (Object): The value of the node to be inserted.
        """
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value, node)
            else:
                self.insert_recursive(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value, node)
            else:
                self.insert_recursive(node.right, key, value)


def main():
    """Main function to test the BinarySearchTree class."""
    bst = BinarySearchTree()

    # Insert values
    bst.insert(10, "Ten")
    bst.insert(5, "Five")
    bst.insert(15, "Fifteen")
    bst.insert(3, "Three")
    bst.insert(7, "Seven")

    # Print in-order traversal
    print("In-order traversal:")
    bst.inorder_traversal_print()

    # Get value for a specific key
    print("\nGet value for key 7:")
    print(bst.get(7))

    # Print size of tree before removal of 5
    print(f"\nSize of the tree before .remove: {bst.size()}")
    
    # Remove a node
    print("\nRemove node with key 5:")
    print(bst.remove(5))

    # Print size of tree after removal of 5
    print(f"\nSize of the tree: {bst.size()}")

    # Print in-order traversal after removal
    print("\nIn-order traversal after removal:")
    bst.inorder_traversal_print()


if __name__ == "__main__":
    main()

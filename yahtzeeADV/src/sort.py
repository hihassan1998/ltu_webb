#!/usr/bin/env python3
"""
This module contains the scort functions.
"""


# def insertion_sort(unordered_list):
#     """ Sorts the UnorderedList using insertion sort based on the second element (score). """
#     size = unordered_list.size()

#     for i in range(1, size):
#         key = unordered_list.get(i)
#         j = i - 1

#         while j >= 0 and unordered_list.get(j)[1] > key[1]:
#             unordered_list.set(j + 1, unordered_list.get(j))
#             j -= 1

#         unordered_list.set(j + 1, key)
def insertion_sort(unordered_list):
    """ Sorts the UnorderedList using insertion sort based on the values themselves. """
    size = unordered_list.size()

    for i in range(1, size):
        key = unordered_list.get(i)
        j = i - 1

        # Directly compare the values (for both integers and strings)
        while j >= 0 and unordered_list.get(j) > key:
            unordered_list.set(j + 1, unordered_list.get(j))
            j -= 1

        unordered_list.set(j + 1, key)


def recursive_insertion(unordered_list, n=None):
    """Recursively sorts the UnorderedList using insertion sort."""
    if n is None:
        n = unordered_list.size()
    if n <= 1:
        return
    recursive_insertion(unordered_list, n - 1)

    key = unordered_list.get(n - 1)
    j = n - 2

    # Directly compare the values (for both integers and strings)
    while j >= 0 and unordered_list.get(j)[1] > key[1]:
        # MAKE CHANGES HERE AT THE SPECIFIED INDEX
        unordered_list.set(j + 1, unordered_list.get(j))
        j -= 1

    unordered_list.set(j + 1, key)

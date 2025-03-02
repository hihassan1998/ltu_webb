#!/usr/bin/env python3
""" Module for testing the UnorderedList Class """
import unittest
from src.unorderedlist import UnorderedList, MissingIndex, MissingValue


class TestSort(unittest.TestCase):
    """ Test class for the UnorderedList class """

    def setUp(self):
        """ New instance of UnorderedList for each test """
        self.my_list = UnorderedList()

    def test_add(self):
        """ Test appending elements to the list """
        self.my_list.append(('Ali', 10))
        self.my_list.append(20)
        self.my_list.append(30)
        self.assertEqual(self.my_list.size(), 3)

    def test_get_by_index(self):
        """ Test getting an element by index """
        self.my_list.append(('Ali', 10))
        self.my_list.append(20)
        self.assertEqual(self.my_list.get(1), 20)

        # Check if it raises MissingIndex
        with self.assertRaises(MissingIndex):
            self.my_list.get(5)

    def test_set_by_index(self):
        """ Test setting an element by index """
        self.my_list.append(('Ali', 10))
        self.my_list.append(20)
        self.my_list.set(1, 25)
        self.assertEqual(self.my_list.get(1), 25)

        # Check if it raises MissingIndex
        with self.assertRaises(MissingIndex):
            self.my_list.set(5, 30)



if __name__ == "__main__":
    unittest.main()

# Python code to demonstrate working of unittest 
import unittest
from functions import *
import random

class SortingTestCase(object):
    def test_random_list(self):
        x = [ random.uniform(0, 10) for i in range(100) ]
        result = self.function(x)

        self.assertEqual(sorted(x), result)

    def test_sorted_list(self):
        x = sorted([ random.uniform(0, 10) for i in range(100) ])
        result = self.function(x)

        self.assertEqual(x, result)

    def test_uniform_list(self):
        x = [ 0 for i in range(100) ]
        result = self.function(x)

        self.assertEqual(x, result)

    def test_empty_list(self):
        x = []
        result = self.function(x)

        self.assertEqual(x, result)

    def test_single_element_list(self):
        x = [0]
        result = self.function(x)

        self.assertEqual(x, result)

    def test_character_list(self):
        characters = "abcdefghijklmnopqrstuvwxyz1234567890"
        x = [ random.choice(characters) for i in range(100) ]
        result = self.function(x)

        self.assertEqual(sorted(x), result)

class SelectionSortTestCase(SortingTestCase, unittest.TestCase):
    def function(self, param):
        return selection_sort(param)

class BubbleSortTestCase(SortingTestCase, unittest.TestCase):
    def function(self, param):
        return bubble_sort(param)

class RecursiveBubbleSortTestCase(SortingTestCase, unittest.TestCase):
    def function(self, param):
        return recursive_bubble_sort(param)

class InsertionSortTestCase(SortingTestCase, unittest.TestCase):
    def function(self, param):
        return insertion_sort(param)
  
if __name__ == '__main__': 
    unittest.main() 
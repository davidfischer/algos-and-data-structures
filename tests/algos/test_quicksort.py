import unittest

from algorithms.quicksort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_empty(self):
        self.assertEquals([], quicksort([]))

    def test_one(self):
        self.assertEquals([1], quicksort([1]))

    def test_numbers(self):
        l1 = [2,5,2,6,7]
        self.assertEquals(sorted(l1), quicksort(l1))

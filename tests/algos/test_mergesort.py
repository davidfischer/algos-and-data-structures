import unittest

from algorithms.mergesort import mergesort

class TestMergesort(unittest.TestCase):
    def test_empty(self):
        self.assertEquals([], mergesort([]))

    def test_one(self):
        self.assertEquals([1], mergesort([1]))

    def test_numbers(self):
        l1 = [2,5,2,6,7]
        self.assertEquals(sorted(l1), mergesort(l1))

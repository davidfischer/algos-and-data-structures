import unittest

from algorithms.bubblesort import bubblesort

class TestBubblesort(unittest.TestCase):
    def test_empty(self):
        self.assertEquals([], bubblesort([]))

    def test_one(self):
        self.assertEquals([1], bubblesort([1]))

    def test_numbers(self):
        l1 = [2,5,2,6,7]
        self.assertEquals(sorted(l1), bubblesort(l1))

        l2 = [5,8,2,0,1,-1,9]
        self.assertEquals(sorted(l2), bubblesort(l2))

        l3 = [9,-1,7]
        self.assertEquals(sorted(l3), bubblesort(l3))

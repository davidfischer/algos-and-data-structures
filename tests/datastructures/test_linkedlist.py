import unittest

from datastructures.linkedlist import ListOutOfRangeError, LinkedList

class TestLinkedList(unittest.TestCase):
    def test_empty(self):
        s = LinkedList()
        self.assertEquals(s.size(), 0)
        self.assertRaises(ListOutOfRangeError, s.remove, 1)
        self.assertRaises(ListOutOfRangeError, s.get, 0)

    def test_get(self):
        s = LinkedList()
        s.insert('a', 0)
        s.insert('b', 0)
        s.insert('c', 0)
        self.assertEquals(s.get(0), 'c')
        self.assertEquals(s.get(1), 'b')
        self.assertEquals(s.get(2), 'a')
        self.assertRaises(ListOutOfRangeError, s.get, 4)
        s.insert('d', 1)
        self.assertEquals(s.get(0), 'c')
        self.assertEquals(s.get(1), 'd')
        self.assertEquals(s.get(2), 'b')

    def test_remove(self):
        s = LinkedList()
        self.assertRaises(ListOutOfRangeError, s.remove, 0)
        s.insert('a', 0)
        s.insert('b', 1)
        s.insert('c', 2)
        self.assertEquals(s.remove(1), 'b')
        self.assertEquals(s.get(0), 'a')
        self.assertEquals(s.get(1), 'c')
        self.assertRaises(ListOutOfRangeError, s.remove, 2)
        self.assertEquals(s.remove(1), 'c')
        self.assertEquals(s.remove(0), 'a')
        self.assertRaises(ListOutOfRangeError, s.remove, 0)

    def test_index(self):
        s = LinkedList()
        s.insert('a', 0)
        self.assertEquals(s.index('a'), 0)
        self.assertEquals(s.index('b'), None)
        s.insert('b', 1)
        self.assertEquals(s.index('a'), 0)
        self.assertEquals(s.index('b'), 1)
        s.insert('c', 1)
        self.assertEquals(s.index('a'), 0)
        self.assertEquals(s.index('b'), 2)
        self.assertEquals(s.index('c'), 1)
        s.insert('d', 0)
        self.assertEquals(s.index('d'), 0)
        self.assertEquals(s.index('a'), 1)
        self.assertEquals(s.index('b'), 3)
        self.assertEquals(s.index('c'), 2)

    def test_size(self):
        s = LinkedList()
        s.insert('a', 0)
        s.insert('b', 0)
        self.assertEquals(s.size(), 2)
        s.insert('c', 2)
        self.assertEquals(s.size(), 3)
        s.remove(0)
        self.assertEquals(s.size(), 2)
        s.remove(0)
        self.assertEquals(s.size(), 1)
        s.remove(0)
        self.assertEquals(s.size(), 0)

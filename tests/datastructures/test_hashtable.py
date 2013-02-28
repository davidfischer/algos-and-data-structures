import unittest

from datastructures.hashtable import HashTable

class TestHashTable(unittest.TestCase):
    def test_empty(self):
        h = HashTable()
        self.assertEquals(h.size(), 0)
        self.assertEquals(h.lookup('a'), None)

    def test_size(self):
        h = HashTable()
        self.assertEquals(h.size(), 0)
        h.insert('a', 1)
        h.insert('b', 2)
        self.assertEquals(h.size(), 2)
        h.insert('b', 9)
        self.assertEquals(h.size(), 2)
        h.insert('c', 3)
        self.assertEquals(h.size(), 3)
        h.insert('c', 4)
        self.assertEquals(h.size(), 3)
        h.insert('d', 8)
        self.assertEquals(h.size(), 4)
        h.remove('c')
        self.assertEquals(h.size(), 3)

    def test_lookup(self):
        h = HashTable()
        h.insert('a', 1)
        h.insert('b', 2)
        self.assertEquals(h.lookup('a'), 1)
        self.assertEquals(h.lookup('b'), 2)
        self.assertEquals(h.lookup('c'), None)
        h.insert('b', 4)
        self.assertEquals(h.lookup('b'), 4)

    def test_remove(self):
        h = HashTable()
        self.assertEquals(h.remove('a'), None)
        h.insert('a', 1)
        h.insert('b', 2)
        self.assertEquals(h.remove('a'), 1)
        self.assertEquals(h.remove('b'), 2)
        h.insert('b', 3)
        self.assertEquals(h.remove('a'), None)
        self.assertEquals(h.remove('b'), 3)

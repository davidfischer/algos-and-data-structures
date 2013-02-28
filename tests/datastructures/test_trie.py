import unittest

from datastructures.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie()

    def test_emptytrie(self):
        self.assertTrue(self.t.lookup('at') is None)
        self.assertTrue(self.t.lookup('') is None)

    def test_basicinsert(self):
        self.t.insert('a')
        self.assertFalse(self.t.lookup('a') is None)
        self.assertTrue(self.t.lookup('at') is None)
        self.t.insert('ate')
        self.assertTrue(self.t.lookup('at') is None)
        self.assertFalse(self.t.lookup('ate') is None)
        self.t.insert('bravo')
        self.assertTrue(self.t.lookup('') is None)
        self.assertFalse(self.t.lookup('a') is None)
        self.assertTrue(self.t.lookup('b') is None)
        self.assertTrue(self.t.lookup('brav') is None)
        self.assertTrue(self.t.lookup('brave') is None)
        self.assertFalse(self.t.lookup('bravo') is None)

    def test_remove(self):
        self.t.insert('a')
        self.assertFalse(self.t.lookup('a') is None)
        self.t.remove('a')
        self.assertTrue(self.t.lookup('a') is None)
        self.t.insert('ate')
        self.assertTrue(self.t.lookup('a') is None)
        self.assertFalse(self.t.lookup('ate') is None)

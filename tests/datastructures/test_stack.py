import unittest

from datastructures.stack import EmptyStackError, Stack

class TestStack(unittest.TestCase):
    def test_empty(self):
        s = Stack()
        self.assertTrue(s.empty(), True)
        self.assertRaises(EmptyStackError, s.top)
        self.assertRaises(EmptyStackError, s.pop)

    def test_simple(self):
        s = Stack()
        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEquals(s.top(), 'c')
        self.assertFalse(s.empty())
        self.assertEquals(s.pop(), 'c')
        self.assertEquals(s.pop(), 'b')
        self.assertEquals(s.pop(), 'a')
        self.assertTrue(s.empty())

    def test_multiple(self):
        s = Stack()
        s.push('a')
        self.assertFalse(s.empty())
        s.push('b')
        self.assertEquals(s.pop(), 'b')
        s.push('b')
        self.assertEquals(s.pop(), 'b')
        s.push('b')
        self.assertEquals(s.pop(), 'b')
        self.assertEquals(s.pop(), 'a')
        self.assertTrue(s.empty())
        self.assertRaises(EmptyStackError, s.pop)
        

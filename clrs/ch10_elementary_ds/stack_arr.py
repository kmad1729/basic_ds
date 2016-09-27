#!/usr/bin/env python3
'array implementation of stack'

import unittest

class Stack:

    def __init__(self, max_sz = 100):
        self.max_sz = max_sz
        self._stack = [None] * max_sz
        self.head = -1

    def push(self, elem):
        if self.head == self.max_sz:
            raise IndexError("Stack Overflow!")
        self.head += 1
        self._stack[self.head] = elem

    def empty(self):
        'check if stack is empty'
        return self.head == -1

    def top(self):
        if self.empty():
            raise IndexError("Empty stack!")
        return self._stack[self.head]

    def pop(self):
        if self.empty():
            raise IndexError("Cannot pop from empty stack!")
        ret = self._stack[self.head]
        self.head -= 1
        return ret


#### TESTS #####
class TestStack_Arr(unittest.TestCase):
    def test_push(self):

        max_sz = 2
        stack = Stack(max_sz = max_sz)
        stack.push(5)
        stack.push(42)
        try:
            stack.push(43)
            self.assertTrue(False, "more than {sz} allow to push on stack".format(
                sz = max_sz))
        except IndexError as e:
            self.assertTrue(True)

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.empty())
        stack.push(32)
        self.assertFalse(stack.empty())

    def test_top(self):
        stack = Stack()

        try:
            top = stack.top()
            self.assertTrue(False, "was able to get the top of empty stack!")
        except IndexError as e:
            self.assertTrue(True)
        stack.push('yo mama!')
        self.assertEqual('yo mama!', stack.top())
        stack.push(42)
        self.assertEqual(42, stack.top())

    def test_pop(self):
        sz = 2
        stack = Stack(max_sz = sz)
        stack.push(43)
        stack.push(42)
        self.assertEqual(42, stack.pop())
        self.assertEqual(43, stack.pop())
        try:
            t = stack.pop()
            self.assertTrue(False, 'was able to pop from empty stack!')
        except IndexError as e:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

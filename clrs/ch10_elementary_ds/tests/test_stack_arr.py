import sys
sys.path.append('..')
import unittest

from stack_arr import Stack

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

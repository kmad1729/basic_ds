#!/usr/bin/env python3
'array implementation of stack'

import unittest

class Stack:

    def __init__(self, *, max_sz = 100):
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



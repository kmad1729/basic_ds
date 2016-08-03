#!/usr/bin/env python3

class Queue:

    def __init__(self, *, max_q_size = 100):
        self.head = 0
        self.tail = 0
        self._q = [None] * (max_q_size + 1)
        self.q_sz = (max_q_size + 1)

    def enqueue(self, elem):
        if self.tail == self.q_sz - 1:
            next_tail = 0
        else:
            next_tail = self.tail + 1

        if next_tail == self.head:
            raise IndexError('Overflow!')

        self._q[self.tail] = elem
        self.tail = next_tail

    def dequeue(self):
        ret = self._q[self.head]
        if self.head == self.tail:
            raise IndexError('Underflow!')

        if self.head == self.q_sz - 1:
            self.head = 0
        else:
            self.head += 1

        return ret

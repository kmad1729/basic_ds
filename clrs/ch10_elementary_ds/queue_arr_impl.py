import unittest

class Queue:

    def __init__(self, max_q_size = 100):
        self.head = 0
        self.tail = 0
        self._q = [None] * (max_q_size + 1)
        self.q_sz = (max_q_size + 1)

    def _is_empty(self):
        return self.head == self.tail

    def _is_full(self):
        if self.tail == self.q_sz - 1:
            return self.head == 0
        else:
            return self.q_sz + 1 == self.head
        
    def enqueue(self, elem):
        if self._is_full():
            raise IndexError('Overflow!')

        self._q[self.tail] = elem
        if self.tail == self.q_sz - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self._is_empty():
            raise IndexError('Underflow!')

        ret = self._q[self.head]

        if self.head == self.q_sz - 1:
            self.head = 0
        else:
            self.head += 1

        return ret

#### TESTS ####

class Test_Queue(unittest.TestCase):

    delim = '#' * 10

    def test_q_basic_funcs(self):
        q = Queue(max_q_size = 2)
        q.enqueue(5)
        q.enqueue(31)
        self.assertRaises(Exception, q.enqueue, 1)
        self.assertEqual(5, q.dequeue())

        q.enqueue(1)
        self.assertEqual(31, q.dequeue())
        self.assertEqual(1, q.dequeue())

        self.assertRaises(Exception, q.dequeue)

        q.enqueue(32)
        self.assertEqual(32, q.dequeue())

        self.assertRaises(Exception, q.dequeue)

        q.enqueue(-1e9)
        self.assertEqual(-1e9, q.dequeue())


if __name__ == '__main__':
    unittest.main()


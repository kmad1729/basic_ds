#!/usr/bin/env python3

import unittest
from prb_10_1_4 import Queue

class Test_Queue(unittest.TestCase):

    delim = '#' * 10

    def test_q_basic_funcs(self):
        q = Queue(max_q_size = 2)
        q.enqueue(5)
        q.enqueue(31)
        print (self.delim)
        try:
            q.enqueue(1)
        except Exception as e:
            print("caught exception ({})".format(e))
        self.assertEqual(5, q.dequeue())
        print (self.delim)

        q.enqueue(1)
        self.assertEqual(31, q.dequeue())
        self.assertEqual(1, q.dequeue())

        try:
            q.dequeue()
        except Exception as e:
            print("caught exception ({})".format(e))

        print (self.delim)
        q.enqueue(32)
        self.assertEqual(32, q.dequeue())

        try:
            q.dequeue()
        except Exception as e:
            print("caught exception ({})".format(e))


if __name__ == '__main__':
    unittest.main()


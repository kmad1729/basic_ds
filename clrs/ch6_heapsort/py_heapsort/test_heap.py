#!/usr/bin/env python3
'tests for heap.py function'

import unittest
from heap import max_heapify

class TestHeaps(unittest.TestCase):

    def test_max_heapify_basic(self):
        lst = [2, 5, 9, 4, 3, 4, 6, 2, 1, 0]
        print("before max heapify lst = {}".format(lst))
        max_heapify(lst, 0, len(lst))
        print("after  max_heapify(lst, 0, len(lst)). lst = {}".format(lst))
        exp_out = [9, 5, 6, 4, 3, 4, 2, 2, 1, 0]
        self.assertEqual(exp_out, lst)

    def test_max_heapify_left_sift(self):
        lst = [2, 12, 9, 4, 3, 4, 6, 2, 1, 0]
        max_heapify(lst, 0, len(lst))
        exp_out = [12, 4, 9, 2, 3, 4, 6, 2, 1, 0]
        self.assertEqual(exp_out, lst)



if __name__ == '__main__':
    unittest.main()

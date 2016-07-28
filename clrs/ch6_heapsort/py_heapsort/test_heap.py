#!/usr/bin/env python3
'tests for heap.py function'

from random import randint
import unittest

from heap import max_heapify, build_max_heap, heap_sort

class TestHeaps(unittest.TestCase):

    def setUp(self):
        self.rand_list = [randint(0, 50) for i in range(25)]

    def test_max_heapify_basic(self):
        lst = [2, 5, 9, 4, 3, 4, 6, 2, 1, 0]
        max_heapify(lst, 0, len(lst))
        exp_out = [9, 5, 6, 4, 3, 4, 2, 2, 1, 0]
        self.assertEqual(exp_out, lst)

    def test_max_heapify_left_sift(self):
        lst = [2, 12, 9, 4, 3, 4, 6, 2, 1, 0]
        max_heapify(lst, 0, len(lst))
        exp_out = [12, 4, 9, 2, 3, 4, 6, 2, 1, 0]
        self.assertEqual(exp_out, lst)

    def test_build_max_heap(self):
        lst = [2, 5, 8, 7, 4, 6, 9, 14, 6, 27]
        build_max_heap(lst)
        exp_out = [27, 14, 9, 7, 5, 6, 8, 2, 6, 4]
        self.assertEqual(exp_out, lst)

    def test_heap_sort(self):
        rand_list_copy = self.rand_list[:]
        rand_list_copy.sort()
        print("rand list = {self.rand_list}".format(self = self))
        heap_sort(self.rand_list)
        print("rand list sorted = {self.rand_list}".format(self = self))
        print('#' * 20)
        self.assertEqual(rand_list_copy, self.rand_list)

    def test_heap_sort_single_elem(self):
        lst = [5]
        heap_sort(lst)
        self.assertEqual([5], lst)

    def test_heap_sort_0_elem(self):
        lst = []
        heap_sort(lst)
        self.assertEqual([], lst)


if __name__ == '__main__':
    unittest.main()

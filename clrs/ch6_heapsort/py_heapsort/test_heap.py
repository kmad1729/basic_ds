#!/usr/bin/env python3
'tests for heap.py function'

from collections import deque
from random import randint
import unittest

from prob_6_5_6 import Queue_PQ

from heap import max_heapify, build_max_heap, heap_sort, \
    heap_max, heap_extract_max, _parent, heap_increase_key, \
    max_heap_insert

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

    def test_heap_max(self):
        lst = list(range(100, 0, -3))
        self.assertEqual(100, heap_max(lst))

    def test_heap_extract_max(self):
        lst = list(range(100, 0, -3))
        expected_len = len(lst)
        for i in range(100, 0, -3):
            exp_max = i
            self.assertEqual(exp_max, heap_extract_max(lst))
            expected_len -= 1
            self.assertEqual(expected_len, len(lst))

    def test__parent(self):
        ind_parent_map = {2 : 0, 1: 0, 5: 2, 8 : 3, 7 : 3, 3 : 1}
        for ind, parent in ind_parent_map.items():
            self.assertEqual(parent, _parent(ind))

    def test_heap_increase_key(self):
        lst = list(range(10))
        print("lst = {}".format(lst))
        build_max_heap(lst)
        print("lst after heap = {}".format(lst))
        print("increasing last elem key to 100")
        heap_increase_key(lst, len(lst) - 1, 100)
        print("lst after heap_increase_key = {}".format(lst))
        print('#' * 20)
        self.assertEqual(100, heap_max(lst))

    def test_max_heap_insert(self):
        max_heap = [27, 14, 9, 7, 5, 6, 8, 2, 6, 4]
        initial_len = len(max_heap)
        print("max_heap = {}".format(max_heap))
        i = 20

        print("inserting {i} to the max_heap".format(i = i))
        max_heap_insert(max_heap, i, -1)
        print("new_heap = {}".format(max_heap))
        self.assertEqual(len(max_heap), initial_len + 1)
        exp_new_heap = [27, 20, 9, 7, 14, 6, 8, 2, 6, 4, 5]
        self.assertEqual(exp_new_heap, max_heap)

        print("inserting {i} to the max_heap".format(i = i))
        max_heap_insert(max_heap, i, -1)
        print("new_heap = {}".format(max_heap))
        print("#" * 20)
        exp_new_heap = [27, 20, 20, 7, 14, 9, 8, 2, 6, 4, 5, 6]
        self.assertEqual(exp_new_heap, max_heap)

class Test_Queue_PQ(unittest.TestCase):
    
    def test_empty(self):
        q1 = Queue_PQ()
        self.assertTrue(q1.empty())

    def test_enqueue_dequeue(self):
        q1 = Queue_PQ()
        q2 = deque()
        for i in range(5):
            elem = randint(1, 500)
            q1.enqueue(elem)
            q2.append(elem)

        self.assertEqual(q1.dequeue(), q2.popleft())
        self.assertEqual(q1.dequeue(), q2.popleft())
        self.assertEqual(q1.front(), q2[0])

        for i in range(7):
            elem = randint(1, 500)
            q1.enqueue(elem)
            q2.append(elem)

        while len(q2) != 0:
            self.assertEqual(q1.dequeue(), q2.popleft())

        self.assertEqual(0, len(q1))



if __name__ == '__main__':
    unittest.main()

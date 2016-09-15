'efficiently compute median of a set of numbers given one by one'

from __future__ import division
from heapq import heappush, heappop
import unittest

class RunningMedian:
    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def insert(self, item):
        left_len = len(self.left_max_heap)
        right_len = len(self.right_min_heap)

        if left_len == right_len == 0:
            heappush(self.left_max_heap, -item)
            return

        if item < -self.left_max_heap[0]:
            heappush(self.left_max_heap, -item)
        else:
            heappush(self.right_min_heap, item)

        left_len = len(self.left_max_heap)
        right_len = len(self.right_min_heap)

        if right_len < left_len:
            l_pop = -heappop(self.left_max_heap)
            heappush(self.right_min_heap, l_pop)
        elif right_len > left_len:
            r_pop = heappop(self.right_min_heap)
            heappush(self.left_max_heap, -r_pop)

    def getMedian(self):
        left_len = len(self.left_max_heap)
        right_len = len(self.right_min_heap)

        if left_len > right_len:
            return -self.left_max_heap[0]
        elif left_len < right_len:
            return self.right_min_heap[0]
        else:
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2


class Test_RunningMedian(unittest.TestCase):
    def setUp(self):
        self.rm = RunningMedian()

    def test_insert(self):
        elems_to_inset = [
                (4, 4), 
                (0, 2), 
                (3, 3), 
                (5, 3.5),
                (1, 3),
                (2, 2.5),
                (6, 3)]
        for elem, exp_median in elems_to_inset:
            self.rm.insert(elem)

            self.assertEquals(exp_median, self.rm.getMedian(),
                    "expected median = {exp_median}; got = {calc_median} "
                    "after inserting element = {elem}".format(
                        exp_median = exp_median,
                        calc_median= self.rm.getMedian(),
                        elem = elem))




if __name__ == '__main__':
    unittest.main()

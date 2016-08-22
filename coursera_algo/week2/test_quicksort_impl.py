'tests for quick sort implemenation'

import unittest
from random import randint

from quicksort_impl import quicksort, partition

class TestQuickSort(unittest.TestCase):
    def test_partition(self):
        def default_pivot_ind(A, p, r):
            return p
        arr = [4, 5, 2, 1, 7, 6, 3]
        self.assertEqual(3, partition(arr, 0, len(arr) - 1, default_pivot_ind))
        self.assertEqual(2, partition(arr, 0, len(arr) - 1, default_pivot_ind))

    def test_quicksort(self):
        arr = [4, 5, 2, 1, 7, 6, 3]
        sorted_arr = sorted(arr)
        comps = quicksort(arr, 0, len(arr) - 1)
        #print("number of comparision = {}".format(comps))
        self.assertEqual(arr, sorted_arr)

    def test_comparisions_small(self):
        arr = list(range(1, 6))
        comps1 = quicksort(arr, 0, len(arr) - 1)
        comps2 = quicksort(arr, 0, len(arr) - 1, lambda A, p, r: r)
        #print("number of comparision for arr{} = {}".format(comps))
        #comparisions of sorted array should be (n - 1)(n) // 2
        self.assertEqual(10, comps1)
        self.assertEqual(10, comps2)

    def test_comparisions_large(self):
        def default_pivot_ind(A, p, r):
            return randint(p, r)
        arr = list(range(1, 600))
        comps1 = quicksort(arr, 0, len(arr) - 1, default_pivot_ind)
        print("number of comparision for arr = {}".format(comps1))
        self.assertEqual(arr, list(range(1, 600)))
        #comparisions of sorted array should be (n - 1)(n) // 2
        #self.assertEqual(17997000, comps1)
        #self.assertEqual(17997000, comps2)


if __name__ == '__main__':
    unittest.main()

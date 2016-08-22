'tests for quick sort implemenation'

import unittest

from quicksort_impl import quicksort, partition

class TestQuickSort(unittest.TestCase):
    def test_partition(self):
        arr = [4, 5, 2, 1, 7, 6, 3]
        def default_pivot_fun(A, p, r):
            return p
        self.assertEqual(3, partition(arr, 0, len(arr) - 1, default_pivot_fun))
        self.assertEqual(2, partition(arr, 0, len(arr) - 1, default_pivot_fun))

    def test_quicksort(self):
        def default_pivot_fun(A, p, r):
            return p
        arr = [4, 5, 2, 1, 7, 6, 3]
        sorted_arr = sorted(arr)
        comps = quicksort(arr, 0, len(arr) - 1, default_pivot_fun)
        #print("number of comparision = {}".format(comps))
        self.assertEqual(arr, sorted_arr)

    def test_comparisions_small(self):
        arr = list(range(1, 6))
        def default_pivot_fun1(A, p, r):
            return p
        def default_pivot_fun2(A, p, r):
            return r
        comps1 = quicksort(arr, 0, len(arr) - 1, default_pivot_fun1)
        comps2 = quicksort(arr, 0, len(arr) - 1, default_pivot_fun2)
        #print("number of comparision for arr{} = {}".format(comps))
        #comparisions of sorted array should be (n - 1)(n) // 2
        self.assertEqual(10, comps1)
        self.assertEqual(10, comps2)

    '''
    def test_comparisions_large(self):
        arr = list(range(1, 6001))
        def default_pivot_fun1(A, p, r):
            return p
        def default_pivot_fun2(A, p, r):
            return r
        comps1 = quicksort(arr, 0, len(arr) - 1, default_pivot_fun1)
        #comps2 = quicksort(arr, 0, len(arr) - 1, default_pivot_fun2)
        #print("number of comparision for arr{} = {}".format(comps))
        #comparisions of sorted array should be (n - 1)(n) // 2
        self.assertEqual(17997000, comps1)
        #self.assertEqual(17997000, comps2)
    '''


if __name__ == '__main__':
    unittest.main()

'tests for quick sort implemenation'

import unittest
from random import randint

from quicksort_impl import quicksort, partition

def read_inp_file(f_name):
    result = []
    with open(f_name, 'r') as f:
        for l in f:
            if l.strip() != '':
                result.append(int(l))
    return result

def first_elem_piv(A, p, r):
    return p
def last_elem_piv(A, p, r):
    return r

def median_of_3_piv(A, p , r):
    first_elem = (A[p], p)
    last_elem = (A[r], r)
    mid_elem_ind = p + (r - p) // 2
    mid_elem = (A[mid_elem_ind], mid_elem_ind)
    return sorted([first_elem, last_elem, mid_elem])[1][1]

class TestQuickSort(unittest.TestCase):
    def test_partition(self):
        arr = [4, 5, 2, 1, 7, 6, 3]
        self.assertEqual(3, partition(arr, 0, len(arr) - 1, first_elem_piv))
        self.assertEqual(2, partition(arr, 0, len(arr) - 1, first_elem_piv))

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

    def test_instructor_test_cases(self):
        d_10_elem = read_inp_file('inp1.txt')
        self.assertEqual(25, quicksort(d_10_elem[:], 0, len(d_10_elem) - 1, first_elem_piv))
        self.assertEqual(29, quicksort(d_10_elem[:], 0, len(d_10_elem) - 1, last_elem_piv))
        self.assertEqual(21, quicksort(d_10_elem[:], 0, len(d_10_elem) - 1, median_of_3_piv))

        d_100_elem = read_inp_file('100.txt')
        self.assertEqual(615, quicksort(d_100_elem[:], 0, len(d_100_elem) - 1, first_elem_piv))
        self.assertEqual(587, quicksort(d_100_elem[:], 0, len(d_100_elem) - 1, last_elem_piv))
        self.assertEqual(518, quicksort(d_100_elem[:], 0, len(d_100_elem) - 1, median_of_3_piv))

        d_1000_elem = read_inp_file('1000.txt')
        self.assertEqual(10297, quicksort(d_1000_elem[:], 0, len(d_1000_elem) - 1, first_elem_piv))
        self.assertEqual(10184, quicksort(d_1000_elem[:], 0, len(d_1000_elem) - 1, last_elem_piv))
        self.assertEqual(8921, quicksort(d_1000_elem[:], 0, len(d_1000_elem) - 1, median_of_3_piv))




if __name__ == '__main__':
    unittest.main()

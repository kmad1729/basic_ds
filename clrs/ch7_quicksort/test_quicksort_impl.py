'tests for quicksort implementation'

from quicksort_impl import quicksort, partition

from random import randint
import unittest

class Test_Quicksort_impl(unittest.TestCase):
    def test_partition(self):
        lst1 = [2, 5, 4, 7, 3, 1, 6]
        self.assertEqual(5, partition(lst1, 0, len(lst1) - 1))
        expected_lst = [2, 5, 4, 3, 1, 6, 7]
        self.assertEqual(expected_lst, lst1)
        self.assertEqual(6, partition(lst1, 0, len(lst1) - 1))
        self.assertEqual(expected_lst, lst1)

        self.assertEqual(0, partition(lst1, 0, len(lst1) - 3))
        expected_lst = [1, 5, 4, 3, 2, 6, 7]
        self.assertEqual(expected_lst, lst1)

        lst2 = [5] * 5
        self.assertEqual(0, partition(lst2, 0, len(lst2) - 1))

    def test_quicksort(self):
        lst1 = [2, 5, 4, 7, 3, 1, 6]
        sorted_list = sorted(lst1)
        quicksort(lst1, 0, len(lst1) - 1)
        self.assertEqual(sorted_list, lst1)

        lst2 = [5] * 10
        quicksort(lst2, 0, len(lst2) - 1)
        self.assertEqual(lst2, [5] * 10)

        lst3 = []
        quicksort(lst3, 0, len(lst3) - 1)
        self.assertEqual(lst3, [])

        size = 100000
        rand_arr = [randint(0, 200) for i in range(size)]
        sorted_rand_arr = sorted(rand_arr)

        quicksort(rand_arr, 0, size - 1)
        self.assertEqual(sorted_rand_arr, rand_arr)




if __name__ == '__main__':
    unittest.main()

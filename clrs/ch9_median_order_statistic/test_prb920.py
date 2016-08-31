import unittest
from random import randint

from prb_9_2_0 import randomized_partition, random_select


class Test_randomized_partition(unittest.TestCase):

    def test_basic_functionality(self):
        sz = 100
        A = [randint(-20, 20) for i in range(sz)]
        part_ind = randomized_partition(A, 0, sz - 1)

        for i in range(part_ind):
            self.assertTrue(A[i] < A[part_ind])

        for i in range(part_ind + 1, sz):
            self.assertTrue(A[i] >= A[part_ind])

class Test_randomize_select(unittest.TestCase):
    def test_basic_functionality(self):
        A = [7, 1, 11, 3, 12, 4, 9, 2, 10, 8, 5, 6]

        i = 6
        self.assertEqual(i, random_select(A, 0, len(A) - 1, i))
        print("after finding {}th smallest element A -->".format(i))
        print(A)

        i = 3
        self.assertEqual(i, random_select(A, 0, len(A) - 1, i))
        print("after finding {}rd smallest element A -->".format(i))
        print(A)


        i = 1
        self.assertEqual(i, random_select(A, 0, len(A) - 1, i))
        print("after finding {}st smallest element A -->".format(i))
        print(A)

if __name__ == '__main__':
    unittest.main()



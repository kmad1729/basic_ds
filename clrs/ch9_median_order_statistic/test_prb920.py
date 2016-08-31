import unittest
from random import randint

from prb_9_2_0 import randomized_partition


class Test_randomized_partition(unittest.TestCase):

    def test_basic_functionality(self):
        sz = 100
        A = [randint(-5, 20) for i in range(sz)]
        part_ind = randomized_partition(A, 0, sz - 1)

        for i in range(part_ind):
            self.assertTrue(A[i] < A[part_ind])

        for i in range(part_ind + 1, sz):
            self.assertTrue(A[i] >= A[part_ind])

if __name__ == '__main__':
    unittest.main()



'compute the k closest stars to earth. Assume earth is a (0, 0, 0)'

import unittest
from heapq import heappush, heappushpop, heappop

def get_k_closest(lst, k = 3):
    h = []
    for p in lst:
        dist = p[0] ** 2 + p[1] ** 2 + p[2] ** 2

        if len(h) < k:
            heappush(h, (-dist, p))
        else:
            heappushpop(h, (-dist, p))

    result = []
    while len(h) != 0:
        result.append(heappop(h)[1])

    return result



class TestKClosest(unittest.TestCase):
    def test_basic_functionality(self):
        stars = [ (1, 0, 9), (-1, 1, 3), (3, 4, 0), (3, 1, 2), (3, 1, 1)]
        k = 3
        expected_out = [(3, 1, 2), (-1, 1, 3), (3, 1, 1)]
        self.assertEqual(expected_out, get_k_closest(stars, k))

    def test_test_all_dist_equal(self):
        stars = [(3, 4, 0), (4, 3, 0), (4, 0, 3), (0, 3, 4), (3, 0, 4)]
        expected_out = [(3, 4, 0), (4, 0, 3), (4, 3, 0)]
        k = 3
        self.assertEqual(expected_out, get_k_closest(stars, k))

    def test_k_greater_than_len(self):
        stars = [(3, 4, 0), (4, 3, 0)]
        expected_out = [(3, 4, 0), (4, 3, 0)]
        k = 3
        self.assertEqual(expected_out, get_k_closest(stars, k))


if __name__ == '__main__':
    unittest.main()

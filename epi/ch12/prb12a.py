'for a sorted array find index of elem greater than the key'

import unittest
from bisect import bisect_right

def my_bisect_right(lst, elem):
    if elem >= lst[-1]:
        return len(lst)
    if elem < lst[0]:
        return 0

    #elem is in array range
    result = len(lst)
    l = 0
    u = len(lst) - 1

    while l <= u:
        m = l + (u - l) // 2
        if elem == lst[m]:
            result = m + 1
            l = m + 1
        elif elem < lst[m]:
            result = m
            u = m - 1
        else:
            result = m + 1
            l = m + 1

    return result


class Test_GetFirstOccurence(unittest.TestCase):

    def test_basic_functionality(self):
        lst = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        tgt = 108
        self.assertEqual(bisect_right(lst, tgt) , my_bisect_right(lst, tgt))
        tgt = -13
        self.assertEqual(bisect_right(lst, tgt) , my_bisect_right(lst, tgt))
        tgt = -14
        self.assertEqual(bisect_right(lst, tgt) , my_bisect_right(lst, tgt))
        tgt = 401
        self.assertEqual(bisect_right(lst, tgt) , my_bisect_right(lst, tgt))
        tgt = 400
        self.assertEqual(bisect_right(lst, tgt) , my_bisect_right(lst, tgt))
        tgt = 404
        self.assertEqual(bisect_right(lst, tgt) , my_bisect_right(lst, tgt))

    def test_all_inp_list_same(self):
        lst = [255] * 10
        self.assertEqual(bisect_right(lst, 255), my_bisect_right(lst, 255))
        self.assertEqual(bisect_right(lst, 256), my_bisect_right(lst, 256))
        self.assertEqual(bisect_right(lst, 206), my_bisect_right(lst, 206))

if __name__ == '__main__':
    unittest.main()

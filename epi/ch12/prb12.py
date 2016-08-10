'search a sorted array for the first occurence of k'

import unittest

def get_first_occur(lst, k):
    l = 0
    u = len(lst) - 1
    while l <= u:
        m = l + (u - l) // 2
        if lst[m] == k:
            if m == 0:
                return 0
            if lst[m - 1] == k:
                u = m - 1
            else:
                return m
        elif lst[m] < k:
            l = m + 1
        else:
            u = m - 1

    return -1


class Test_GetFirstOccurence(unittest.TestCase):

    def test_basic_functionality(self):
        lst = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        self.assertEqual(3, get_first_occur(lst, 108))
        self.assertEqual(6, get_first_occur(lst, 285))
        self.assertEqual(0, get_first_occur(lst, -14))
        self.assertEqual(9, get_first_occur(lst, 401))
        self.assertEqual(-1, get_first_occur(lst, -21))
        self.assertEqual(-1, get_first_occur(lst, -11))
        self.assertEqual(-1, get_first_occur(lst, 284))
        self.assertEqual(-1, get_first_occur(lst, 402))

    def test_all_inp_list_same(self):
        lst = [255] * 10
        tgt = 255
        self.assertEqual(0, get_first_occur(lst, tgt))

if __name__ == '__main__':
    unittest.main()

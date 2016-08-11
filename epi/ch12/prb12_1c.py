'search a sorted array for the first and last occurence of elem'

import unittest

def get_first_last_occur(lst, elem):
    l = 0
    u = len(lst) - 1
    low, high = -1, -1
    while l <= u:
        m = l + (u - l) // 2
        if elem == lst[m]:
            low, high = m, m
            break
        elif elem < lst[m]:
            u = m - 1
        else:
            l = m + 1
    if low == -1:
        return (-1, -1)

    if low != 0 and lst[low - 1] == elem:
        l, u = 0, low - 1
        while l <= u:
            m = l + (u - l) // 2
            if elem == lst[m]:
                low = m
                u = m - 1
            elif elem < lst[m]:
                u = m - 1
            else:
                l = m + 1
    if high != len(lst) - 1 and lst[high + 1] == elem:
        l, u = high + 1, len(lst) - 1
        while l <= u:
            m = l + (u - l) // 2
            if elem == lst[m]:
                high = m
                l = m + 1
            elif elem < lst[m]:
                u = m - 1
            else:
                l = m + 1

    return (low, high)



class Test_GetFirstLastOccurence(unittest.TestCase):

    def test_basic_functionality(self):
        lst = [-13, -9, -9, -9, 3, 5, 5, 5, 5, 9, 9, 13, 56, 56]
        self.assertEqual((0, 0), get_first_last_occur(lst, -13))
        self.assertEqual((12, 13), get_first_last_occur(lst, 56))
        self.assertEqual((-1, -1), get_first_last_occur(lst, 54))
        self.assertEqual((1, 3), get_first_last_occur(lst, -9))
        self.assertEqual((4, 4), get_first_last_occur(lst, 3))

    def test_all_inp_list_same(self):
        lst = [255] * 10
        tgt = 255
        self.assertEqual((0, 9), get_first_last_occur(lst, tgt))

if __name__ == '__main__':
    unittest.main()

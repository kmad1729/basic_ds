'''given an unsorted array A of n integers with A[0] >= A[1] and A[n - 2] <= A[n-1],
find a local minimum 'i' s.t A[i] is <= to its neighbors
'''

import unittest

def get_local_minimum(lst):
    assert len(lst) >= 3
    assert lst[0] >= lst[1]
    assert lst[-1] >= lst[-2]

    l, u = 0, len(lst) - 1

    while (u - l + 1) >= 3:
        m = l + (u - l) // 2
        if (u - l + 1) <= 4:
            if lst[m - 1] >= lst[m] <= lst[m + 1]:
                return m
            else:
                return m + 1
        if lst[m] >= lst[l]:
            u = m
        else:
            if lst[m] >= lst[u]:
                l = m
            else:
                l += 1
                u -= 1
    return -1


class Test_get_local_min(unittest.TestCase):

    def _basic_test(self, lst):
        loc_min = get_local_minimum(lst)
        print('loc min for {} = {}'.format(lst, loc_min))
        self.assertTrue(lst[loc_min - 1] >= lst[loc_min] <= lst[loc_min + 1])

    def test_basic_functionality(self):
        self._basic_test([12, 9, 7, 10, 16])
        self._basic_test([12, 8, 16, 14, 15])
        self._basic_test([13, 11, 9, 8, 9])
        self._basic_test([13, 9, 6, 4, 5])
        self._basic_test([7, 4, 2, 6])
        self._basic_test([6, 2, 4, 7])
        self._basic_test([12, 8, 9, 6, 9, 7, 8])
        self._basic_test([49, 36, 12, 23, 86, 47, 47, 73, 75, 85])



    def test_all_inp_list_same(self):
        lst = [255] * 10
        self._basic_test(lst)

if __name__ == '__main__':
    unittest.main()

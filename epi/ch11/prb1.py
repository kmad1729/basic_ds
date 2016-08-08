'''w.a.p that takes as input a set of sorted sequences and computes union of the 
sequences as a sorted sequence'''

from heapq import heappush, heappop
import unittest


def merge_sorted(*args):
    h = []
    result = []
    for i, l in enumerate(args):
        if len(l) > 0:
            heappush(h, (l[0], i, 0))

    while len(h) != 0:
        elem, list_ind, ind_in_list = heappop(h)
        result.append(elem)
        lst = args[list_ind]
        ind_in_list += 1
        if ind_in_list < len(lst):
            heappush(h, (lst[ind_in_list], list_ind, ind_in_list))

    return result


class TestSol(unittest.TestCase):

    def test_basic_functionality(self):
        args1 = [ [3, 5, 7], [0, 6], [0, 6, 28]]

        self.assertEqual([0, 0, 3, 5, 6, 6, 7, 28],
                merge_sorted(*args1))

if __name__ == '__main__':
    unittest.main()

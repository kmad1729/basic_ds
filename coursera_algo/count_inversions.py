'count the number of inversions for a givne array'

def count_and_sort(A):
    n = len(A)
    if n <= 1:
        return (A, 0)
    (l1, x) = count_and_sort(A[:n//2])
    (l2, y) = count_and_sort(A[n//2:])
    (l3, z) = count_split_inv(l1, l2)
    return (l3, x + y + z)

def count_split_inv(l1, l2):
    i, j, result = 0, 0, 0
    k = 0
    result_list = [None] * (len(l1) + len(l2))

    while k < (len(l1) + len(l2)):
        if i != len(l1) and j != len(l2):
            if l1[i] <= l2[j]:
                result_list[k] = l1[i]
                i += 1
            else:
                result_list[k] = l2[j]
                j += 1
                result += (len(l1) - i)
        else:
            if i == len(l1):
                result_list[k] = l2[j]
                j += 1
            else:
                result_list[k] = l1[i]
                i += 1
        k += 1

    return (result_list, result)

def get_inversion(A):
    sorted_arr, invs = count_and_sort(A)
    return invs

import unittest

class Test_Count_inversion(unittest.TestCase):

    def test_count_inv(self):
        lst = [1, 3, 5, 2, 4, 6]
        self.assertEqual(3, get_inversion(lst))
        lst2 = [6, 5, 4, 3, 2, 1]
        self.assertEqual(15, get_inversion(lst2))
        lst3 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(0, get_inversion(lst3))




if __name__ == '__main__':
    unittest.main()



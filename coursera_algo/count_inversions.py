'count the number of inversions for a givne array'

def count_and_sort(A, start, end):
    n = end - start
    if n <= 1:
        return 0
    mid = start + n // 2
    x = count_and_sort(A, start, mid)
    y = count_and_sort(A, mid, end)
    z = count_split_inv(A, start, end, mid)
    return x + y + z

def count_split_inv(A, start, end, mid):
    #A[start...mid) is sorted
    #A[mid...end) is sorted
    i, j, result = 0, 0, 0

    left = A[start:mid] + [1e9]
    right = A[mid:end] + [1e9]

    for k in range(start, end):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
            if left[i] != 1e9:
                result += (len(left) - i - 1)

    return result

def get_inversion(A):
    #print("before sort A = {}".format(A))
    invs = count_and_sort(A, 0, len(A))
    #print("after sort A = {}".format(A))
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

        lst4 = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 
                33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 
                0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
        self.assertEqual(590, get_inversion(lst4))

        lst5 = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 
                8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 
                67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 
                63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 
                75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 
                34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 
                31, 85, 33, 54]
        self.assertEqual(2372, get_inversion(lst5))



if __name__ == '__main__':
    unittest.main()



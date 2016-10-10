
import random
import unittest

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        curr = A[i]
        while j >= 0 and A[j] > curr:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = curr

class Test_insertion_sort(unittest.TestCase):
    def test_basic(self):
        test_size = 10000
        rand_list = [random.randint(-1e6, 1e6) for i in range(test_size)]
        list_copy = rand_list[:]
        insertion_sort(rand_list)

        self.assertEqual(rand_list, sorted(list_copy))

    def test_empty(self):
        l1 = []
        insertion_sort(l1)
        self.assertEqual(l1, [])

    def test_single_elem(self):
        l1 = [4]
        insertion_sort(l1)
        self.assertEqual(l1, [4])

if __name__ == '__main__':
    unittest.main()



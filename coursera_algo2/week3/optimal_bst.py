'''Given a sorted list of keys 1, 2, 3, 4, 5
with search probabilities     p1,p2,p3,p4,p5
compute an optimal binary search tree that the average search cost C(T) is minimum
'''

from pprint import pprint

def get_avg_search_cost(inp):
    'inp -> [p1,p2,p3,p4,p5,p6..] with 1,2,3,4.. in sorted order'
    n = len(inp)
    A = [[0] * n for i in range(n)]
    print(A)
    
    for i in range(n):
        A[i][i] = inp[i]

    for L in range(2, n + 1):
        #length of range can vary from 2 to n
        for i in range(n - L + 1):
            #starting element can range from 0 to n - L 
            j = i + L - 1
            #last index = i + L - 1
            print('i = {i}, j = {j}, L = {l}'.format(i=i,j=j,l=L))
            A[i][j] = 1e9
            for r in range(i, j + 1):
                c = (A[i][r-1] if r > i else 0) + \
                        (A[r+1][j] if r < j else 0) + \
                        sum(inp[i:j+1])
                if c  < A[i][j]:
                    A[i][j] = c
    pprint(A)
    return A[0][n-1]


import unittest

class Test_min_avg_search_cost(unittest.TestCase):

    def test_1(self):
        probs = [2, 98]
        self.assertEqual(102, get_avg_search_cost(probs))

    def test_1(self):
        probs = [2, 98]
        self.assertEqual(102, get_avg_search_cost(probs))

    '''
    def test_3(self):
        probs = [34, 8, 50]
        self.assertEqual(142, get_avg_search_cost(probs))

    def test_2(self):
        probs = [2, 23, 73, 1]
        self.assertEqual(127, get_avg_search_cost(probs))
    '''

if __name__ == '__main__':
    unittest.main()


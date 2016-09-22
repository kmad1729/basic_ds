import unittest
from dijkstra_algo import *

class Test_heap(unittest.TestCase):

    def setUp(self):
        self.h = []

    def test_heap_insert(self):
        h = []
        n_h_p_m = {}
        exp_len = 0
        dijkstra_heap_insert(h, {'node':'A', 'dist':3}, n_h_p_m)
        exp_len += 1

        dijkstra_heap_insert(h, {'node':'B', 'dist':6}, n_h_p_m)
        exp_len += 1

        dijkstra_heap_insert(h, {'node':'C', 'dist':0}, n_h_p_m)
        exp_len += 1

        self.assertEquals(len(h), exp_len)
        self.assertEquals(h[0], {'node':'C', 'dist':0})

        self.assertEquals(0, n_h_p_m['C'])
        self.assertEquals(1, n_h_p_m['B'])
        self.assertEquals(2, n_h_p_m['A'])

if __name__ == '__main__':
    unittest.main()


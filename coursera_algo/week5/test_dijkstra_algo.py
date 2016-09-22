import unittest
from dijkstra_algo import *

class Test_heap(unittest.TestCase):

    def setUp(self):
        self.h = []
        self.n_h_p_m = {}
        dijkstra_heap_insert(self.h, {'node':'A', 'dist':3}, self.n_h_p_m)
        dijkstra_heap_insert(self.h, {'node':'B', 'dist':6}, self.n_h_p_m)
        dijkstra_heap_insert(self.h, {'node':'C', 'dist':0}, self.n_h_p_m)
        dijkstra_heap_insert(self.h, {'node':'D', 'dist':8}, self.n_h_p_m)

    def test_heap_decrease_key
    def test_heap_insert(self):
        exp_len=4
        self.assertEquals(len(self.h), exp_len)
        self.assertEquals(self.h[0], {'node':'C', 'dist':0})

        self.assertEquals(0, self.n_h_p_m['C'])
        self.assertEquals(1, self.n_h_p_m['B'])
        self.assertEquals(2, self.n_h_p_m['A'])
        self.assertEquals(3, self.n_h_p_m['D'])

if __name__ == '__main__':
    unittest.main()

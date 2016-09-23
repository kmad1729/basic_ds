import unittest
from dijkstra_algo import *

class Test_heap(unittest.TestCase):

    def setUp(self):
        self.h = []
        self.n_h_p_m = {}
        dijkstra_heap_insert(self.h, {'node':'A', 'dist':3}, self.n_h_p_m)
        dijkstra_heap_insert(self.h, {'node':'B', 'dist':6}, self.n_h_p_m)
        dijkstra_heap_insert(self.h, {'node':'C', 'dist':2}, self.n_h_p_m)
        dijkstra_heap_insert(self.h, {'node':'D', 'dist':8}, self.n_h_p_m)

    def test_heap_extract_min(self):
        min_dist, min_node = dijkstra_heap_extract_min(self.h, self.n_h_p_m)
        self.assertEquals(min_dist, 2)
        self.assertEquals(min_node, 'C')
        self.assertEquals(0, self.n_h_p_m['A'])
        self.assertEquals(1, self.n_h_p_m['B'])
        self.assertEquals(2, self.n_h_p_m['D'])

        self.assertEquals(len(self.h), 3)

        self.assertEquals((3, 'A'), dijkstra_heap_extract_min(self.h, self.n_h_p_m))
        self.assertEquals(len(self.h), 2)

        self.assertEquals((6, 'B'), dijkstra_heap_extract_min(self.h, self.n_h_p_m))
        self.assertEquals(len(self.h), 1)
        self.assertEquals((8, 'D'), dijkstra_heap_extract_min(self.h, self.n_h_p_m))
        self.assertEquals(len(self.h), 0)



    def test_heap_decrease_key(self):
        new_data = {'node':'D', 'dist':1}
        dijkstra_heap_decrease_key(self.h, len(self.h) - 1, 1, self.n_h_p_m)
        self.assertEquals(self.h[0], {'node':'D', 'dist':1})

        self.assertEquals(0, self.n_h_p_m['D'])
        self.assertEquals(1, self.n_h_p_m['C'])
        self.assertEquals(2, self.n_h_p_m['A'])
        self.assertEquals(3, self.n_h_p_m['B'])

    def test_heap_insert(self):
        exp_len=4
        self.assertEquals(len(self.h), exp_len)
        self.assertEquals(self.h[0], {'node':'C', 'dist':2})

        self.assertEquals(0, self.n_h_p_m['C'])
        self.assertEquals(1, self.n_h_p_m['B'])
        self.assertEquals(2, self.n_h_p_m['A'])
        self.assertEquals(3, self.n_h_p_m['D'])

class Test_Dijkstra_Algo(unittest.TestCase):
    def setUp(self):
        self.G = {
                1:[(2,1), (3,6)],
                2:[(1,1), (3,3), (4,2), (5,5)],
                3:[(1,6), (2,3), (4,10)],
                4:[(3,10), (2,2), (5,1)],
                5:[(2,5), (4,1)],
                }

    def test_dijkstras(self):
        exp_dists_from_1 = { 1:0, 2:1, 3:4, 4:3, 5:4}
        self.assertEquals(exp_dists_from_1, dijkstra_get_shortest_paths_from_single_node(
            self.G, 1))
        exp_dists_from_2 = { 1:1, 2:0, 3:3, 4:2, 5:3}
        self.assertEquals(exp_dists_from_2, dijkstra_get_shortest_paths_from_single_node(
            self.G, 2))

if __name__ == '__main__':
    unittest.main()


import unittest

from find_min_cut import reduce_graph, get_random_edge

class Test_find_min_cut(unittest.TestCase):

    def setUp(self):
        self.G = {
                1: [2, 3],
                2: [1, 3, 4],
                3: [1, 2, 4],
                4: [2, 3],
                }

    def test_get_random_edge(self):
        rand_src, rand_dest = get_random_edge(self.G)
        self.assertTrue(rand_dest in self.G[rand_src])
        self.assertTrue(rand_src in self.G[rand_dest])

    def test_reduce_graph(self):
        new_id = len(self.G) + 1
        new_g = reduce_graph(self.G, new_id)

if __name__ == '__main__':
    unittest.main()

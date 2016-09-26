import unittest

from find_min_cut import contract_graph, get_random_edge, \
        kargers_algo

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

    def test_contract_graph(self):
        edge_to_delete = (1, 3)
        contract_graph(self.G, edge_to_delete)
        expected_graph = {
                2: [3, 4, 3], 
                3: [2, 4, 2], 
                4: [2, 3]}
        self.assertEquals(expected_graph, self.G)

        edge_to_delete = (3, 2)
        contract_graph(self.G, edge_to_delete)
        expected_graph = {
                3:[4, 4],
                4:[3, 3],
                }
        self.assertEquals(expected_graph, self.G)

    def test_kargers_algo(self):
        kargers_algo(self.G)
        print(self.G)
        self.assertEquals(2, len(self.G))

        for k in self.G:
            self.assertEquals(len(set(self.G[k])), 1)

if __name__ == '__main__':
    unittest.main()

import unittest

from prb3_btree_lca import *
from binary_tree import BinaryTree, get_toy_binary_tree, get_toy_binary_tree2

class TestLCA(unittest.TestCase):
    def test_lca(self):
        tr = get_toy_binary_tree2()
        n0 = tr.root['left']['left'] #9
        n1 = tr.root['left']['right']['left'] #8

        lca_node = get_LCA(tr, n0, n1)
        self.assertEqual(lca_node['data'], 3)

    def test_lca2(self):
        tr = get_toy_binary_tree2()
        n0 = tr.root['right']['left']['left']['right'] #23
        n1 = tr.root['right']['right']['right'] #86

        lca_node = get_LCA(tr, n0, n1)
        self.assertEqual(lca_node['data'], 8)

    def test_lca_equal_nodes(self):
        tr = get_toy_binary_tree2()
        n0 = tr.root['right']['left']['left']['right'] #23
        n1 = tr.root['right']['left']['left']['right'] #23

        lca_node = get_LCA(tr, n0, n1)
        self.assertEqual(lca_node['data'], 23)



if __name__ == '__main__':
    unittest.main()

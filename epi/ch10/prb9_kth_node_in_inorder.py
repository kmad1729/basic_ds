import unittest
'''Write a program that efficiently computes the kth node appearing in
an inorder traversal. Assume that each node stores the number of nodes
in the subtree rooted at that node.

Hint: Use divide and conquer
'''

from binary_tree import BinaryTree, get_toy_binary_tree2

def get_kth_node_in_order(n, k):
    assert k <= n['node_count'], \
            "there are {nc} (greater than {k}) nodes in the tree".format(
                    nc = n['node_count'], k = k)
    if n['left']:
        curr_node_ind = n['left']['node_count'] + 1
    else:
        curr_node_ind = 1

    if curr_node_ind == k:
        return n['data']
    elif k < curr_node_ind:
        return get_kth_node_in_order(n['left'], k)
    else:
        return get_kth_node_in_order(n['right'], k - curr_node_ind)

def util_generate_node_count_data(n):
    if n == None:
        return 0

    if n['left'] == None and n['right'] == None:
        n['node_count'] = 1
    else:
        n['node_count'] = util_generate_node_count_data(n['left']) +\
                util_generate_node_count_data(n['right']) + 1

    return n['node_count']


class Test_prb9(unittest.TestCase):

    def test_generate_node_count_data(self):
        tr = get_toy_binary_tree2()
        util_generate_node_count_data(tr.root)
        tr_in_order = [9, 3, 8, 6, 5, 98, 7, 23, 42, 8, 0, 28, 86]
        self.assertEqual(tr.root['node_count'], len(tr_in_order))
        self.assertEqual(tr.root['left']['node_count'], 4)
        self.assertEqual(tr.root['left']['left']['node_count'], 1)
        self.assertEqual(tr.root['right']['left']['node_count'], 4)
        
    def test_generate_node_count_data2(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        util_generate_node_count_data(tr.root)
        self.assertEqual(tr.root['node_count'], len(in_ordr))

    def test_generate_node_count_data3(self):
        in_ordr = [3, 4, 1, 2, 6, 8, 12, 13, 16, 21]
        pre_ordr = [3, 6, 4, 2, 1, 16, 12, 8, 13, 21]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        util_generate_node_count_data(tr.root)
        self.assertEqual(tr.root['node_count'], len(in_ordr))
        self.assertEqual(tr.root['right']['node_count'], len(in_ordr) - 1)
        self.assertEqual(tr.root['right']['right']['node_count'], 5)

    def _test_kth_in_order(self, in_order_traversal, n):
        for i, num in enumerate(in_order_traversal, 1):
            self.assertEqual(get_kth_node_in_order(n, i), num)

    def test_get_kth_node_in_order1(self):
        tr = get_toy_binary_tree2()
        util_generate_node_count_data(tr.root)
        tr_in_order = [9, 3, 8, 6, 5, 98, 7, 23, 42, 8, 0, 28, 86]
        self._test_kth_in_order(tr_in_order, tr.root)

    def test_get_kth_node_in_order2(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        util_generate_node_count_data(tr.root)
        self._test_kth_in_order(in_ordr, tr.root)

    def test_get_kth_node_in_order3(self):
        in_ordr = [3, 4, 1, 2, 6, 8, 12, 13, 16, 21]
        pre_ordr = [3, 6, 4, 2, 1, 16, 12, 8, 13, 21]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        util_generate_node_count_data(tr.root)
        self._test_kth_in_order(in_ordr, tr.root)


if __name__ == '__main__':
    unittest.main()

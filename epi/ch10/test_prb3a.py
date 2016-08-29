from prb3a_btree_get_max_full_subtree import get_largest_complete_subtree_size
from binary_tree import BinaryTree

import unittest

class Test_prb3A(unittest.TestCase):
    def test_basic_functionality1(self):
        in_order = [7, 8, 55, 46, 91, 16, 13, 18, 12, 9, 14]
        pre_order = [8, 7, 12, 16, 46, 55, 91, 13, 18, 14, 9]

        tr = BinaryTree.from_in_and_pre_order_traversal(in_order, pre_order)

        post_order = [7, 55, 91, 46, 18, 13, 16, 9, 14, 12, 8]

        print('tr post order ->')
        tr.printPostOrder()
        print('expected -->')
        print('(' + ' '.join(map(str, post_order)) + ')')

        self.assertEqual(3, get_largest_complete_subtree_size(tr))

    def test_basic_functionality2(self):
        in_order = [7, 8, 55, 46, 91, 16, 102, 13, 18, 12, 9, 14]
        pre_order = [8, 7, 12, 16, 46, 55, 91, 13, 102, 18, 14, 9]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_order, pre_order)


        self.assertEqual(7, get_largest_complete_subtree_size(tr))

    def test_basic_functionality1(self):
        in_order = [4, 7, 8, 16, 12]
        pre_order = [8, 7, 4, 12, 16]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_order, pre_order)


        self.assertEqual(1, get_largest_complete_subtree_size(tr))



if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3

'tests for binary_tree.py'

from binary_tree import BinaryTree, BinarySearchTree,\
        get_toy_binary_tree, get_empty_tree, get_toy_binary_search_tree, \
        BinaryTreeWithPrarent

import unittest


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tr = get_toy_binary_tree()
        self.empty_tr = get_empty_tree()
        self.bst = get_toy_binary_search_tree()

    def test_basic_functionality(self):
        self.assertTrue(self.tr)
        self.assertTrue(self.bst)

    def test_size(self):
        self.assertEqual(0, self.empty_tr.size())
        self.assertEqual(9, self.tr.size())
        self.assertEqual(12, self.bst.size())

    def test_maxDepth(self):
        self.assertEqual(0, self.empty_tr.maxDepth())
        self.assertEqual(4, self.tr.maxDepth())
        self.assertEqual(5, self.bst.maxDepth())

    def test_printInOrder(self):
        print("printing bst -->")
        self.bst.printInOrder()
        print("printing normal tree -->")
        self.tr.printInOrder()
        print("printing empty tree")
        self.empty_tr.printInOrder()

    def test_build_binary_tree(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        post_order = [1, 16, 14, 86, 29, 3, 18, 63, 141, 69, 4]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        print("printing post order -->")
        tr.printPostOrder()
        print("expected order -->")
        print("(" + " ".join(map(str, post_order)) + " )")
        self.assertEqual(5, tr.maxDepth())

    def test_binary_tree_in_order_path(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        self.assertEqual(tr.getInOrderPath(), in_ordr)


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):

        self.empty_bst = BinarySearchTree()
        self.single_node_bst = BinarySearchTree()
        self.single_node_bst.insert(-1)

        self.small_bst = BinarySearchTree()
        self.small_bst.insert(43)
        self.small_bst.insert(43)
        self.small_bst.insert(-2)
        self.small_bst.insert(102)

        self.toy_bst = get_toy_binary_search_tree()

    def test_maxValue(self):
        self.assertRaises(TypeError, self.empty_bst.maxValue)
        self.assertEqual(-1, self.single_node_bst.maxValue())
        self.assertEqual(102, self.small_bst.maxValue())
        self.assertEqual(102, self.toy_bst.maxValue())

    def test_minValue(self):
        self.assertRaises(TypeError, self.empty_bst.minValue)
        self.assertEqual(-1, self.single_node_bst.minValue())
        self.assertEqual(-2, self.small_bst.minValue())
        self.assertEqual(-1, self.toy_bst.minValue())

    def test_delete_node(self):
        values = [7, 3, 23, 1, 5, 9, 52, 2, 4, 36]
        tr = BinarySearchTree()
        for v in values:
            tr.insert(v)
        tr.populate_parent()

        expected_in_order_tree_after_7_delete = \
                [1, 2, 3, 4, 5, 9, 23, 36, 52]
        tr.delete_data(7)
        self.assertEquals(tr.getInOrderPath(), expected_in_order_tree_after_7_delete)
        self.assertRaises(Exception, tr.delete_data, 6)


        expected_in_order = \
                [1, 3, 4, 5, 9, 23, 36, 52]
        tr.delete_data(2)
        self.assertEquals(tr.getInOrderPath(), expected_in_order)



class TestBinaryTreeWithParent(unittest.TestCase):
    def test_populate_parent(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        tr = BinaryTreeWithPrarent.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        tr.populate_parent()
        self.assertEqual(None, tr.root['parent'])
        self.assertEqual(tr.root['left'], tr.root['left']['right']['parent'])
        self.assertEqual(tr.root['left'], tr.root['left']['left']['parent'])
        self.assertEqual(141, tr.root['right']['right']['left']['parent']['data'])
        self.assertEqual(tr.root['right'], tr.root['right']['left']['parent'])
        self.assertEqual(tr.getInOrderPath(), in_ordr)


if __name__ == '__main__':
    unittest.main()

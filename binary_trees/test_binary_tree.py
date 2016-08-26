#!/usr/bin/env python3

'tests for binary_tree.py'

from binary_tree import BinaryTree, BinarySearchTree,\
        get_toy_binary_tree, get_empty_tree, get_toy_binary_search_tree

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
        tr = BinarySearchTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        print("printing post order -->")
        tr.printPostOrder()
        print("expected order -->")
        print("(" + " ".join(map(str, post_order)) + " )")


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

    def test_minValue(self):
        self.assertRaises(TypeError, self.empty_bst.minValue)
        self.assertEqual(-1, self.single_node_bst.minValue())
        self.assertEqual(-2, self.small_bst.minValue())
        self.assertEqual(-1, self.toy_bst.minValue())


if __name__ == '__main__':
    unittest.main()

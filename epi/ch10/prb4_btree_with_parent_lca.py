'''Given 2 nodes in a binary tree, design an algo that computes least common ancestor.
Assume that each node has a parent pointer
'''

import unittest
from binary_tree import BinaryTreeWithPrarent

def get_depth(n):
    result = 0
    while n['parent'] != None:
        result += 1
        n = n['parent']
    return result

def get_LCA(n1, n2):
    d1 = get_depth(n1)
    d2 = get_depth(n2)
    #d2 is always deeper than d1
    if d1 > d2:
        n1, n2 = n2, n1
        d1, d2 = d2, d1

    while d1 != d2:
        n2 = n2['parent']
        d2 -= 1

    #now n1 and n2 are at same depth
    while n1 != n2:
        n1 = n1['parent']
        n2 = n2['parent']

    return n1

class Test_get_LCA_with_Parent(unittest.TestCase):

    def setUp(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        self.tr = BinaryTreeWithPrarent.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        self.tr.populate_parent()

    def test_get_LCA1(self):
        n1 = self.tr.root['left']['right']['right']['left'] #14
        n2 = self.tr.root['left']['left']

        exp = self.tr.root['left']
        self.assertEqual(exp, get_LCA(n1, n2))

    def test_get_LCA_same_depth(self):
        n1 = self.tr.root['left']['right']['right'] #86
        n2 = self.tr.root['left']['right']['left'] #16

        exp = self.tr.root['left']['right'] #29
        self.assertEqual(exp, get_LCA(n1, n2))
        self.assertEqual(29, get_LCA(n1, n2)['data'])


    def test_get_LCA_root(self):
        n1 = self.tr.root['left']['right']['right']['left'] #14
        n2 = self.tr.root['right']['right']['left'] #63

        exp = self.tr.root #4
        self.assertEqual(exp, get_LCA(n1, n2))
        self.assertEqual(4, get_LCA(n1, n2)['data'])

    def test_get_LCA_root2(self):
        n1 = self.tr.root['right']['right']['left'] #63
        n2 = self.tr.root['left']['right']['right']['left'] #14

        exp = self.tr.root #4
        self.assertEqual(exp, get_LCA(n1, n2))
        #self.assertEqual(4, get_LCA(n1, n2)['data'])

if __name__ == '__main__':
    unittest.main()


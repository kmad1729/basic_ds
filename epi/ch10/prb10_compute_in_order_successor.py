''' Design an algorithm that computes the successor of a node in a binary tree.
Assume that each node stores its parent.

Hint: Study the node's right subtree. What if the node does not have a right subtree?
'''
import unittest
from binary_tree import BinaryTreeWithPrarent

def get_node_successor(n):
    if n['right']:
        n = n['right']
        while n['left']:
            n = n['left']
    else:
        while n['parent'] and n != n['parent']['left']:
            n = n['parent']
        n = n['parent']
    return n


class Test_node_successor(unittest.TestCase):
    def test_basic_functionality(self):
        in_order = [16, 6, 108, -1, -3, 42, 3, 4, -6, 12, 36, 8]
        pre_order = [3, 6, 16, -3, -1, 108, 42, 12, 4, -6, 8, 36]
        tr = BinaryTreeWithPrarent.from_in_and_pre_order_traversal(in_order, pre_order)
        tr.populate_parent()

        self.assertEquals(get_node_successor(tr.root['left'])['data'], 108)
        self.assertEquals(get_node_successor(tr.root['left']['left'])['data'], 6)
        self.assertEquals(get_node_successor(tr.root['right']['left'])['data'], -6)
        self.assertEquals(get_node_successor(tr.root['right']['right']), None)
        self.assertEquals(get_node_successor(tr.root['right']['right']['left'])['data'], 8)
        self.assertEquals(get_node_successor(tr.root['left']['right']['left'])['data'], -3)
        self.assertEquals(get_node_successor(tr.root['left']['right']['right'])['data'], 3)




if __name__ == '__main__':
    unittest.main()


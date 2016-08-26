'''print level order traversal of a binary tree using dfs
   http://articles.leetcode.com/binary-tree-level-order-traversal-using_17
'''

from binary_tree import BinaryTree
import unittest

def print_level(n, level):
    if n == None:
        return
    if level == 1:
        print(n['data'], end = " ")
        return
    print_level(n['left'], level - 1)
    print_level(n['right'], level - 1)

def print_level_order_using_dfs(tr):
    tr_ht = tr.maxDepth()
    for ht in range(tr_ht):
        print_level(tr.root, ht + 1)
        print()

class Test_print_lvl_order_using_dfs(unittest.TestCase):

    def test_print_lvl_order(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        expected_out = '''
        4
        3 69
        1 29 18 141
        16 86 63
        14
        '''

        print_level_order_using_dfs(tr)
        print("expected out -->")
        print(expected_out)


if __name__ == '__main__':
    unittest.main()




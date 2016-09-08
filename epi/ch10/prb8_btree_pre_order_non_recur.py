'write a program to print pre-order binary tree traversal non-recursively'

from binary_tree import BinaryTree, get_toy_binary_tree2
import unittest


def pre_order_non_recur(n):
    if n == None:
        return []
    result = []
    util_stack = [n]
    while len(util_stack) != 0:
        top = util_stack.pop()
        result.append(top['data'])
        if top['right']:
            util_stack.append(top['right'])
        if top['left']:
            util_stack.append(top['left'])

    return result

class Test_pre_order_non_recur(unittest.TestCase):
    def test_basic_functionality(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        post_order = [1, 16, 14, 86, 29, 3, 18, 63, 141, 69, 4]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        curr_pre_order = pre_order_non_recur(tr.root)
        self.assertEqual(curr_pre_order, pre_ordr)

    def test_basic_functionality1(self):
        tr = get_toy_binary_tree2()
        expecte_pre_order = [5, 3, 9, 6, 8, 8, 42, 7, 98, 23, 28, 0, 86]
        self.assertEqual(expecte_pre_order, pre_order_non_recur(tr.root))


if __name__ == '__main__':

    unittest.main()

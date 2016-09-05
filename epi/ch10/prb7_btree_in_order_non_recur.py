'write a program to print in-order binary tree traversal non-recursively'

from binary_tree import BinaryTree, get_toy_binary_tree2
import unittest

def print_in_order_non_recur(n):
    util_stack = []
    result = []
    if n == None: return result

    util_stack.append((n, False))

    while len(util_stack) != 0:
        top_node, status = util_stack.pop()
        if status:
            result.append(top_node['data'])
        else:
            if top_node['right'] != None:
                util_stack.append((top_node['right'], False))
            util_stack.append((top_node, True))
            if top_node['left'] != None:
                util_stack.append((top_node['left'], False))
    return result

def print_in_order_non_recur_book_sol(n):
    util_stack = []
    result = []
    while len(util_stack) != 0 or n != None:
        if n != None:
            util_stack.append(n)
            n = n['left']
        else:
            c_n = util_stack.pop()
            result.append(c_n['data'])
            n = c_n['right']
    return result

class Test_in_order_non_recur(unittest.TestCase):
    def test_basic_functionality(self):
        in_ordr = [1, 3, 16, 29, 14, 86, 4, 18, 69, 63, 141]
        pre_ordr = [4, 3, 1, 29, 16, 86, 14, 69, 18, 141, 63]
        post_order = [1, 16, 14, 86, 29, 3, 18, 63, 141, 69, 4]
        tr = BinaryTree.from_in_and_pre_order_traversal(in_ordr, pre_ordr)
        curr_in_order = print_in_order_non_recur(tr.root)
        self.assertEqual(curr_in_order, in_ordr)
        self.assertEqual(print_in_order_non_recur_book_sol(
            tr.root), in_ordr)

    def test_basic_functionality1(self):
        tr = get_toy_binary_tree2()
        expected_in_order = [9, 3, 8, 6, 5, 98, 7, 23, 42, 8, 0, 28, 86]
        self.assertEqual(expected_in_order, print_in_order_non_recur(tr.root))


if __name__ == '__main__':
    unittest.main()

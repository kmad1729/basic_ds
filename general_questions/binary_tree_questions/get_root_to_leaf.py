''' For a given binary tree get all the root -> leaf path
'''

import unittest
from binary_tree import get_toy_binary_tree2, get_toy_binary_search_tree

def _utils_get_root_to_leaf_path(n, curr_path, all_paths):
    if n == None:
        return

    curr_path.append(n['data'])
    if n['left'] == None and n['right'] == None:
        all_paths.append(curr_path[:])
        curr_path.pop()
        return

    if n['left'] != None:
        _utils_get_root_to_leaf_path(n['left'], curr_path, all_paths)

    if n['right'] != None:
        _utils_get_root_to_leaf_path(n['right'], curr_path, all_paths)

    curr_path.pop()


def get_root_to_leaf_path(n):
    all_paths = []
    curr_path = []
    _utils_get_root_to_leaf_path(n, curr_path, all_paths)
    return all_paths

class Test_root_to_leaf_paths(unittest.TestCase):

    def test_1(self):
        exp_out = [[5,3,9],
                [5, 3, 6, 8],
                [5, 8, 42, 7, 98],
                [5, 8, 42, 7, 23],
                [5, 8, 28, 0],
                [5, 8, 28, 86],]

        self.assertEqual(exp_out, get_root_to_leaf_path(get_toy_binary_tree2().root))

    def test_2(self):
        exp_out = [[43, 21,2,-1],
                [43, 21, 2, 12, 5],
                [43, 21, 38, 43],
                [43, 97, 60, 74],
                [43,97, 102],
                ]

        self.assertEqual(exp_out, get_root_to_leaf_path(get_toy_binary_search_tree().root))

if __name__ == '__main__':
    unittest.main()

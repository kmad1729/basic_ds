'''draw a binary tree rooted at index 6 for following fields 
creating a binary tree tree DS instead. Also subtracting indexes by 1 for 0 based
representation.
'''

TREE_REPR = [
        {'key': 12, 'left':    6, 'right': 2},
        {'key': 15, 'left':    7, 'right': None},
        {'key':  4, 'left':    9, 'right': None},
        {'key': 10, 'left':    4, 'right': 8},
        {'key':  2, 'left': None, 'right': None},
        {'key': 18, 'left':    0, 'right': 3},
        {'key':  7, 'left': None, 'right': None},
        {'key': 14, 'left':    5, 'right': 1},
        {'key': 21, 'left': None, 'right': None},
        {'key':  5, 'left': None, 'right': None},
        ]

class BinaryTree:
    def __init__(self):
        self.root = None


    def build_tree_from_repr(self, tree_repr, root_ind):
        self.root = self._tree_from_repr_util(tree_repr, root_ind)

    def _tree_from_repr_util(self, tree_repr, root_ind):
        if root_ind == None:
            return None
        c_n = tree_repr[root_ind]
        n = {'key': c_n['key']}
        n['left'] = self._tree_from_repr_util(tree_repr, c_n['left'])
        n['right'] = self._tree_from_repr_util(tree_repr, c_n['right'])
        return n

if __name__ == '__main__':
    my_tree = BinaryTree()
    my_tree.build_tree_from_repr(TREE_REPR, 5)

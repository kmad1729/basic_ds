'classes related to binary trees and binary search trees'

class BinaryTree:
    '''Basic Binary Tree using pointer/linked data structure
    Each node represented as a dictionary {'data':'Foo', 'left':None,'right':<Another_node>}
    '''

    def __init__(self):
        self.root = None

    def _util_size(self, n):
        if n != None:
            return 1 + self._util_size(n['left']) + self._util_size(n['right'])
        return 0

    def size(self):
        return self._util_size(self.root)

    def _util_maxDepth(self, n):
        if n != None:
            return 1 + max(self._util_maxDepth(n['left']), 
                self._util_maxDepth(n['right']))
        return 0

    def maxDepth(self):
        return self._util_maxDepth(self.root)

    def _util_printInOrder(self, n):
        if n != None:
            self._util_printInOrder(n['left'])
            print(n['data'], end = " ")
            self._util_printInOrder(n['right'])

    def printInOrder(self):
        print('(', end = "")
        self._util_printInOrder(self.root)
        print(")")

    
    def _utils_get_node_from_traversals(self, in_order_traversal, pre_order_traversal):
        assert len(in_order_traversal) == len(pre_order_traversal), \
            "in_order -> \n({in_order} != \npre_order ->\n({pre_order})".format(
                    in_order = in_order_traversal, pre_order = pre_order_traversal)

        if len(in_order_traversal) == 0:
            return None

        curr_node = {'data' : pre_order_traversal[



    @classmethod
    def from_in_and_pre_order_traversal(cls, in_order_traversal, pre_order_traversal):
        result = 0 #bug if elems has 0 then edge case
        for elem in in_order_traversal:
            result ^= elem
        assert result == 0, "in_order_traversal ({in_order}) has duplicates".format(
                in_order = in_order_traversal)
        
        result_obj = cls()

        result_obj.root = result_obj._utils_get_node_from_traversals(in_order_traversal, 
            pre_order_traversal)

        return result_obj




class BinarySearchTree(BinaryTree):

    def _util_insert(self, data, n):
        if n == None:
            n = {'data':data, 'left':None, 'right':None}
        else:
            if data <= n['data']:
                n['left'] = self._util_insert(data, n['left'])
            else:
                n['right'] = self._util_insert(data, n['right'])

        return n

    def insert(self, data):
        self.root = self._util_insert(data, self.root)

    def minValue(self):
        if self.root == None:
            raise TypeError('minValue for empty bst not defined!')

        n = self.root
        while n['left'] != None:
            n = n['left']
        return n['data']


#### TEST CODE #####

def get_empty_tree():
    return BinaryTree()

def get_toy_binary_search_tree():
    vals = [43, 97, 21, 2, 38, 60, 74, 102, 12, 5, -1, 43]
    new_bst = BinarySearchTree()
    for v in vals:
        new_bst.insert(v)
    return new_bst

def get_toy_binary_tree():
    'Get a toy binary tree (something with data) to work with'
    root = {
        'data':5,
        'left':{
            'data':9,
            'left':{
                'data':8,
                'left':None,
                'right':{
                    'data':3,
                    'left':None,
                    'right':None,
                    }
                },
            'right':{
                'data':24,
                'left':None,
                'right':None
                },
            },
        'right':{
            'data':4,
            'left':{
                'data':12,
                'left':None,
                'right':{
                    'data':-1,
                    'left':None,
                    'right':None
                    }
                },
            'right':{
                'data':6,
                'left':None,
                'right':None
                },
            },
        }
    new_obj = BinaryTree()
    new_obj.root = root
    return new_obj


def get_toy_binary_tree2():
    'Get a toy binary tree (something with data) to work with'
    '''
                    5
             /            \
            3              8
         /      \        /   \
        9        6      42    28
                /      /     /   \
               8      7     0     86
                     / \    
                    98 23


                
    '''
    root = {
        'data':5,
        'left':{
            'data':3,
            'left':{
                'data':9,
                'left':None,
                'right': None,
                },
            'right':{
                'data':6,
                'left': {
                    'data': 8,
                    'left': None,
                    'right': None,
                },
                'right':None
                },
            },
        'right':{
            'data':8,
            'left':{
                'data':42,
                'left': {
                    'data': 7,
                    'left': {
                        'data': 96,
                        'left': None,
                        'right': None,
                    },
                    'right' : {
                        'data': 23,
                        'left':None,
                        'right':None,
                    },
                },
                'right': None,
            },
            'right':{
                'data':28,
                'left': {
                    'data': 0,
                    'left': None,
                    'right': None,
                },
                'right': {
                    'data': 86,
                    'left':None,
                    'right': None,
                },
            },
        },
        }
    new_obj = BinaryTree()
    new_obj.root = root
    return new_obj


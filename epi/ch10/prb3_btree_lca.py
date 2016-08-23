'get the least common ancestor of two nodes in a generic binary tree'

from binary_tree import BinaryTree

'''Binary tree represented as
{'data': 1, 'left': {'data':-1, 'left': None, 'right': None}, 'right':None}
'''

def _util_lca(subtree_root, n0, n1):
    '''utility function to recursively get the least commont ancestor.
    Returns dictionary {"LCA_node":..., "num_targets":...}
    At each node in the Binary Tree, the node will have n0, n1 or both in its family.
    num_targets keeps track if both nodes are in the family or now.
    LCA_node: Returns the lowest level which has both nodes i.e. the solution
    '''

    if subtree_root == None:
        return {'LCA_node':None, 'num_targets':0}

    left_status = _util_lca(subtree_root['left'], n0, n1)
    if left_status['num_targets'] == 2:
        return left_status

    right_status = _util_lca(subtree_root['right'], n0, n1)
    if right_status['num_targets'] == 2:
        return right_status

    curr_node_targets = left_status['num_targets'] + right_status['num_targets']

    if subtree_root == n0:
        curr_node_targets += 1

    if subtree_root == n1:
        curr_node_targets += 1

    if curr_node_targets == 2:
        return {'LCA_node' : subtree_root, 'num_targets' : 2}
    else:
        return {'LCA_node' : None, 'num_targets' : curr_node_targets}



def get_LCA(tr, n0, n1):
    return _util_lca(tr.root, n0, n1)['LCA_node']

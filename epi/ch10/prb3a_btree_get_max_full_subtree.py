'''return the size of the largest subtree that is complete.
Complete binary tree is a tree where all leaves are at the same level and 
all internal nodes have degree 2.
'''

from binary_tree import BinaryTree


def _util_get_lc_subtree(n):
    '''Recursive function to get the largest subtree rooted at or under n
    that is complete.
    Returns a dictionary {'complete':..., 'size':...}
    'complete' says whether n is complete tree
    'size' returns maximum size of complete subtree at or under n
    '''

    if n == None:
        return {'complete': True, 'size': 0}

    left_status = _util_get_lc_subtree(n['left'])
    right_status = _util_get_lc_subtree(n['right'])

    if left_status['complete'] and right_status['complete']:
        if left_status['size'] == right_status['size']:
            #current tree is complete as both left and right a complete and
            #both of them have equal sizes
            return {'complete': True, 'size':
                    left_status['size'] + right_status['size'] + 1}

    result_status = {'complete': False,
            'size': max(left_status['size'], right_status['size']),
            }

    return result_status

def get_largest_complete_subtree_size(tr):
    return _util_get_lc_subtree(tr.root)['size']

'''given a weighted-graph G and source node s, compute shortest path
distances to all the nodes in the graph. Assume weights to be non-negative
'''

from __future__ import print_function

## HELPER FUNCTIONS ## HEAP IMPLEMENTATION ##
# maintain a map of a node and its position in the heap in variable node_heap_position_map

INF=1e6

def dijkstra_heap_insert(h, node_data, node_heap_position_map):
    '''insert node with node_data in h

    node_data: dict {'node': <NODE>, 'dist', <distance computed till now>} into h 
    h: list of dicts maintaining the min heap property on the basis of 'dist'
    node_heap_position_map: dict to keep track of node's positio nin the heap
    '''
    h.append( {'dist':INF, 'node':node_data['node']})
    node_heap_position_map[node_data['node']] = len(h) - 1
    dijkstra_heap_decrease_key(h, 
            pos=len(h) - 1,
            new_key=node_data['dist'],
            n_h_p_m=node_heap_position_map)

def dijkstra_heap_decrease_key(h, pos, new_key, n_h_p_m):
    '''decrease the key(dist) of a node in the heap h at position pos
    '''
    if new_key > h[pos]['dist']:
        raise Exception('new_key {n_k} is greater than current dist value {d}!'.format(
            n_k=new_key, d=h[pos]['dist']))
    
    def _get_parent_pos(pos):
        'util to get position of a parent e.g parent of 2,3 -> 0, 1 resp'
        return (pos - 1) // 2

    h[pos]['dist'] = new_key
    while pos > 0 and h[_get_parent_pos(pos)]['dist'] > h[pos]['dist']:
        parent_pos = _get_parent_pos(pos)
        #swap node at pos with node at parent_pos
        print("swapping pos! between {parent_pos} and {pos}".format(parent_pos=parent_pos, pos=pos))
        h[parent_pos], h[pos] = h[pos], h[parent_pos]

        #update the node_heap_position_map
        n_h_p_m[h[parent_pos]['node']] = pos
        n_h_p_m[h[pos]['node']] = parent_pos
        
        pos = parent_pos





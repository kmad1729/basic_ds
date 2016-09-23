'''given a weighted-graph G and source node s, compute shortest path
distances to all the nodes in the graph. Assume weights to be non-negative
'''

from __future__ import print_function
import argparse

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
        h[parent_pos], h[pos] = h[pos], h[parent_pos]

        #update the node_heap_position_map
        n_h_p_m[h[pos]['node']] = pos
        n_h_p_m[h[parent_pos]['node']] = parent_pos
        
        pos = parent_pos


def dijkstra_heap_min_heapify(h, pos, n_h_p_m):
    '''maintain the min heap property at pos. Child subtrees of pos are 
    assumed to be min heaps
    '''
    heap_size = len(h)
    left_child = 2 * pos + 1
    right_child = 2 * pos + 2
    min_idx = pos
    if left_child < heap_size and h[min_idx]['dist'] > h[left_child]['dist']:
        min_idx = left_child

    if right_child < heap_size and h[min_idx]['dist'] > h[right_child]['dist']:
        min_idx = right_child

    if min_idx != pos:
        h[min_idx], h[pos] = h[pos], h[min_idx]
        n_h_p_m[h[min_idx]['node']] = min_idx
        n_h_p_m[h[pos]['node']] = pos
        dijkstra_heap_min_heapify(h, min_idx, n_h_p_m)

def dijkstra_heap_extract_min(h, n_h_p_m):
    if len(h) <= 0:
        raise Exception('heap size <= 0. no min!')
    result = h[0]
    last_elem = h.pop()
    if len(h) != 0:
        h[0] = last_elem
        n_h_p_m[h[0]['node']] = 0
        dijkstra_heap_min_heapify(h, 0, n_h_p_m)

    return result['dist'], result['node']


def dijkstra_get_shortest_paths_from_single_node(G, source_node):
    'Calculate the shortest path to different nodes from source_node in graph G'
    dists = dict((k, INF) for k in G)
    edge_pq = []
    node_heap_position_map = {}
    dijkstra_heap_insert(edge_pq, {'dist': 0, 'node': source_node}, node_heap_position_map)
    while len(edge_pq):
        min_dist, min_node = dijkstra_heap_extract_min(edge_pq, node_heap_position_map)
        dists[min_node] = min_dist
        for n, d in G[min_node]:
            if dists[n] > d + dists[min_node]:
                new_dist = d + dists[min_node]
                dists[n] = new_dist
                n_heap_pos = node_heap_position_map.get(n, None)
                if n_heap_pos != None:
                    dijkstra_heap_decrease_key(edge_pq, n_heap_pos, new_dist,
                            node_heap_position_map)
                else:
                    dijkstra_heap_insert(edge_pq, {'dist': new_dist, 'node': n}, 
                            node_heap_position_map)

    return dists

def read_file_get_graph(fname):
    result = {}
    with open(fname, 'r') as f:
        for l in f:
            if l.startswith('#'): continue
            obs = l.split()
            src, dests = obs[0], obs[1:]
            result[src] = []
            for d in dests:
                n, w = d.split(',')
                result[src].append((n, int(w)))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='calculate the shortest path distance from'
            ' source s to a given list of nodes')
    parser.add_argument('f', help='input filename representing the graph')
    parser.add_argument('s', help='source node id')
    parser.add_argument('-d', '--dest_nodes',
            type=lambda s: [(item) for item in s.split(',')],
            help='get distances to the comma-separated nodes specified. All distances if not specified')

    args = parser.parse_args()
    print('args.dest_nodes = {d}'.format(d=args.dest_nodes))
    G = read_file_get_graph(args.f)
    result = []
    dists = dijkstra_get_shortest_paths_from_single_node(G, args.s)
    if args.dest_nodes:
        for dest in args.dest_nodes:
            print('shortest distance from {s}->{d} = {distance}'.format(s=args.s, d=dest,
                distance=dists[dest]))
            result.append(dists[dest])
    else:
        for n in G:
            print('shortest distance from {s}->{d} = {distance}'.format(s=args.s, d=n,
                distance=dists[n]))
            result.append(dists[dest])
    print(result)


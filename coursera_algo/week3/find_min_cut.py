'''given an undirected graph, find the minimum cut using random contraction algorithm
'''

from random import seed, choice

def get_random_edge(G):
    'get a random edge in graph G'
    src_node = choice(G.keys())
    dest_node = choice(G[src_node])
    return (src_node, dest_node)

def reduce_graph(G, new_node_id):
    '''Reduce the graph by a random edge.
    Combine the nodes in the random edge by new_node_id
    Reassign edges and compute the new edges after reduction
    '''

    rand_edge = get_random_edge(G)


    print rand_edge


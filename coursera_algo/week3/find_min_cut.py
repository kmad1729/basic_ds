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

    rand_src, rand_dest = get_random_edge(G)
    print (rand_src, rand_dest)

    src_adjacent_nodes = G[rand_src]
    dest_adjacent_nodes = G[rand_dest]

    del G[rand_src]
    del G[rand_dest]

    #reduction step
    G[new_node_id] = []
    for n in src_adjacent_nodes:
        if n not in [rand_src, rand_dest]:
            G[new_node_id].append(n)

    for n in dest_adjacent_nodes:
        if n not in [rand_src, rand_dest] and n not in G[new_node_id]:
            G[new_node_id].append(n)


    print(G)


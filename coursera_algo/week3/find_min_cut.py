'''given an undirected graph, find the minimum cut using random contraction algorithm
'''

from random import seed, choice

def get_random_edge(G):
    'get a random edge in graph G'
    src_node = choice(G.keys())
    dest_node = choice(G[src_node])
    return (src_node, dest_node)

def contract_graph(G, rand_edge):
    '''Contract the graph by a random edge.
    Combine the nodes in the random edge by new_node_id
    Reassign edges and compute the new edges after reduction
    '''

    #Getting random edge
    rand_src, rand_dest = rand_edge

    
    #Delete that edge
    G[rand_src].remove(rand_dest)
    G[rand_dest].remove(rand_src)


    lower_id, higher_id = sorted([rand_src, rand_dest])
    #now higher_id represents both the nodes in the graph
    #extract lower id's adjacent nodes
    l_adjacent_nodes = G[lower_id]

    #delete lower id
    del G[lower_id]

    #add all extracted lower id's adjacent nodes to higher_id
    G[higher_id].extend(l_adjacent_nodes)

    #Rename all lower_id in the graph to higher_id
    #THIS CAN BE DONE BETTER -->
    for n in G:
        if lower_id in G[n]:
            G[n].remove(lower_id)
            G[n].append(higher_id)

    #Remove all self loops
    #AGAIN THIS CAN BE DONE BETTER -->
    while higher_id in G[higher_id]:
        G[higher_id].remove(higher_id)

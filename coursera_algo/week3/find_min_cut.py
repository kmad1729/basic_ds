'''given an undirected graph, find the minimum cut using random contraction algorithm
'''

import argparse
from random import seed, choice
from copy import deepcopy

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
        while lower_id in G[n]:
            G[n].remove(lower_id)
            G[n].append(higher_id)

    #Remove all self loops
    #AGAIN THIS CAN BE DONE BETTER -->
    while higher_id in G[higher_id]:
        G[higher_id].remove(higher_id)

def get_graph_from_input_file(f_name):
    result = {}
    with open(f_name, 'r') as f:
        for l in f:
            if l.startswith('#'): continue
            if not l.strip(): continue
            objs = map(int, l.split())
            result[objs[0]] = objs[1:]

    return result

def kargers_algo(G):
    while len(G) > 2:
        rand_edge = get_random_edge(G)
        #print('contracting the graph on edge {ed}'.format(ed=rand_edge))
        contract_graph(G, rand_edge)
        #print('G --> {G}'.format(G=G))

    return len(G.values()[0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="for a given graph G compute and trial count N "
            "run karger's algorithm for N times and get the minimum cut")

    parser.add_argument('f', help='input file name')
    parser.add_argument('N', help='number of trials', type=int)
    args = parser.parse_args()

    G = get_graph_from_input_file(args.f)
    min_till_now = 1e9
    for i in range(args.N):
        seed(i)
        min_till_now = min(min_till_now, kargers_algo(deepcopy(G)))

    print("minimum cut after {N} trials = {m}".format(N=args.N, m=min_till_now))



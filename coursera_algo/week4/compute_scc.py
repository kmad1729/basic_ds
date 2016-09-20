'compute the strongly connected components of a directed graph.'

from __future__ import print_function
import argparse
from collections import defaultdict, Counter


def DFS(G, start_node, source_node, start_time, finish_times,
        explored_nodes, leader_nodes):

    explored_nodes[start_node] = True
    leader_nodes[start_node] = source_node

    for node in G[start_node]:
        if not explored_nodes[node]:
            DFS(G,
                    start_node=node,
                    source_node=source_node,
                    start_time=start_time,
                    finish_times=finish_times,
                    explored_nodes=explored_nodes,
                    leader_nodes=leader_nodes)
    start_time[0] += 1
    finish_times[start_node] = start_time[0]



def DFS_loop(G, finish_times):
    t = [0]
    s = None
    num_nodes = len(G)
    explored_nodes = [False] * (num_nodes + 1)
    leader_nodes = [0] * (num_nodes + 1)

    for i in range(num_nodes, 0, -1):
        if not explored_nodes[i]:
            s = i
            DFS(G,
                    start_node=s,
                    source_node=s,
                    start_time=t,
                    finish_times=finish_times,
                    explored_nodes=explored_nodes,
                    leader_nodes=leader_nodes)
    return leader_nodes

def get_G_rev(G):
    num_nodes = len(G)
    result = dict((i, []) for i in range(1,num_nodes+1))

    for src_node in G:
        for dst_node in G[src_node]:
            result[dst_node].append(src_node)
    return result

def get_relabled_graph(G, finish_times):
    num_nodes = len(G)
    result = dict((i, []) for i in range(1,num_nodes+1))
    for src_node in G:
        for dst_node in G[src_node]:
            result[finish_times[src_node]].append(finish_times[dst_node])
    return result

def compute_SCC(G):
    G_Rev = get_G_rev(G)
    num_nodes = len(G)
    finish_times = [1e9] * (num_nodes + 1)
    DFS_loop(G_Rev, finish_times)
    G = get_relabled_graph(G, finish_times)
    leader_nodes = DFS_loop(G, finish_times)
    return leader_nodes[1:]

def graph_data_from_file(fname):
    data = defaultdict(list)
    with open(fname, 'r') as f:
        for l in f:
            if not l.startswith('#'):
                src, dst = map(int, l.split())
                data[src].append(dst)

    return dict(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="compute strongly connected components"
            " in a graph")
    parser.add_argument('f', help='input file name/path')
    args = parser.parse_args()
    fname = args.f
    G = graph_data_from_file(fname)
    leader_nodes = compute_SCC(G)
    num_most_common = 5
    print("here are the largest {i} components".format(i=num_most_common))
    for leader, num_components in Counter(leader_nodes).most_common(num_most_common):
        print("there are {n_c} components with leader {c}".format(n_c=num_components,
            c=leader))





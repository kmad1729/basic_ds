


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




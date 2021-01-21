from typing import Hashable, Mapping, Union
import networkx as nx
import queue
from math import inf


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    prev = {}
    result = {v: inf for v in list(nx.nodes(g))}
    v_nodes = []
    v_queue = queue.Queue()

    result[starting_node] = 0
    v_queue.put((result[starting_node], starting_node))

    while v_queue.queue:
        curr_cost, curr = v_queue.get()
        v_nodes.append(curr)
        for relation_ in dict(g.adj).get(curr):
            path = result[curr] + g.get_edge_data(curr, relation_).get('weight')
            if path < result[relation_]:
                result[relation_] = path
                prev[relation_] = curr
                if relation_ not in v_nodes:
                    v_nodes.append(relation_)
                    v_queue.put((result[relation_], relation_))
                else:
                    v_queue.put((result[relation_], relation_))
    return result


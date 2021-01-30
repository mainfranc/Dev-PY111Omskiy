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
    result = {v: inf for v in list(nx.nodes(g))}
    v_nodes = []
    v_queue = queue.Queue()

    result[starting_node] = 0
    v_queue.put(starting_node)

    while v_queue.queue:
        curr = v_queue.get()
        v_nodes.append(curr)
        for relation_ in dict(g.adj).get(curr):
            path = result[curr] + g.get_edge_data(curr, relation_).get('weight')
            if path < result[relation_]:
                result[relation_] = path
                v_queue.put(relation_)
    return result


def dijkstra_algo2(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    prev = {}
    result = {v: inf for v in list(nx.nodes(g))}
    v_nodes = []

    result[starting_node] = 0
    next_one = starting_node
    v_nodes.append(starting_node)

    while next_one:
        visit_from = v_nodes[-1]
        next_one = ''
        for relation_ in dict(g.adj).get(visit_from):
            path = result[visit_from] + g.get_edge_data(visit_from, relation_).get('weight')
            if path < result[relation_]:
                v_nodes.append(relation_)
                result[relation_] = path
                prev[relation_] = visit_from
                next_one = relation_
    return result

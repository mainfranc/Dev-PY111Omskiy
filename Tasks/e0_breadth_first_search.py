from typing import Hashable, List
import networkx as nx
import queue


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    v_queue = queue.Queue()
    v_queue.put(start_node)
    v_nodes = [start_node]

    while True:
        legacies = v_queue.get()

        for node in g[legacies]:
            if not (node in v_nodes):
                v_nodes.append(node)
                v_queue.put(node)
        if not v_queue.queue: return v_nodes


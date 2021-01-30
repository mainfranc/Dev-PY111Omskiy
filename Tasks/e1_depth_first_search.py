from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    v_stack = [start_node]
    total_result = []
    v_nodes = []

    while True:
        legacies = v_stack[-1]
        v_stack.pop(-1)
        v_nodes.append(legacies)

        for node in g[legacies]:
            if  node not in v_nodes:
                v_stack.append(node)
        if not v_stack:
            return v_nodes

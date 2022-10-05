from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """

    queue = []
    queue.append(start_node)
    for node in queue:
        for nebr in g.neighbors(node):
            if nebr not in queue:
                queue.append(nebr)

    print(g, start_node)
    return queue

from typing import Hashable, List
import networkx as nx

from Tasks.a0_my_stack import Stack

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    stack = Stack()
    stack.push(start_node)
    for node in stack:
        print(node)
        for nbr in g.neighbors(node):
            print(nbr)
            stack.push(nbr)
    print(g, start_node)
    print(stack)
    return [i for i in stack]

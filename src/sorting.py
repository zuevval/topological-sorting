from src import Graph
import numpy as np  # type:ignore


def sorting(graph: Graph) -> set:
    """
    Topological sorting using Depth First Search
    :param graph: vertices and edges of the graph to be traversed
    :return: sorted vertices
    """
    return set(range(graph.n_vertices))  # TODO implement algorithm

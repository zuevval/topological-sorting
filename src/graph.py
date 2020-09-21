from dataclasses import dataclass
import logging

import numpy as np  # type:ignore


@dataclass
class Graph:
    """
    This structure may represent any non-directed, non-weighted graph or multigraph.
    `edges` - array of pairs of vertices n*2, where `n` is a total number of edges
    `vertices` - set of all vertices (those which form edges and others)
    """
    edges: np.ndarray
    vertices: set

    def __init__(self, edges: np.ndarray, vertices: set):
        for edge in edges:
            assert len(edge) == 2, "each edge must connect two vertices"
            assert edge[0] in vertices and edge[1] in vertices, "vertices in the edge must exist in the vertices set"
        self.edges, self.vertices = edges, vertices

    @staticmethod
    def loadtxt(filename: str):
        try:
            # read first line into `vertices`
            vertices = set(np.loadtxt(filename, max_rows=1, ndmin=1).astype(int))
            # read second and subsequent lines into `edges`
            edges = np.loadtxt(filename, skiprows=1).astype(int)
            return Graph(edges, vertices)
        except FileNotFoundError:
            logging.error("Could not read graph from file: file does not exist")
        except Exception as e:
            logging.error("Could not read graph from file: an unexpected error occurred: " + str(e))

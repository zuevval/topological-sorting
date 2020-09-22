from dataclasses import dataclass
import logging

import numpy as np  # type:ignore


@dataclass
class Graph:
    """
    This structure may represent any non-directed, non-weighted graph or multigraph.
    `n_vertices` - number of vertices in graph. Each vertex is an integer in range {0;n-1}
    `edges` - array of pairs of vertices m*2, where `m` is a total number of edges
    """
    edges: np.ndarray
    n_vertices: int

    def __init__(self, edges: np.ndarray, n_vertices: int):
        assert edges.dtype == int, "each vertex must be a non-negative integer"
        for edge in edges:
            assert len(edge) == 2, "each edge must connect two vertices, no more and no less"
            assert min((0 < v < n_vertices for v in edge)), "each vertex must be within the range {1;n-1}"
        self.edges, self.n_vertices = edges, n_vertices

    @staticmethod
    def loadtxt(filename: str):
        try:
            # read number of vertices from the first line
            with open(filename) as fin:
                n_vertices = int(fin.readline().strip())
            # read second and subsequent lines into `edges`
            edges = np.loadtxt(filename, skiprows=1).astype(int)
            return Graph(edges, n_vertices)
        except FileNotFoundError:
            logging.error("Could not read graph from file: file does not exist")
        except Exception as e:
            logging.error("Could not read graph from file: an unexpected error occurred: " + str(e))

from collections import defaultdict
from typing import DefaultDict, List, Union

from .sorting import Vertex, toposort


class DependencyGraph:
    def __init__(self):
        self.graph: DefaultDict[Vertex, List[Vertex]] = defaultdict(list)

    def __repr__(self):
        return "DependencyGraph({})".format(", ".join("{} : {}".format(v, li) for v, li in self.graph.items()))

    def add(self, v: Vertex, dependencies: Union[List[Vertex], None] = None):
        assert v not in self.graph, "could not add vertex: already in the graph"
        if dependencies is None:
            dependencies = []
        self.graph[v] = dependencies

    def get_dependencies(self, v: Vertex) -> List[Vertex]:
        assert v in self.graph, "graph does not contain this vertex"
        result = list(reversed(toposort(v, self.graph)))
        result.remove(v)
        return result

import os
from collections import defaultdict
from pathlib import Path
from typing import List, Dict
from graphviz import Digraph

from pipeline_manager import Vertex, toposort


def run_toposort_test(
    v: Vertex, graph: Dict[Vertex, List[Vertex]], expected_dependencies: List[Vertex]
):
    ans = toposort(v, defaultdict(list, graph))
    assert ans == expected_dependencies, (
        "\n expected: " + str(expected_dependencies) + "\n got: " + str(ans)
    )


def run_toposort_multisolution_test(
    v: Vertex, graph: Dict[Vertex, List[Vertex]], expected_chains: List[List[Vertex]]
):
    """
    testing a graph with which multiple solutions are possible
    :param expected_chains: each chain is a sequence of vertices which must follow this order in any topological sort
    """
    ans = toposort(v, defaultdict(list, graph))
    ans_indices = {v: v_idx for v, v_idx in zip(ans, range(len(ans)))}
    for chain in expected_chains:
        for u, u_next in zip(chain[:-1], chain[1:]):
            assert (
                ans_indices[u] < ans_indices[u_next]
            ), "one of the chains is ordered differently from the sorting"


def get_out_path() -> Path:
    out_arg = "OUT_PATH"
    out_dir = Path(os.environ[out_arg]) if out_arg in os.environ else Path("./out")
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def visualize(graph: Dict[Vertex, List[Vertex]], name: str):
    graph = defaultdict(list, graph)
    vertices = graph.keys()
    nonzero_degree_vertices = set()
    g = Digraph(comment=name)
    for v in vertices:
        if graph[v]:
            nonzero_degree_vertices.add(v)
        for u in graph[v]:
            nonzero_degree_vertices.add(u)
            g.edge(str(v), str(u))
    for v in vertices:
        if v not in nonzero_degree_vertices:
            g.node(str(v))
    out_dir = get_out_path()
    g.render(out_dir / (name + ".gv"))

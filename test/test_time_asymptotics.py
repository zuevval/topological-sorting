from functools import wraps
from time import time
from typing import List, Tuple

import matplotlib.pyplot as plt

# credit: https://stackoverflow.com/a/15136422
from pipeline_manager import DependencyGraph
from .utils import get_out_path


def timing(f: callable):
    @wraps(f)
    def wrap(*args, **kwargs) -> float:
        """
        measure execution time of wrapped function
        :return: time (seconds)
        """
        start = time()
        f(*args, **kwargs)
        elapsed = time()
        return elapsed - start

    return wrap


@timing
def run_dependency_graph_test(graph_size: int):
    graph = DependencyGraph()
    for v in range(graph_size):
        graph.add(v, list(range(v)))
    assert graph_size > 0, "please provide non-trivial graph"
    graph.get_dependencies(graph_size - 1)


def test_time_complexity():
    graph_sizes = list(range(1, 4001, 500))
    graph_times: List[Tuple[float, float]] = [
        (graph_size, run_dependency_graph_test(graph_size))
        for graph_size in graph_sizes
    ]

    x, y = zip(*graph_times)

    plt.plot(x, y)
    plt.ylabel("time")
    plt.xlabel("number of elements in the graph")
    plt.grid()
    plt.savefig(get_out_path() / "test_time_complexity")

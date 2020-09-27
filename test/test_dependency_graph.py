from pipeline_manager import DependencyGraph
from test.utils import visualize


def test_dependency_graph_numeric():
    graph = DependencyGraph()
    graph.add(1, [2, 3, 4])
    graph.add(2, [3, 4])
    graph.add(3, [4])
    graph.add(5)
    assert graph.get_dependencies(1) == [4, 3, 2]
    assert graph.get_dependencies(2) == [4, 3]
    assert graph.get_dependencies(3) == [4]
    assert graph.get_dependencies(4) == []
    assert graph.get_dependencies(5) == []
    visualize(graph.graph, "graph_numeric")


def test_dependency_graph_strings():
    graph = DependencyGraph()
    graph.add("baz", ["bar"])
    graph.add("foo", ["bar", "baz"])
    graph.add("fubar", ["foo", "bar"])
    assert graph.get_dependencies("fubar") == ["bar", "baz", "foo"]
    visualize(graph.graph, "graph_strings")

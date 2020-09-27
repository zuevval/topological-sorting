from .utils import run_toposort_test, visualize, run_toposort_multisolution_test


def test_sorting_one_vertex():
    run_toposort_test(0, {0: []}, [0])


def test_sorting_simple():
    graph = {0: [], 1: [0], 2: [0, 1]}
    run_toposort_test(0, graph, [0])
    run_toposort_test(1, graph, [1, 0])
    run_toposort_test(2, graph, [2, 1, 0])
    visualize(graph, "simple")


def test_sorting_tree():
    """
        6   two backslashes \\ used only to avoid making escape char sequence
       / \
      4   5
     /\\  |\
    0  1  2 3
    """
    graph = {0: [], 1: [], 2: [], 3: [], 4: [0, 1], 5: [2, 3], 6: [4, 5]}
    run_toposort_multisolution_test(6, graph, [[6, 4, 0], [6, 5, 2], [4, 1], [5, 3]])
    run_toposort_test(0, graph, [0])
    visualize(graph, "tree")


def test_sorting_two_symmetric_contours():
    """
            6->5
           /    \
    9->8->7      2->1->0
          \\    /
            4->3
    """
    graph = {
        9: [8],
        8: [7],
        7: [4, 6],
        6: [5],
        5: [2],
        4: [3],
        3: [2],
        2: [1],
        1: [0],
        0: [],
    }
    run_toposort_test(0, graph, [0])
    run_toposort_test(1, graph, [1, 0])
    run_toposort_test(2, graph, [2, 1, 0])
    run_toposort_test(3, graph, [3, 2, 1, 0])
    run_toposort_test(4, graph, [4, 3, 2, 1, 0])
    run_toposort_test(5, graph, [5, 2, 1, 0])
    run_toposort_test(6, graph, [6, 5, 2, 1, 0])
    run_toposort_multisolution_test(
        9, graph, [[9, 8, 7, 6, 5, 2, 1, 0], [9, 8, 7, 4, 3, 2, 1, 0]]
    )
    visualize(graph, "two symmetric contours")


def test_sorting_two_asymmetric_contours():
    """
        4-3-2
       /     \
    7-6       1->0
      \\     /
        --5--
    """
    graph = {7: [6], 6: [4, 5], 5: [1], 4: [3], 3: [2], 2: [1], 1: [0]}
    run_toposort_multisolution_test(7, graph, [[7, 6, 4, 3, 2, 1, 0], [7, 6, 5, 1, 0]])
    visualize(graph, "two asymmetric contours")


def test_sorting_multiple_contours():
    """
          5->4->3    1
         /      \\ /
    11->10->7->6->2
        \\ /    /  \
         9---->8    0

    """
    graph = {
        11: [10],
        10: [5, 7, 9],
        9: [7, 8],
        8: [2],
        7: [6],
        6: [2],
        5: [4],
        4: [3],
        3: [2],
        2: [0, 1],
        1: [],
        0: [],
    }
    run_toposort_multisolution_test(2, graph, [[2, 0], [2, 1]])
    run_toposort_multisolution_test(9, graph, [[9, 7, 6, 2, 1], [9, 8, 2, 0]])
    run_toposort_multisolution_test(
        11,
        graph,
        [[11, 10, 7, 6, 2, 1], [11, 10, 5, 4, 3, 2, 0], [11, 10, 9, 7, 6, 2, 0]],
    )
    visualize(graph, "multiple contours")


def test_sorting_two_components():
    graph = {0: [], 1: [0], 2: [0, 1], 3: [], 4: [], 5: [], 6: [3, 4, 5], 7: [6, 3]}
    run_toposort_test(2, graph, [2, 1, 0])
    run_toposort_multisolution_test(7, graph, [[7, 6, 5], [6, 4], [6, 3]])
    visualize(graph, "two components")


def test_sorting_no_edges():
    graph = {0: [], 1: [], 2: [], 3: [], 4: []}
    for v in graph.keys():
        run_toposort_test(v, graph, [v])
    visualize(graph, "no edges")


def test_sorting_complete_graph():
    graph = {
        0: [],
        1: [0],
        2: [1, 0],
        3: [2, 1, 0],
        4: [3, 2, 1, 0],
        5: [4, 3, 2, 1, 0],
        6: [5, 4, 3, 2, 1, 0],
    }
    run_toposort_test(6, graph, [6, 5, 4, 3, 2, 1, 0])
    visualize(graph, "complete graph")


def test_sorting_stress():
    n_vertices = 5000
    graph = {}
    for v in range(n_vertices - 1):
        graph[v] = [v + 1]
    for v in range(n_vertices - 2):
        graph[v].append(v + 2)
    run_toposort_test(0, graph, list(range(n_vertices)))

    graph_slice = {v: graph[v] for v in graph.keys() if v > 4900}
    visualize(graph_slice, "stress test (part of the graph)")

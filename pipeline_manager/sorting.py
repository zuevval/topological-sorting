from typing import DefaultDict, Union, NewType, List

# mypy bug: https://github.com/python/mypy/issues/4200
Vertex = NewType("Vertex", Union[str, int])  # type: ignore


def toposort(start: Vertex, graph: DefaultDict[Vertex, List[Vertex]]) -> List[Vertex]:
    """
    Topological sorting. Assuming that graph is directed and acyclic (
    otherwise will loop endlessly)
    :param start: vertex to start from
    :param graph: a graph to traverse
    :return: visited vertices in the traverse order
    """
    used = set()
    stack_local: List[Vertex] = []
    result = []
    stack_global = [start]
    while stack_global:
        v = stack_global.pop()
        if v not in used:
            used.add(v)
            stack_global.extend(graph[v])
            while stack_local and v not in graph[stack_local[-1]]:
                result.append(stack_local.pop())
            stack_local.append(v)
    stack_local.extend(list(reversed(result)))
    return stack_local

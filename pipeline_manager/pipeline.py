from typing import Callable, Any

from .dependency_graph import DependencyGraph


def pipeline():
    """
    :return: returns a decorator that allows to add steps to the pipeline
    """
    graph = DependencyGraph()
    name_to_func = {}

    def register_decorator_factory(*args, **kwargs):
        depends_on = []

        def register_decorator(func: Callable[[], Any]):
            nonlocal depends_on
            graph.add(func.__name__, depends_on)

            def wrapper():
                dependencies = graph.get_dependencies(func.__name__)
                for f_name in dependencies:
                    name_to_func[f_name]()
                func()

            name_to_func[func.__name__] = wrapper
            return wrapper

        if len(args) == 1 and callable(args[0]):  # if called without params
            return register_decorator(args[0])
        assert "depends_on" in kwargs, "specify a parameter depends_on"
        depends_on = kwargs["depends_on"]
        return register_decorator

    return register_decorator_factory

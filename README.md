# Topological sorting in pipeline management

[![Actions Status](https://github.com/zuevval/topological-sorting/workflows/Python%20CI/badge.svg?branch=develop)](https://github.com/zuevval/topological-sorting/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code Coverage](https://codecov.io/gh/zuevval/topological-sorting/branch/develop/graph/badge.svg)](https://codecov.io/gh/zuevval/topological-sorting)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![HitCount](http://hits.dwyl.com/zuevval/topological-sorting.svg)](http://hits.dwyl.com/zuevval/topological-sorting)

This is a Python package which features:
 - Depth First Search implementation of topological sorting for acyclic oriented graphs written in Python 3
 - an application of this sorting - managing pipelines of your functions with dependencies: each function invokes automatically all its dependencies

## Requirements
- Python 3.8.x: [get at python.org](https://www.python.org/downloads/)

## Installation
- Download these files from GitHub or clone this repository via https:
```shell script
git clone https://github.com/zuevval/topological-sorting.git
cd topological-sorting
```
- Install dependencies for command line application:
 ```shell script
 pip install src/requirements.txt
```
If you wish to **run tests and static code checks**, install also dependencies for tests:
```shell script
pip install test/requirements.txt
```
To run tests install also [install GraphViz](https://www.graphviz.org/download/) for test visualization. If you're running Windows, 
make sure to add `<graphviz/installation/path>/bin` to PATH environmental variable.

## Usage
If you invoke Python from the root folder of this repository, a package `pipeline_manager` will be in your Python path.

Otherwise you need to add this folder to PYTHONPATH, e. g. on Linux
```shell script
export PYTHONPATH="${PYTHONPATH}:/path/containing/repository/pipeline-management-zuevval"
```
### Topological sorting
You may sort oriented acyclic graphs with strings or integers as vertices.

At the top of your file add imports:
```python
...
from pipeline_manager import Vertex, toposort
```
where `Vertex` is a shorthand for `Union[str, int]`

Each graph must be of type `DefaultDict[Vertex, List[Vertex]]`.

Then call `toposort`, passing a graph and a starting vertex to it:
```python
...
sorted = toposort(v, my_graph)
```

Example:
```python
from collections import defaultdict

from pipeline_manager import toposort


def main():
    graph = defaultdict(list, {0:[], 1:[0], 2:[0, 1]})
    print(toposort(2, graph))

if __name__ == '__main__':
    main()

```

### Building pipeline of functions

Consider a *pipeine* - a set of steps, each steps is a function invocation. Steps may depend from other steps. You may build a pipeline using
a decorator which allows passing an optional argument - names of methods on which this step depends:

```python
from pipeline_manager import pipeline

register = pipeline()

@register
def step1():
    print("Step 1")

@register(depends_on=["step1"])
def step2():
    print("Step 2")

step1()
"Step 1"
```

When a method decorated with `@register` (or another name that you give to a result of the `pipeline()`) is called, all 
its dependencies are called, too. The order of invocation follows the inverse topological sort of the graph where
each vertex is a step and each edge is a dependency, so that none of the steps are executed before their dependencies and
all dependencies for every step are executed.

```python
step2()
"Step 1"
"Step 2"

step1()
"Step 1"
```

### Running test cases
There are some tests under `test` folder. To run them:
 - install test dependencies (see "Installation")
 - \[optionally\] set up the environmental variable `OUT_PATH` - the output path for tests artifacts, e. g. on Linux
     ```shell script
    export OUT_PATH=test/out
    ```
 - run `pytest` from the root directory of the repository:
    ```shell script
    python -m pytest
    ```

### Obtaining test artifacts from GitHub Actions
Some tests produce files that are not stored in the repository but are auto-generated and uploaded to artifacts when a
CI workflow is triggered (e. g. on pull request to `develop` or `master`). This includes PDF illustration to graphs and 
code coverage reports. You may download these files:
1. Go to the [workflow webpadge](https://github.com/zuevval/topological-sorting/actions)
1. Navigate to the latest successfull run
1. Download the archive "test output" and unpack it
![image](https://user-images.githubusercontent.com/23435506/94366555-c94f6f80-00e1-11eb-86d4-07f610f7bff0.png)


## Uninstalling

simply remove the root folder of the repository from your filesystem

## Contact & support
To report proboems (or for any questions whatsoever) create an [issue on GitHub](https://github.com/zuevval/topological-sorting/issues/new).

Alternatively, you may e-mail me at [valera.zuev.zva@gmail.com](mailto:valera.zuev.zva@gmail.com)

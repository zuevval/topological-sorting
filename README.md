# Topological Sorting

[![Actions Status](https://github.com/zuevval/topological-sorting/workflows/Python%20CI/badge.svg?branch=develop)](https://github.com/zuevval/topological-sorting/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/zuevval/topological-sorting)](https://codecov.io/gh/zuevval/topological-sorting)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![HitCount](http://hits.dwyl.com/zuevval/topological-sorting.svg)](http://hits.dwyl.com/zuevval/topological-sorting)

Depth First Search implementation of topological sorting written in Python 3

## Requirements
- Python 3.8.x: [get at python.org](https://www.python.org/downloads/)

## Installation
- Download these files from GitHub or clone this repository via https:
```
git clone https://github.com/zuevval/topological-sorting.git
cd topological-sorting
```
- Install dependencies for command line application:
 ```
 pip install src/requirements.txt
```
If you wish to run tests and static code checks, install also dependencies for tests:
```
pip install test/requirements.txt
```

## Usage
### Application
`TODO write usage`

### Running tests
- set up environmental variable `OUT_PATH` for output files, e. g.
```
export OUT_PATH=test/data/out
```
- run all tests with `unittest.discover`:
```
python -m unittest discover
```

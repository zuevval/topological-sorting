import argparse
from src import sorting, Graph
import numpy as np  # type:ignore


def main():
    input_argname, output_argname = "input", "output"
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--" + input_argname, required=True,
                    help="input filename: graph (line 1 - int `n`, next lines - edges (pairs of int in {1;n-1})")
    ap.add_argument("-o", "--" + output_argname, required=False, help="output filename")
    args = vars(ap.parse_args())
    input_filename = args[input_argname]
    output_filename = args[output_argname] if output_argname in args else "./output.txt"

    result = sorting(Graph.loadtxt(input_filename))
    np.savetxt(output_filename, np.array(list(result)), fmt="%d")


if __name__ == "__main__":
    main()

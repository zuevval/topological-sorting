import argparse
from src import sorting, Graph
import numpy as np  # type:ignore


def main():
    input_argname, output_argname = "input", "output"
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--" + input_argname, required=True,
                    help="input filename: graph (line 1 - list of vertices (integers), next lines - edges (int pairs)")
    ap.add_argument("-o", "--" + output_argname, required=False, help="output filename")
    args = vars(ap.parse_args())
    input_filename = args[input_argname]
    output_filename = args[output_argname] if output_argname in args else "./output.txt"

    result = sorting(Graph.loadtxt(input_filename))
    print("-----")
    print(np.array(list(result)))
    np.savetxt(output_filename, np.array(list(result)), fmt="%d")


if __name__ == "__main__":
    main()

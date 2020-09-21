import os
from test.integration import TestCaseWrapper
import numpy as np


class TestFromFile(TestCaseWrapper):
    def test_trivial(self):
        out_filename = str(self.OutDir) + "/" + self.id() + ".txt"
        os.system("python3 -m src -i ./test/data/test_cases/trivial/graph.txt -o " + out_filename)
        answer = np.loadtxt(out_filename)
        expected_answer = np.loadtxt("test/data/test_cases/trivial/answer.txt")
        assert (answer == expected_answer).all

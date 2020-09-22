import os
from test.integration import TestCaseWrapper
import numpy as np


class TestFromFile(TestCaseWrapper):
    def run_test(self, test_subfolder: str):
        out_filename = str(self.out_dir / (self.id() + ".txt"))
        test_folder = (self.data_dir / "test_cases") / test_subfolder
        input_filename = str(test_folder / "graph.txt")
        expected_ans_filename = str(test_folder / "answer.txt")

        os.system("python3 -m src -i " + input_filename + " -o " + out_filename)
        answer = np.loadtxt(out_filename)
        expected_answer = np.loadtxt(expected_ans_filename)
        assert (answer == expected_answer).all()

    def test_trivial(self):
        self.run_test("trivial")

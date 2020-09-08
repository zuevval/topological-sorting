import unittest
from pathlib import Path


class TestExample(unittest.TestCase):
    def test_example(self):
        assert True
        Path("test/data/out/").mkdir(parents=True, exist_ok=True)
        with open("test/data/out/example.txt", "w") as file_out:
            file_out.writelines("Hello Example Output File")

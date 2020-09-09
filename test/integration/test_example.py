from test.integration import TestCaseWrapper


class TestExample(TestCaseWrapper):
    def test_example(self):
        assert True
        with open(self.OutDir / "example.txt", "w") as file_out:
            file_out.writelines("Hello Example Output File")

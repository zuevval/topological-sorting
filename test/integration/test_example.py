from test.integration import TestCaseWrapper
import logging


class TestExample(TestCaseWrapper):
    def test_example(self):
        assert True
        with open(self.OutDir / "example.txt", "w") as file_out:
            file_out.writelines("Hello Example Output File")
        logging.info("This is an example test: " + TestCaseWrapper.id(self))

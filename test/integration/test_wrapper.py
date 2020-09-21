import os
import datetime
import unittest
import logging
from pathlib import Path


class TestCaseWrapper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert "OUT_PATH" in os.environ, "'OUT_PATH' (output directory) must be among environment variables"
        cls.OutDir = Path(os.environ["OUT_PATH"])
        cls.OutDir.mkdir(parents=True, exist_ok=True)
        log_filename = str(cls.OutDir / (
            "integration_tests_" + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-') + ".log"))
        logging.basicConfig(level=logging.DEBUG, force=True, filename=log_filename)

    def setUp(self):
        logging.info(" starting: " + str(self.id()))

    def tearDown(self):
        logging.info(" success: " + str(self.id()))

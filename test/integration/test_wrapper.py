import os
import unittest
import logging
from pathlib import Path


class TestCaseWrapper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert "OUT_PATH" in os.environ, "'OUT_PATH' (output directory) must be among environment variables"
        cls.OutDir = Path(os.environ["OUT_PATH"])
        cls.OutDir.mkdir(parents=True, exist_ok=True)
        log_dir = cls.OutDir / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_filename = str(log_dir / ("IntegrationTests_" + cls.__name__ + ".log"))
        logging.basicConfig(level=logging.DEBUG, force=True, filename=log_filename)

    def setUp(self):
        logging.info(" starting: " + str(self.id()))

    def tearDown(self):
        logging.info(" success: " + str(self.id()))

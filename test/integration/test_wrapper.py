import os
import unittest
import logging
from pathlib import Path


class TestCaseWrapper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        arg_out, arg_data = "OUT_PATH", "DATA_PATH"
        for arg, desc in {arg_out: "output directory", arg_data: "path to test data"}.items():
            assert arg in os.environ, arg + " (" + desc + ") must be among environmental variables"
        cls.data_dir = Path(os.environ[arg_data])
        cls.out_dir = Path(os.environ[arg_out])
        cls.out_dir.mkdir(parents=True, exist_ok=True)
        log_dir = cls.out_dir / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_filename = str(log_dir / ("IntegrationTests_" + cls.__name__ + ".log"))
        logging.basicConfig(level=logging.DEBUG, force=True, filename=log_filename)

    def setUp(self):
        logging.info(" starting: " + str(self.id()))

    def tearDown(self):
        logging.info(" success: " + str(self.id()))

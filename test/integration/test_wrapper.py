import os
import unittest
from pathlib import Path


class TestCaseWrapper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert "OUT_DIR" in os.environ, "'OUT_DIR' (output directory) must be among environment variables"
        cls.OutDir = Path(os.environ["OUT_DIR"])
        cls.OutDir.mkdir(parents=True, exist_ok=True)

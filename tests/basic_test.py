import io
import os
from unittest import TestCase

from ask_openai import ask

import dotenv

dotenv.load_dotenv()


class TestBasic(TestCase):
    def test_basic(self):
        logger = io.StringIO()

        @ask(api_key=os.environ['MY_OPENAI_API_KEY'], logger=logger.write)
        def foo():
            raise 1 / 0

        with self.assertRaises(ZeroDivisionError):
            foo()

        self.assertIn("divi".lower(), logger.getvalue().lower())
        self.assertIn("zero".lower(), logger.getvalue().lower())

    def test_robustness(self):
        logger = io.StringIO()

        @ask(api_key="sk-", logger=logger.write)
        def foo():
            raise 1 / 0

        with self.assertRaises(ZeroDivisionError):
            foo()

        self.assertIn("Incorrect API key", logger.getvalue())

import os
from unittest import TestCase

from ask_openai import ask

import dotenv

dotenv.load_dotenv()

ask = ask(api_key=os.environ['MY_OPENAI_API_KEY'], logger=print)


@ask
def foo():
    raise 1 / 0


class TestBasic(TestCase):
    def test_basic(self):
        with self.assertRaises(ZeroDivisionError):
            foo()

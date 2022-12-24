import os
from unittest import TestCase
from ask_me import ask

import dotenv

dotenv.load_dotenv()

api_key = os.environ['MY_OPENAI_API_KEY']


@ask(api_key)
def foo():
    raise 1 / 0


class TestBasic(TestCase):
    def test_basic(self):
        foo()

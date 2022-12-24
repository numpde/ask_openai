This package `ask_openai` provides a single minimal implementation
of a function decorator `ask`.

If the decorated function raises an error,
the decorator asks OpenAI / GPT-3 to explain it to you.

Use as follows:

```Python
import os
from ask_openai import ask

ask = ask(api_key=os.environ['OPENAI_API_KEY'], logger=print)


@ask
def f(x):
    return 1 / 0
```

This will print something like:

```commandline
OpenAI explanation: Division by zero is an error because a number cannot be divided by 0.
```

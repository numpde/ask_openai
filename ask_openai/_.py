import openai
import inspect


def ask(api_key, logger=print):
    def _(f):
        def _(*a, **kw):
            code = inspect.getsource(f)
            try:
                f(*a, **kw)
            except Exception as ex:
                prompt = f"CODE:\n\n{code}\n\nERROR:\n\n{ex}\n\nVery concise explanation:\n\n"

                response = openai.Completion.create(
                    model='text-davinci-003',
                    prompt=prompt,
                    api_key=api_key,
                    max_tokens=(len(prompt) + 150),
                )

                explanation = response['choices'][0]['text']
                logger(f"OpenAI explanation: {explanation}")

                raise ex

        return _

    return _

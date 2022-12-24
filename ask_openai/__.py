import openai
import inspect


def ask(api_key, logger=print):
    def _(f):
        def _(*a, **kw):
            code = inspect.getsource(f)
            try:
                f(*a, **kw)
            except Exception as ex:
                try:
                    prompt = f"CODE:\n\n{code}\n\nERROR:\n\n{ex}\n\nVery concise explanation:\n\n"

                    response = openai.Completion.create(
                        model='text-davinci-003',
                        prompt=prompt,
                        api_key=api_key,
                        max_tokens=(len(prompt.split(' ')) + 150),
                    )

                    explanation = response['choices'][0]['text'].strip()
                    logger(f"OpenAI explanation:\n{explanation}")
                except Exception as open_ai_ex:
                    logger(f"Could not fetch explanation from OpenAI due to: {open_ai_ex}")
                finally:
                    raise ex

        return _

    return _

from decouple import config

import openai

openai.api_key = config('OPENAI_API_KEY')


def generate_prompt(text):
    return """Summarize this in three short sentences:
    
    "{}"
    """.format(text)


def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=generate_prompt(text),
        max_tokens=1000,
        temperature=0
    )
    summary = response.choices[0].text
    return summary

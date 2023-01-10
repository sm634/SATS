import os

import openai

openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_prompt(text):
    return """Summarize the text below into one short paragraph:
    
    {}
    """.format(text)


def summarize_text(text):
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=generate_prompt(text),
        max_tokens=1000,
        temperature=0
    )
    summary = response.choices[0].text
    return summary

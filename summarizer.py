import openai

openai.api_key = "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"


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

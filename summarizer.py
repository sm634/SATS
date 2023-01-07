import os

import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"


def summarise_prompt(text):
    return """Summarize the text below into two bullet points:
    
    {}
    """.format(text)


text_sample = """A short treatise on how to acquire power, create a state, and keep it, The Prince represents 
Machiavelli’s effort to provide a guide for political action based on the lessons of history and his own experience 
as a foreign secretary in Florence. His belief that politics has its own rules so shocked his readers that the 
adjectival form of his surname, Machiavellian, came to be used as a synonym for political maneuvers marked by 
cunning, duplicity, or bad faith."""

response = openai.Completion.create(
    engine="text-curie-001",
    prompt=summarise_prompt(text_sample),
    max_tokens=250,
    temperature=0
)

print(response.choices[0].text)

import os

from summarizer import summarize_text
from utils.parser import TextPreprocessor

input_path = 'data/input/'
output_path = 'data/output/'

input_files = os.listdir(input_path)

tp = TextPreprocessor()

for file in input_files:
    with open(input_path + file, 'r', encoding='utf8') as f:
        text = f.read()
        text_batches = tp.batch_document(text)

    summary_batches = []
    for i, batch in enumerate(text_batches):
        print(f'batch no. {i}')
        batch_summary = summarize_text(batch)
        summary_batches.append(batch_summary)

    summary = '\n'.join(summary for summary in summary_batches)

    f.close()

    with open(output_path + 'summary_for_' + file, 'w', encoding='utf8') as w:
        w.write(summary)

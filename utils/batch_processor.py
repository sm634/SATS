"""
THIS NEEDS TO BE RECODED INTO A FUNCTION THAT CAN PROCESS LARGE TEXTS INTO BATCHES MORE EFFICIENTLY TO FEED TO THE
MODEL.
"""

import os
import re

from prompts import summarize_text
from utils.text_preprocessor import TextPreprocessor

input_path = 'extraction_layer/data/input/text/'
output_path = 'extraction_layer/data/output/from_text/'

input_files = os.listdir(input_path)

tp = TextPreprocessor()

for file in input_files:
    if re.search('.txt', file):
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

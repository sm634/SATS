from nltk.tokenize import word_tokenize
from string import punctuation
from datetime import datetime


class TextPreprocessor:
    def __init__(self):
        self.numbers = [str(n) for n in range(0, 10)]
        self.tokenizer = 'nltk'

    @staticmethod
    def standardize(text):
        """
        Standardize text method: 1. Remove numbers, remove punctuation and lower case text.
        :return: str, standardized text.
        """
        text = ''.join([c for c in text if c not in punctuation])
        text = text.lower()
        return text

    def tokenize(self, text, tokenizer='standard'):
        """
        Tokenize text into list of words.
        :param text: the input text to be tokenized.
        :param tokenizer: the method of tokenizing the text or sentence. Current options: ['standard', 'nltk']
        :return: List of words.
        """
        text = self.standardize(text)
        if tokenizer == 'standard':
            return text.split()
        elif tokenizer == 'nltk':
            return word_tokenize(text)

    def batch_document(self, text, max_tokens=1000, save_batches=False, output_path='data/output/'):
        """Break the text down into a suitable length to not exceed the openai API max token length."""
        max_words_per_batch = int(max_tokens * 0.7)
        words = self.tokenize(text)
        n_batches = len(words) // max_words_per_batch

        if len(words) > 750:
            text_batches = []
            for i in range(0, n_batches):
                batch = words[(max_words_per_batch * i): max_words_per_batch * (i+1)]
                batch_text = ' '.join(word for word in batch)
                text_batches.append(batch_text)
                if save_batches:
                    """If save_batches option on then save the batches of text in the directory given in output_path"""
                    with open('data/input/batch/summary_' + str(datetime), 'w') as f:
                        f.write(batch_text)

            return text_batches
        else:
            return ' '.join(word for word in words)

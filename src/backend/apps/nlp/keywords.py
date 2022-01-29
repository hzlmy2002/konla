from collections import Counter
import pandas as pd

class KeywordExtractor:

    @staticmethod
    def extract_keywords(doc, n: int):
        """
        Extracts n most frequent tokens from doc
        and returns an html frequency table

            Parameters:
                doc    : spacy object after execution of standard spacy pipeline
                n (int): number of most frequent tokens to include
        """
        # Remove stop words and punctuation
        # Do we want any Part of Speech filter?
        # TODO: Change spacy tokenizer to ignore whitespace characters                   #TODO: to be removed
        words = [token.text for token in doc if not token.is_stop and not token.is_punct and token.text != '\n']
        word_freq = Counter(words)
        common_nouns = word_freq.most_common(n)
        return pd.DataFrame(common_nouns).values.tolist()

from collections import Counter
import pandas as pd

class KeywordExtractor:
    
    @staticmethod
    def extract_keywords(doc, n: int, html=False):
        """
        Extracts n most frequent tokens from doc
        and returns an html frequency table

            Parameters:
                doc    : spacy object after execution of standard spacy pipeline
                n (int): number of most frequent tokens to include
                html (bool) : return html table or a list of (index, keyword, frequency) 
        """
        # Remove stop words and punctuation
        # Do we want any Part of Speech filter?
        # TODO: Change spacy tokenizer to ignore whitespace characters                   #TODO: to be removed
        words = [token.text for token in doc if not token.is_stop and not token.is_punct and token.text != '\n' and token.pos_ != 'NUM' and token.pos_ != 'SYM' and len(token.text) > 1]
        word_freq = Counter(words)
        common_nouns = word_freq.most_common(n)
        res = []
        for i in range(len(common_nouns)):
            res.append((i+1, common_nouns[i][0], common_nouns[i][1]))
        if html:
            return pd.DataFrame(common_nouns).to_html()
        else:
            return res
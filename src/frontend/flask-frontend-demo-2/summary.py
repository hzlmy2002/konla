"""
I METHOD: Extractive Summarization with spacy based on cos similarity

1. Clean and seperate text into sentences
2. Build similarity matrix using cosine similarity (between each sentence)
3. 

"""
import os, sys
sys.path.append(os.path.abspath('.'))
from string import punctuation
import spacy
from collections import Counter
from heapq import nlargest
import pandas as pd
import numpy as np
# from gensim.summarization import summarize


nlp = spacy.load("en_core_web_lg")
STOP_WORDS = list(nlp.Defaults.stop_words)


class Summarizer:

    def __init__(self) -> None:
        pass

    def start(self, doc, n=5, mct=5):
        freq_word = self._get_most_common_tokens(doc, mct)
        sent_strength = self._weigh_sentences(doc, freq_word)
        res = nlargest(n, sent_strength, key=sent_strength.get)
        print(type(res))
        return res

    def _get_most_common_tokens(self, doc, n=5):
        keywords = []
        pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
        for token in doc:
            if (token.text in STOP_WORDS or token.text in punctuation):
                continue
            if token.pos_ in pos_tag:
                keywords.append(token.text)
        freq_word = Counter(keywords)
        # normalizing
        max_freq = freq_word.most_common(1)[0][1]
        for word in freq_word.keys():
            freq_word[word] = (freq_word[word]/max_freq)
        return freq_word
    
    def _weigh_sentences(self, doc, freq_word):
        sent_strength = {}
        for sent in doc.sents:
            for word in sent:
                if word.text in freq_word.keys():
                    if sent in sent_strength.keys():
                        sent_strength[sent] += freq_word[word.text]
                    else:
                        sent_strength[sent] = freq_word[word.text]
        return sent_strength

        

# def create_similarity_matrix(sentences, stop_words):
#     # create an empty similarity matrix
#     similarity_matrix = np.zeros((len(sentences), len(sentences)))

#     for sent_id_x in range(len(sentences)):
#         for sent_id_y in range(len(sentences)):
#             if sent_id_x != sent_id_y:
#                 continue
#             similarity_matrix[sent_id_x][sent_id_y] = sentence_similarity(sentences[sent_id_x], sentences[sent_id_y])
    
#     return similarity_matrix


if __name__ == "__main__":
    from PDFHelper import PDFHelper
    filepath = "konla_frontend/static/uploads/shapes.pdf"
    content = PDFHelper().pdf2text(filepath)
    doc = nlp(content)
    summarizer = Summarizer().start(doc)
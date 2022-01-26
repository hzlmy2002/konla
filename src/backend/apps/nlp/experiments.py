"""
This file is for nlp experiments and testing of unadded features
"""

import os
import sys
from spacy import matcher
sys.path.append(os.path.abspath('.'))
from PDFHelper import PDFHelper
import spacy
import en_core_web_lg
import pandas as pd
from tika import parser
from time import sleep
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_lg')

def remove_adjacent_duplicates(l: list):
    res = []
    for el in l:
        if el not in res:
            res.append(el)
    return res

def print_token_info(token):
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

def extract_headings():
    pdf_helper = PDFHelper()
    content = pdf_helper.pdf2text("shapes.pdf")
    print(pdf_helper.getTitle("shapes.pdf"))
    print(pdf_helper.getAuthor("shapes.pdf"))
    doc = nlp(content)
    matcher = Matcher(nlp.vocab)
    pattern_heading = [{"IS_DIGIT": True}, {"IS_TITLE": True, "OP": "+"}, {"IS_SENT_START":True, "OP":"!"}] # DIGIT that is start of the sentence + ANY TOKEN
    pattern_subheading_2 = [{"TEXT": {"REGEX": "[0-9]+\.[0-9]+"}},{"IS_TITLE":True, "OP": "+"},{"IS_SENT_START": True, "OP":"!"}]
    pattern_subheading = [{"IS_DIGIT": True, "TEXT": {"REGEX": "[0-9]+\.[0-9]+"}},{"IS_TITLE":True, "OP": "+"},{"IS_SENT_START": True, "OP":"!"}] # DIGIT that is start of the sentence + ANY TOKEN
    # pattern_subheading2 = [{"LIKE_NUM": True, "OP":"+"}, {"IS_TITLE": True, "OP": "+"}]
    matcher.add('match_heading', None, pattern_heading)
    matcher.add('match_subheading', None, pattern_subheading)
    matcher.add('match_subheading_2', None, pattern_subheading_2)
    matches = matcher(doc)
    print(f"NUMBER OF MATCHES: {len(matches)}")
    headings = []
    subheadings = []
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # get string representation
        span = doc[start:end]                    # get the matched span
        match = [span.text]
        if doc[end-1].is_stop:
            i = end
            while not doc[i].is_sent_start:
                match.append(" " + doc[i].text)
                i+=1
        match = "".join(match)
        if string_id == "match_heading" and match not in headings and match[-1] == "\n":
            headings.append(match.strip())
        if string_id == "match_subheading_2" and match not in subheadings and match[-1] == "\n":
            subheadings.append(match.strip())

    headings = remove_adjacent_duplicates(headings)
    subheadings = remove_adjacent_duplicates(subheadings)
    print(headings)
    print(subheadings)


if __name__ == "__main__":
    extract_headings()



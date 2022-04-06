from .sections import SectionExtractor
from collections import OrderedDict
# COMP0016-Team6-Bartosz Grabek 
class Summarizer:

    WHOLE_SUMMARY_LENGTH = 10
    SEGMENT_SUMMARY_LENGTH = 10

    def __init__(self, doc, nlp):
        self.doc = doc
        self.nlp = nlp

    def run_whole(self):
        return self.summary_extractive(doc=self.doc, n=self.WHOLE_SUMMARY_LENGTH)

    def run_partial(self) -> OrderedDict:
        sections = SectionExtractor(self.doc, self.nlp).run()
        section_summaries = OrderedDict()
        for section in sections:
            name, start_tk, end_tk, _ = section
            text = self.doc[start_tk:end_tk].text
            doc = self.nlp(text)   # sentencising span
            summary = self.summary_extractive(doc, self.SEGMENT_SUMMARY_LENGTH)
            section_summaries[name] = summary
        return section_summaries

    def summary_extractive(self, doc, n=5):
        """
        Extracts n best scoring sentences based on the sum of relative frequencies
        of keywords appearing in each sentence (sent_strength). By defeault mct=0 means
        all of the keywords relative frequencies will be taken into account, while mct > 1 will
        compute sentence score by summing up only the relative frequencies of top mct tokens 
        in the text.

        Parameters:
        doc (spacy doc object): Spacy doc object containing tokenised text
        n (int): Number of sentences to extract

        Returns:
        str: Concatanated n best scoring sentences in order
        """
        # STEP 1. Text preprocessing
        #print(type(doc))
        keywords = dict()
        num_tks = 0
        for tk in doc: 
            if not any([tk.is_space, tk.like_num, tk.is_stop, tk.is_punct, tk.is_digit, tk.text in ['\\n', '\n', '.']]):
                num_tks += 1
                tk = tk.lower_
                if tk in keywords.keys():
                    keywords[tk] += 1
                else:
                    keywords[tk] = 1
        # Change dictionary values to relative frequency
        for key, value in keywords.items():
            keywords[key] = value / num_tks
        # Score sentences based on the keywords and their relative frequency
        sentences = []
        for sent in doc.sents:
            sent_score = 0
            for tk in sent:
                tk = tk.lower_
                if tk in keywords.keys():
                    sent_score += keywords[tk]
            sentences.append((sent_score, sent))
        # get n sentences with highest scores
        sentences.sort(key=lambda item: item[0], reverse=True)
        best_sents = [item[1].text for item in sentences[:n]]
        return " ".join(best_sents)

# Potential additional arg for extractive summarization
# mct (int): optional argument, number of top keywords to take into account
# when computing sentence score, default 0 means all
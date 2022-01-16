""" Konla App - 2022 """
import os, sys
import spacy
from keywords import KeywordExtractor
from text_metrics import TextMetricsCalculator

sys.path.append(os.path.abspath('..'))
from PDFHelper import PDFHelper

class Analyser():
    """
    Extracts text from a paper and runs analysis on the content
    """
    def __init__(self, filepath:str):
        extension = os.path.splitext(filepath)[1].lower()
        if extension != ".pdf":
            self.error = "Error: Images cannot be processed currently"
        else:
            try:
                nlp_model = spacy.load("en_core_web_trf")
                print("Model loaded (1/5)")
                self.content = PDFHelper().pdf2text(filepath)
                print("Text extracted (2/5)")
                doc = nlp_model(self.content)  # doc = tokenised_content
                a=[t for t in doc] 
                print("Text analysed (3/5)")
                self.keywords_html = KeywordExtractor().extract_keywords(doc, n=10)
                print("Keywords extracted (4/5)")
                self.text_metrics_html = TextMetricsCalculator().get_metrics_html_table(doc)
                print("Text Metrics Computed (5/5)")
                self.error = None
            except Exception as e:
                print(e)
                self.error = "Error: Paper could not be analysed"

    def get_error(self):
        return self.error

    def get_extracted_text(self):
        return self.content

    def get_keywords_html(self):
        return self.keywords_html

    def get_text_metrics(self):
        return self.text_metrics_html

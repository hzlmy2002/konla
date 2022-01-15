""" Konla App - 2022 """
import os
from pdf_to_text import PDFToText
from keywords import KeywordExtractor
from text_metrics import TextMetricsCalculator


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
                self.content = PDFToText().get_content(filepath)

                # self.keywords_html = KeywordExtractor().extract_keywords(
                #     self.content, n=10)

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
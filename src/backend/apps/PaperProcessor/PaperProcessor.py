import spacy
import sys
from wordFrequency import wordFrequency
sys.path.append("../")
from PDFHelper import PDFHelper

class PaperProcessor():
    def __init__(self,doc:"spacy.tokens.doc.Doc") -> None:
        self.doc=doc
    
    def wordFrequency(self,max=10,ignoreCase=False,useLemma=False) -> dict:
        wf=wordFrequency(self.doc,max,ignoreCase,useLemma)
        return wf.getWordFrequency()

def test():
    nlp = spacy.load("en_core_web_lg")
    text=PDFHelper.pdf2text("shapes.pdf")
    doc = nlp(text)
    pp=PaperProcessor(doc)
    print(pp.wordFrequency(max=20,useLemma=True))

#test()
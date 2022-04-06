from typing import List, OrderedDict
import spacy
from .wordFrequency import wordFrequency
from .PDFHelper.PDFHelper import PDFHelper
from .refs import Ref
from .authors import AuthorParser
from .sections import SectionExtractor
from .summary import Summarizer
# COMP0016-Team6-Minyi_Lei, Bartosz_Grabek 

class PaperProcessor():
    def __init__(self,path:str) -> None:
        text = self.preprocessText(PDFHelper.pdf2text(path))
        self.metadata = PDFHelper.getMetaData(path)
        self.nlpTRF = spacy.load("en_core_web_trf")
        self.doc = self.nlpTRF(text)

    def preprocessText(self, text: str) -> str:
        text = text.replace("’", "'")  # handle tricky chars
        return text
    
    def wordFrequency(self,max=10,ignoreCase=False,useLemma=False) -> dict:
        wf = wordFrequency(self.doc,max,ignoreCase,useLemma)
        return wf.getWordFrequency()

    def metaData(self) -> dict:
        self.metadata["authors"] = self.getAuthor()
        return self.metadata

    def getAuthor(self) -> List[str]:
        ap = AuthorParser(self.doc)
        return ap.run()

    def wordCount(self) -> int:
        count=0
        for token in self.doc:
            if not token.is_punct:
                count+=1
        return count

    def metrics(self) -> dict:
        result={}
        result["wordCount"] = self.wordCount()
        result["readingTime"] = 60*self.wordCount()//250
        result["speakingTime"] = 60*self.wordCount()//130
        return result

    def references(self) -> List[str]:
        refs = Ref(self.doc,self.nlpTRF)
        return refs.run()

    def sections(self) -> List[str]:
        extractor = SectionExtractor(self.doc, self.nlpTRF)
        return extractor.run()

    def summarize_whole(self) -> str: # Or should it be List[str]
        summarizer = Summarizer(self.doc, self.nlpTRF)
        return summarizer.run_whole()

    def summarize_partial(self) -> OrderedDict:
        # returns ordered dict where key is title of section, value is its summary
        summarizer = Summarizer(self.doc, self.nlpTRF)
        return summarizer.run_partial()


def test():
    pp=PaperProcessor("/tmp/typestudy.pdf")
    print(pp.wordFrequency(max=20,useLemma=True))
    print(pp.wordCount())
    print(pp.metaData())
    print(pp.metrics())
    print(pp.references())
    print(pp.sections())
    print(pp.summarize_whole)
    print(pp.summarize_partial)

#test()
# For in-container testing
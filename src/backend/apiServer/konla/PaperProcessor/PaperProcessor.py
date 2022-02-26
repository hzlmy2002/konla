from typing import List
import spacy
from .wordFrequency import wordFrequency
from .PDFHelper.PDFHelper import PDFHelper
from .refs import Ref
from .authors import AuthorParser

class PaperProcessor():
    def __init__(self,path:str) -> None:
        text=PDFHelper.pdf2text(path)
        self.metadata=PDFHelper.getMetaData(path)
        self.nlpTRF=spacy.load("en_core_web_trf")
        self.doc=self.nlpTRF(text)
    
    def wordFrequency(self,max=10,ignoreCase=False,useLemma=False) -> dict:
        wf=wordFrequency(self.doc,max,ignoreCase,useLemma)
        return wf.getWordFrequency()

    def metaData(self) -> dict:
        return self.metadata

    def getAuthor(self) -> List[str]:
        ap=AuthorParser(self.doc)
        return ap.run()

    def wordCount(self)-> int:
        count=0
        for token in self.doc:
            if not token.is_punct:
                count+=1
        return count

    def metrics(self)->dict:
        result={}
        result["wordcount"]=self.wordCount()
        result["readingtime"]=self.wordCount()//238
        result["speakingtime"]=self.wordCount()//140

        return result

    def references(self)->List[str]:
        refs=Ref(self.doc,self.nlpTRF)
        return refs.run()

def test():
    pp=PaperProcessor("typestudy.pdf")
    print(pp.wordFrequency(max=20,useLemma=True))
    print(pp.getAuthor())
    print(pp.wordCount())
    print(pp.metaData())
    print(pp.metrics())
    print(pp.references())

#test()
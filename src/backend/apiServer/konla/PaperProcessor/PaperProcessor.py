from typing import List
import spacy
import sys
from .wordFrequency import wordFrequency
sys.path.append("../")
from .PDFHelper.PDFHelper import PDFHelper
from .refs import Ref


class PaperProcessor():
    def __init__(self,path:str) -> None:
        text=PDFHelper.pdf2text(path)
        self.metadata=PDFHelper.getMetaData(path)
        self.doc=spacy.load("en_core_web_trf")(text)
    
    def wordFrequency(self,max=10,ignoreCase=False,useLemma=False) -> dict:
        wf=wordFrequency(self.doc,max,ignoreCase,useLemma)
        return wf.getWordFrequency()

    def MetaData(self) -> dict:
        return self.metadata

    def getAuthor(self) -> List[str]:
        pass

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
        refs=Ref(self.doc)
        return refs.run()

def test():
    pp=PaperProcessor("shapes.pdf")
    print(pp.wordFrequency(max=20,useLemma=True))
    print(pp.MetaData())
    print(pp.metrics())

#test()
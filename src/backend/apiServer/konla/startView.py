from ast import keyword
from django.core.cache import cache
from .form import selectionForm

from .PaperProcessor.PaperProcessor import PaperProcessor
from threading import Thread,Lock


class Container():
    def __init__(self,content) -> None:
        self.ccontent=content
    def load(self,content):
        self.ccontent=content
    def get(self):
        return self.ccontent


def startProcessing(request):
    try:
        if request.method=="POST":
            form=selectionForm(request.POST)
            if not form.is_valid():
                raise Exception("Invalid form!")

        featureTable={
            "enableWholeSummarisation":True if form.cleaned_data["whole"] == 1 else False,
            "enablePartialSummarisation":True if form.cleaned_data["partial"] == 1 else False,
            "enableKeywords":True if form.cleaned_data["keywords"] == 1 else False,
            "enableRefs":True if form.cleaned_data["refs"] == 1 else False,
            "enableMeta":True if form.cleaned_data["meta"] == 1 else False,
            "enableMetrics":True if form.cleaned_data["metrics"] == 1 else False
        }
        
        checksum=request.session["paperFingerprint"]
        if request.session["uploadedFile"] == None:
            raise Exception("No file uploaded!")

        threadMain=Thread(target=mainThread,args=(request.session["uploadedFile"],checksum,featureTable))
        threadMain.start()
        

        response={"status":1}

    except Exception as e:
        response={
            "status": 0,
            "errors": [str(e)],
            "messages": [],
            "result": {}
        }
    finally:
        return response

def mainThread(path,prefix,featureTable):
    pp=PaperProcessor(path)
    keyword=Thread(target=keywordThread,args=(prefix,pp))
    keyword.start()


def keywordThread(prefix,paperProcessor):
    normalResult=paperProcessor.wordFrequency(max=100,ignoreCase=False,useLemma=False)
    ignoreCaseResult=paperProcessor.wordFrequency(max=100,ignoreCase=True,useLemma=False)
    lemmaResult=paperProcessor.wordFrequency(max=100,ignoreCase=False,useLemma=True)
    result={
        "normal": normalResult,
        "ignoreCase": ignoreCaseResult,
        "lemma": lemmaResult
    }
    cache.set(prefix+"_keywords",result)



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
        
        if request.session["uploadedFile"] == None:
            raise Exception("No file uploaded!")
        checksum=request.session["paperFingerprint"]
        threadMain=Thread(target=mainThread,args=(request.session["uploadedFile"],checksum,featureTable))
        threadMain.start()

        response={
            "status": 1,
            "errors": [],
            "messages": [],
            "result": {}
        }

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
    cache.set(prefix+"_initialized",0)
    pp=PaperProcessor(path)

    print("Init done")

    if featureTable["enableWholeSummarisation"]:
        pass
    else:
        pass
    if featureTable["enablePartialSummarisation"]:
        pass
    else:
        pass
    if featureTable["enableKeywords"]:
        keyword=Thread(target=keywordThread,args=(prefix,pp))
        cache.set(prefix+"_keywords_completed",0)
        keyword.start()
    else:
        cache.set(prefix+"_keywords_completed",-1)
    if featureTable["enableRefs"]:
        refs=Thread(target=referencesThread,args=(prefix,pp))
        cache.set(prefix+"_refs_completed",0)
        refs.start()
    else:
        cache.set(prefix+"_refs_completed",-1)
    if featureTable["enableMeta"]:
        meta=Thread(target=metadataThread,args=(prefix,pp))
        cache.set(prefix+"_meta_completed",0)
        meta.start()
    else:
        cache.set(prefix+"_meta_completed",-1)
    if featureTable["enableMetrics"]:
        metrics=Thread(target=metricsThread,args=(prefix,pp))
        cache.set(prefix+"_metrics_completed",0)
        metrics.start()
    else:
        cache.set(prefix+"_metrics_completed",-1)
    cache.set(prefix+"_initialized",1)

    """
    ### debug only, delete before submission
    keyword.join()
    refs.join()
    meta.join()
    metrics.join()
    print(cache.get(prefix+"_keywords"))
    print(cache.get(prefix+"_keywords_completed"))
    print(cache.get(prefix+"_refs"))
    print(cache.get(prefix+"_refs_completed"))
    print(cache.get(prefix+"_meta"))
    print(cache.get(prefix+"_meta_completed"))
    print(cache.get(prefix+"_metrics"))
    print(cache.get(prefix+"_metrics_completed"))
    """
    


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
    cache.set(prefix+"_keywords_completed",1) # -1 means feature disabled, 0 means feature in progress, 1 means feature completed

def referencesThread(prefix,paperProcessor):
    refs=paperProcessor.references()
    cache.set(prefix+"_refs",refs)
    cache.set(prefix+"_refs_completed",1)

def metadataThread(prefix,paperProcessor):
    meta=paperProcessor.metaData()
    cache.set(prefix+"_meta",meta)
    cache.set(prefix+"_meta_completed",1)

def metricsThread(prefix,paperProcessor):
    metrics=paperProcessor.metrics()
    cache.set(prefix+"_metrics",metrics)
    cache.set(prefix+"_metrics_completed",1)



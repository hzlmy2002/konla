from django.core.cache import cache
from .form import selectionForm

from .PaperProcessor.PaperProcessor import PaperProcessor
from threading import Thread

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
            "enableMeta":True if form.cleaned_data["metadata"] == 1 else False,
            "enableMetrics":True if form.cleaned_data["metrics"] == 1 else False
        }
        if "paperFingerprint" not in request.session:
            raise Exception("No file uploaded! Session data missing!")
        checksum=request.session["paperFingerprint"]
        cache.set(checksum+"_featureTable",featureTable,timeout=3600)
        threadMain=Thread(target=mainThread,args=(request.session["uploadedFile"],checksum,featureTable))
        threadMain.start()

        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {}
        }

    except Exception as e:
        response={
            "current_status": 0,
            "errors": [str(e)],
            "messages": [],
            "result": {}
        }
    finally:
        return response

def mainThread(path,prefix,featureTable):
    cache.set(prefix+"_initialized",False,timeout=3600)
    pp=PaperProcessor(path)

    if featureTable["enableWholeSummarisation"]:
        whole=Thread(target=wholeSummarisationThread,args=(prefix,pp))
        cache.set(prefix+"_whole_completed",False,timeout=3600)
        whole.start()
    if featureTable["enablePartialSummarisation"]:
        partial=Thread(target=partialSummarisationThread,args=(prefix,pp))
        cache.set(prefix+"_partial_completed",False,timeout=3600)
        partial.start()
    if featureTable["enableKeywords"]:
        keyword=Thread(target=keywordThread,args=(prefix,pp))
        cache.set(prefix+"_keywords_completed",False,timeout=3600) # 0: in progress, 1: completed, -1: disabled
        keyword.start()

    if featureTable["enableRefs"]:
        refs=Thread(target=referencesThread,args=(prefix,pp))
        cache.set(prefix+"_refs_completed",False,timeout=3600)
        refs.start()
    
    if featureTable["enableMeta"]:
        meta=Thread(target=metadataThread,args=(prefix,pp))
        cache.set(prefix+"_meta_completed",False,timeout=3600)
        meta.start()
    
    if featureTable["enableMetrics"]:
        metrics=Thread(target=metricsThread,args=(prefix,pp))
        cache.set(prefix+"_metrics_completed",False,timeout=3600)
        metrics.start()
    
    cache.set(prefix+"_initialized",True,timeout=3600)

def wholeSummarisationThread(prefix,paperProcessor):
    summary=paperProcessor.summarize_whole()
    cache.set(prefix+"_whole",summary,timeout=3600)
    cache.set(prefix+"_whole_completed",True,timeout=3600)

def partialSummarisationThread(prefix,paperProcessor):
    summary=paperProcessor.summarize_partial()
    cache.set(prefix+"_partial",summary,timeout=3600)
    cache.set(prefix+"_partial_completed",True,timeout=3600)

def keywordThread(prefix,paperProcessor):
    normalResult=paperProcessor.wordFrequency(max=100,ignoreCase=False,useLemma=False)
    ignoreCaseResult=paperProcessor.wordFrequency(max=100,ignoreCase=True,useLemma=False)
    lemmaResult=paperProcessor.wordFrequency(max=100,ignoreCase=False,useLemma=True)
    result={
        "normal": normalResult,
        "ignoreCase": ignoreCaseResult,
        "lemma": lemmaResult
    }
    #time.sleep(60)
    cache.set(prefix+"_keywords",result,timeout=3600)
    cache.set(prefix+"_keywords_completed",True,timeout=3600) # -1 means feature disabled, 0 means feature in progress, 1 means feature completed

def referencesThread(prefix,paperProcessor):
    refs=paperProcessor.references()
    cache.set(prefix+"_refs",refs,timeout=3600)
    cache.set(prefix+"_refs_completed",True,timeout=3600)

def metadataThread(prefix,paperProcessor):
    meta=paperProcessor.metaData()
    cache.set(prefix+"_meta",meta,timeout=3600)
    cache.set(prefix+"_meta_completed",True,timeout=3600)

def metricsThread(prefix,paperProcessor):
    metrics=paperProcessor.metrics()
    cache.set(prefix+"_metrics",metrics,timeout=3600)
    cache.set(prefix+"_metrics_completed",True,timeout=3600)



from django.core.cache import cache
# COMP0016-Team6-Minyi Lei



def provideWholeSummarisation(request):
    try:
        prefix=request.session["paperFingerprint"]
    except KeyError:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    if cache.get(prefix+"_initialized")==None:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_featureTable")["enableWholeSummarisation"]==False:
        return {
            "current_status": 0,
            "errors": ["Whole summarisation is disabled!"],
            "messages": [],
            "result": {}
        }
    
    elif cache.get(prefix+"_initialized")==False:
        return {
            "current_status": -1,
            "errors": ["System initializing, analysis did not start yet!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_whole_completed") == False:
        return {
            "current_status": -1,
            "errors": ["Whole summarisation is in progress!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_whole_completed") == True:
        result=cache.get(prefix+"_whole")
        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {"whole_summarisation":result}
        }
        return response
    else:
        return {
            "current_status": 0,
            "errors": ["Unknown error!"],
            "messages": [],
            "result": {}
        }

def providePartialSummarisation(request):
    try:
        prefix=request.session["paperFingerprint"]
    except KeyError:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    if cache.get(prefix+"_initialized")==None:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_featureTable")["enablePartialSummarisation"]==False:
        return {
            "current_status": 0,
            "errors": ["Partial summarisation is disabled!"],
            "messages": [],
            "result": {}
        }
    
    elif cache.get(prefix+"_initialized")==False:
        return {
            "current_status": -1,
            "errors": ["System initializing, analysis did not start yet!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_partial_completed") == False:
        return {
            "current_status": -1,
            "errors": ["Partial summarisation is in progress!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_partial_completed") == True:
        result=cache.get(prefix+"_partial")
        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {"partial_summarisation":result}
        }
        return response
    else:
        return {
            "current_status": 0,
            "errors": ["Unknown error!"],
            "messages": [],
            "result": {}
        }


def provideKeywords(request):
    try:
        prefix=request.session["paperFingerprint"]
    except KeyError:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    if cache.get(prefix+"_initialized")==None: # avoid key error
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_featureTable")["enableKeywords"]==False:
        return {
            "current_status": 0,
            "errors": ["Keywords analysis is disabled!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_initialized")==False:
        return {
            "current_status": -1,
            "errors": ["System initializing, analysis did not start yet!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_keywords_completed") == False:
        return {
            "current_status": -1,
            "errors": ["Keywords analysis is in progress!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_keywords_completed") == True:
        result=cache.get(prefix+"_keywords")
        if request.GET.get("max") != None:
            maxNum=int(request.GET.get("max"))
        else:
            maxNum=100
        ignoreCase=True if request.GET.get("ignorecase") == "1" else False
        extractLemma=True if request.GET.get("extractlemma") == "1" else False
        provisionalResult={}
        if extractLemma:
            provisionalResult=result["lemma"]
        elif ignoreCase:
            provisionalResult=result["ignoreCase"]
        else:
            provisionalResult=result["normal"]
        finalResultKey=sorted(provisionalResult,key=lambda x:provisionalResult[x],reverse=True)[:maxNum]
        finalResult={}
        for i in finalResultKey:
            finalResult[i]=provisionalResult[i]
        
        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {"keywords":finalResult}
        }
        return response
    else:
        return {
            "current_status": 0,
            "errors": ["Unknown error!"],
            "messages": [],
            "result": {}
        }


def provideRefs(request):
    try:
        prefix=request.session["paperFingerprint"]
    except KeyError:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    if cache.get(prefix+"_initialized")==None:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_featureTable")["enableRefs"]==False:
        return {
            "current_status": 0,
            "errors": ["References extraction is disabled!"],
            "messages": [],
            "result": {}
        }
    
    elif cache.get(prefix+"_initialized")==False:
        return {
            "current_status": -1,
            "errors": ["System initializing, analysis did not start yet!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_refs_completed") == False:
        return {
            "current_status": -1,
            "errors": ["References extraction is in progress!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_refs_completed") == True:
        result=cache.get(prefix+"_refs")
        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {"refs":result}
        }
        return response
    else:
        return {
            "current_status": 0,
            "errors": ["Unknown error!"],
            "messages": [],
            "result": {}
        }






def provideMeta(request):
    try:
        prefix=request.session["paperFingerprint"]
    except KeyError:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    if cache.get(prefix+"_initialized")==None:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_featureTable")["enableMeta"]==False:
        return {
            "current_status": 0,
            "errors": ["Metadata extraction is disabled!"],
            "messages": [],
            "result": {}
        }
    
    elif cache.get(prefix+"_initialized")==False:
        return {
            "current_status": -1,
            "errors": ["System initializing, analysis did not start yet!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_meta_completed") == False:
        return {
            "current_status": -1,
            "errors": ["Metadata extraction is in progress!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_meta_completed") == True:
        result=cache.get(prefix+"_meta")
        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {"metadata":result}
        }
        return response
    else:
        return {
            "current_status": 0,
            "errors": ["Unknown error!"],
            "messages": [],
            "result": {}
        }






def provideMetric(request):
    try:
        prefix=request.session["paperFingerprint"]
    except KeyError:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    if cache.get(prefix+"_initialized")==None:
        return {
            "current_status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_featureTable")["enableMetrics"]==False:
        return {
            "current_status": 0,
            "errors": ["Metrics is disabled!"],
            "messages": [],
            "result": {}
        }
    
    elif cache.get(prefix+"_initialized")==False:
        return {
            "current_status": -1,
            "errors": ["System initializing, Metrics did not start yet!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_metrics_completed") == False:
        return {
            "current_status": -1,
            "errors": ["Metrics extraction is in progress!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_metrics_completed") == True:
        result=cache.get(prefix+"_metrics")
        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {"metrics":result}
        }
        return response
    else:
        return {
            "current_status": 0,
            "errors": ["Unknown error!"],
            "messages": [],
            "result": {}
        }
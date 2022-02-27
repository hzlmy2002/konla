from django.core.cache import cache



def provideKeywords(request):
    prefix=request.session["paperFingerprint"]
    if cache.get(prefix+"_featureTable")["enableKeywords"]==False:
        return {
            "status": 0,
            "errors": ["Keywords analysis is disabled!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_initialized")==None:
        return {
            "status": 0,
            "errors": ["No file uploaded!"],
            "messages": [],
            "result": {}
        }
    
    elif cache.get(prefix+"_initialized")==False:
        return {
            "status": -1,
            "errors": ["System initializing, analysis did not start yet!"],
            "messages": [],
            "result": {}
        }
    elif cache.get(prefix+"_keywords_completed") == False:
        return {
            "status": -1,
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
            "status": 1,
            "errors": [],
            "messages": [],
            "result": finalResult
        }
        return response
    else:
        return {
            "status": 0,
            "errors": ["Unknown error!"],
            "messages": [],
            "result": {}
        }

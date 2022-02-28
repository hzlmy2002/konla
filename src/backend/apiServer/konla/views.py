from urllib import response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


import json
import time
from threading import Thread
from django.core.cache import cache

from . import uploadingView
from . import startView
from . import dataProviderView

# Create your views here.

@csrf_exempt
def uploadFile(request):
    response=uploadingView.acceptFile(request)
    if response["status"] == 1:
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        httpResponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpResponse.status_code=400
        return httpResponse

def uploadURL(request):
    response=uploadingView.acceptURL(request)
    if response["status"] == 1:
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        httpResponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpResponse.status_code=400
        return httpResponse

@csrf_exempt
def uploadStart(request):
    response=startView.startProcessing(request)
    if response["status"] == 1:
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        httpResponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpResponse.status_code=400
        return httpResponse


def keywords(request):
    response=dataProviderView.provideKeywords(request)
    if response["status"] != 0:
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        httpResponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpResponse.status_code=400
        return httpResponse

def infoRefs(request):
    response=dataProviderView.provideRefs(request)
    if response["status"] != 0:
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        httpResponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpResponse.status_code=400
        return httpResponse

def infoMeta(request):
    response=dataProviderView.provideMeta(request)
    if response["status"] != 0:
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        httpResponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpResponse.status_code=400
        return httpResponse

def infoMetrics(request):
    response=dataProviderView.provideMetric(request)
    if response["status"] != 0:
        return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        httpResponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpResponse.status_code=400
        return httpResponse

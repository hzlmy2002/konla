from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt


import json
import time
from threading import Thread
from django.core.cache import cache

from . import uploadingView

# Create your views here.

def testSessionInThread(checksum):
    for i in range(100):
        if cache.get(checksum)==None:
            cache.set(checksum,0,timeout=None)
        else:
            cache.incr(checksum)
        time.sleep(1)

def stat(request):
    return HttpResponse("{}".format(cache.get("1")))

def index(request):
    thread=Thread(target=testSessionInThread,args=("1",))
    thread.start()
    return HttpResponse("Hello, world. You're at the index.")

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
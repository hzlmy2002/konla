from time import time
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt

from .PaperProcessor.PaperProcessor import PaperProcessor
from .PaperProcessor.PDFHelper.PDFHelper import PDFHelper
import requests
from .models import PaperFile
import hashlib
from pathlib import Path
import json
import os

import time
from threading import Thread
from django.core.cache import cache

# Create your views here.

def testSessionInThread(checksum):
    for i in range(100):
        if cache.get(checksum)==None:
            cache.set(checksum,0,timeout=3000)
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
def acceptFile(request):
    try:
        if len(request.FILES)!=0:
            for i in request.FILES.values():
                uploadedFile=i
        else:
            raise Exception("No file uploaded")

        fileContent=uploadedFile.read()
        fileName=uploadedFile.name
        savedPath=Path(os.path.join("/tmp",fileName))
        with savedPath.open("wb") as f:
            f.write(fileContent)
        with savedPath.open("rb") as f:
            fingerprint=hashlib.sha256(f.read()).hexdigest()
            existingPaper=PaperFile.objects.filter(fingerprint=fingerprint)
            if len(existingPaper)==0:
                PaperText=PDFHelper.pdf2text(savedPath)
                pf=PaperFile(name=fileName,fingerprint=fingerprint,file=File(f,name=fileName))
                pf.save()
            else:
                PaperText=PDFHelper.pdf2text(existingPaper[0].file.path)

        request.session["uploadedFile"]=fileName
        request.session["paperFingerprint"]=fingerprint

        response={
            "success": True,
            "errors": [],
            "messages": [],
            "result": {
    	        "sha256": fingerprint,
    	        "text": PaperText
            }
        }


        return HttpResponse(json.dumps(response),content_type="application/json")

    except Exception as e:
        response={
            "success": False,
            "errors": [str(e)],
            "messages": [],
            "result": {}
        }

        httpresponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpresponse.status_code=400
        return httpresponse


def acceptURL(request):
    try:
        url=request.GET.get("link")
        fileContent=requests.get(url).content
        fileName=url.split("/")[-1]
        savedPath=Path(os.path.join("/tmp",fileName))
        with savedPath.open("wb") as f:
            f.write(fileContent)
        with savedPath.open("rb") as f:
            fingerprint=hashlib.sha256(f.read()).hexdigest()
            existingPaper=PaperFile.objects.filter(fingerprint=fingerprint)
            if len(existingPaper)==0:
                PaperText=PDFHelper.getText(savedPath)
                pf=PaperFile(name=fileName,fingerprint=fingerprint,file=File(f,name=fileName))
                pf.save()
            else:
                PaperText=PDFHelper.pdf2text(existingPaper[0].file.path)

        request.session["uploadedFile"]=fileName
        request.session["paperFingerprint"]=fingerprint

        response={
            "success": True,
            "errors": [],
            "messages": [],
            "result": {
    	        "sha256": fingerprint,
    	        "text": PaperText
            }
        }


        return HttpResponse(json.dumps(response),content_type="application/json")

    except Exception as e:
        response={
            "success": False,
            "errors": [str(e)],
            "messages": [],
            "result": {}
        }

        httpresponse=HttpResponse(json.dumps(response),content_type="application/json")
        httpresponse.status_code=400
        return httpresponse





    
    

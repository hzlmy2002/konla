from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files import File

from konla.PaperProcessor.PaperProcessor import PaperProcessor
from .PaperProcessor.PDFHelper.PDFHelper import PDFHelper
import requests
from .models import PaperFile
import hashlib
from pathlib import Path
import json
import os

# Create your views here.

def index(request):
    if "times" not in request.session:
        request.session["times"] = 0
        return HttpResponse("Hello World!")
    else:
        request.session["times"] += 1
        return HttpResponse("Hello World! {}".format(request.session["times"]))

def acceptFile(request):
    return HttpResponse("Uploading file")

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
            pf=PaperFile(name=fileName,fingerprint=fingerprint,file=File(f,name=fileName))
            pf.save()

        request.session["uploadedFile"]=fileName
        request.session["paperFingerprint"]=fingerprint

        response={
            "success": True,
            "errors": [],
            "messages": [],
            "result": {
    	        "sha256": fingerprint,
    	        "text": PDFHelper.pdf2text(savedPath),
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





    
    

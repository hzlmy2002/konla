from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt

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





    
    

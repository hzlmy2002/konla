import requests
from pathlib import Path
import hashlib
from .PaperProcessor.PDFHelper.PDFHelper import PDFHelper
import os

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
            PaperText=PDFHelper.pdf2text(savedPath)
               
        request.session["uploadedFile"]=os.path.join("/tmp",fileName)
        request.session["paperFingerprint"]=fingerprint
        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {
    	        "sha256": fingerprint,
    	        "text": PaperText
            }
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
            PaperText=PDFHelper.pdf2text(savedPath)
               
        request.session["uploadedFile"]=os.path.join("/tmp",fileName)
        request.session["paperFingerprint"]=fingerprint
        response={
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {
    	        "sha256": fingerprint,
    	        "text": PaperText
            }
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
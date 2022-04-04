import PyPDF2
import subprocess
# Written by Minyi Lei

class PDFHelper():
    def __init__(self) -> None:
        pass
    @staticmethod
    def pdf2text(path:str):
        proc=subprocess.Popen(["pdftotext","-nopgbrk","-raw",path,"/dev/stdout"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result=proc.communicate()
        if result[1]:
            raise Exception(result[1])
        else:
            return result[0].decode("utf-8")

    @staticmethod
    def getMetaData(path:str):
        with open(path,"rb") as f:
            pdf=PyPDF2.PdfFileReader(f)
            info=pdf.getDocumentInfo()
        data={}
        data["author"]=""
        data["creator"]=info.creator if info.creator else ""
        data["producer"]=info.producer if info.producer else ""
        data["subject"]=info.subject if info.subject else ""
        data["title"]=info.title if info.title else ""
        return data
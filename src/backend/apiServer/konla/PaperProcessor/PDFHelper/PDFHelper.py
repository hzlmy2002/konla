import PyPDF2
import subprocess

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
        data["Author"]=info.author
        data["Creator"]=info.creator
        data["Producer"]=info.producer
        data["Subject"]=info.subject
        data["Title"]=info.title
        return data
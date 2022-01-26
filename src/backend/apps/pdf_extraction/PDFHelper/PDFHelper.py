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
    def getAuthor(path:str):
        pdf=PyPDF2.PdfFileReader(open(path,"rb"))
        return pdf.getDocumentInfo().author

    @staticmethod
    def getTitle(path:str):
        pdf=PyPDF2.PdfFileReader(open(path,"rb"))
        return pdf.getDocumentInfo().title
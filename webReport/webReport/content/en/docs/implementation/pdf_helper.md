---
title: "PDF helper (PDF file operations)"
linkTitle: "PDF helper (PDF file operations)"
weight: 5
date: 2022-4-01
description: >
  Implementation of the PDF helper
---

PDF helper is a very simple object which abstracts the PDF file operations. It supports the following features:
- PDF text extractions
- PDF metadata reading

### PDF text extractions
The way we extract the text from pdf files is by invoking poppler's command:  pdftotext. This is a linux command which can output the result to stdout. Thus, we use subprocess.Popen to execute the command and read the output.
```python
def pdf2text(path:str):
    proc=subprocess.Popen(["pdftotext","-nopgbrk","-raw",path,"/dev/stdout"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result=proc.communicate()
    if result[1]:
        raise Exception(result[1])
    else:
        return result[0].decode("utf-8")
```

### PDF metadata reading
This is implemented by using PyPDF2. PyPDF2 can read the metadata of the pdf file.
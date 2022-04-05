---
title: "PDF-to-Text Conversion"
linkTitle: "PDF-to-Text Conversion"
weight: 1
date: 2022-4-01
description: >
  In this section we describe the pdf-to-text tools we explored and explain our final choice for the system.
  
---

### Objectives
Because research papers are commonly written, published and shared in a **.pdf** file format, we had to find a tool to extract text from this type of files. We wanted to find a tool that can be accurate as well as fast enough to meet usability standards. In particular we researched the following methods:
* [Tika](#tika)
* [Optical Image Recognition](#optical-image-recognition-ocr)
* [LibreOffice PDF-to-doc-to-text](#pdf-to-doc-to-text-method)
* [Poppler](#poppler)

To see our final choice, scroll down to [Final Choice](#final-choice) heading.

### Tika

One of the tools we explored was Tika. Tika is a Java library that can extract text content from various file types. It detects the type of file and uses a parser appropriate to that type to fetch its content. We found that there is a way to use Tika in python programme with the use of tika Python library. The Python library connects with the external Java program which then communicates with an Apache server where the PDF is processed. The downside is that Java Runtime needs to be installed on the machine.

**Experimental Usage**

Using the `from_file()` method, Tika understands the file is a PDF and, after processing, returns a data dictionary.
```python
from tika import parser as tikaParser
pdf_filename = "paper.pdf"
pdf_data_dict = tikaParser.from_file(pdf_filename)
```

The data dictionary has three keys metadata, content, status. Content is the most important as it is the extracted text. Metadata is somewhat useful as it contains properties of the PDF file.
```python
metadata = pdf_data_dict['metadata']
content = pdf_data_dict['content']
```
Many research papers will contain mathematical symbols. Therefore, the content needs to be converted to UTF-8 before being written to a file. This function writes each encoded line of the extracted text into a file.
```python
def save_content(content):
    with open("pdf_text_output.txt", "wb") as f:
        content_split = content.split("\n")
        for line in content_split:
            # Check line has content
            if len(line) > 0:
                try:
                    encoded_line = (line + '\n').encode("utf8")
                    f.write(encoded_line)
                except:
                    pass
```

At this stage, we can extract text from a PDF using the Tika library. Although the output is not perfect, some of the flaws lie in formulas, we need it for NLP to build summaries of sections which doesn't need perfectly written data.

**Tika Summary**

Pros of Tika:
* quite accurate, successfully recognises text in .pdf and parses it correctly in most situations

Cons of Tika:
* medium speed
* the need to connect to the server
* dependent on Java Runtime

### Optical Image Recognition (OCR)
Another approach to extracting text from a research paper is to use **OCR**, which stands for **Optical Image Recognition**. This method looks for characters in the image and generates the content of the paper. Each page of the .pdf file must be converted into an image before applying OCR. Using this method can aid researchers who have images of written research papers instead of .pdf files; however this is very uncommon and should not outweigh the most important factor such as pdf-to-text conversion performance.

**Experimental Usage**

Firstly, we used Python **pdf2image** library to convert .pdf into images. The pdf2image method `convert_from_path` takes in a path where the file is located and returns a PIL Image object representing an image of the page of this file.

```python
from pdf2image import convert_from_path
pdf_filename = "paper.pdf"
images = convert_from_path(pdf_filename)
```

These images need to be saved into a directory. First, the directory is emptied to remove any previous images, then the new images are saved as PNGs. The filename of each image is just a number, e.g. 3.png, which corresponds to the page number.
```python
import os

# Empty the image directory before storing new PDF images
for f in os.listdir("pdf_images"):
    os.remove(os.path.join("pdf_images", f))

# Store each image
for i, img in enumerate(images):
    # Save pages as images in the pdf
    img.save(f"pdf_images/{i}.png", 'PNG')
```

The next stage is to apply the OCR to extract the text from each image. For this process we use a Python library called **pytesseract**  on each image. We iterate through each image in the directory and use the `image_to_string()` method which returns the content for that particular page. The content of all pages is concatenated together.
```python
import pytesseract

content = ""

for img_filename in os.listdir("pdf_images"):
    content += pytesseract.image_to_string(f"pdf_images/{img_filename}")
```

**OCR Summary**

Applying OCR to each image is very slow. Some pages can be processed in less than 10s while others take a few minutes.

Pros:
* can be used on scanned images of research papers

Cons:
* on average very slow
* not accurate as Tika, ignores mathematical formulas
* parses text in text blobs, which is then difficult to preprocess

### PDF-to-Doc-to-text method
Another method involves using **libreoffice** to firstly convert .pdf to .docx file and then use Python library called **python-docx** to read from docx file.

**Experimental Usage**
We used libreoffice command for converting doc to docx:
`unconv -d document --format=docx filename.doc`

When trying to read from the doc with python-docx library we discovered that reading text from docx divides the text to small portions, text blobs. The problem is formatting. Libreoffice tries to keep the original formatting. Although keeping the formatting can give some insightful information for example the headings, it is very difficult and inefficient to read and analyse.
We discarded this method due to this issue.

### Poppler
The last method we explored was using **Poppler**. Poppler provides a linux command that can extract text from pdf files and output them to standard output. Once we tested poppler on several documents, we saw great potential in this particular tool, as it was reliable and fast. The only downside was that it is available for linux only.

**Experimental & Final Usage**

We used `subprocess.Popen` to execute the command and read the output.

```python
def pdf2text(path:str):
    proc=subprocess.Popen(["pdftotext","-nopgbrk","-raw",path,"/dev/stdout"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result=proc.communicate()
    if result[1]:
        raise Exception(result[1])
    else:
        return result[0].decode("utf-8")
```
**Summary**

Pros of poppler:
* Fast and reliable, yields satisfactory results in most cases
* Parses text well including whitespaces
* Includes mathematical formulas

Cons of poppler:
* Uses Linux command

### Final Choice
The fastest and most reliable tools we considered were Tika and Poppler.
As Tika required connection to the server OR being packaged into a seperate container it was more difficult for us to use it in the project. That is why we decided that **Poppler** will be our default method of extracting text from .pdf files. To ensure that it will work on any OS, it was packaged inside Docker container running Ubuntu OS.
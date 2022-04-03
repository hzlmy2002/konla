---
title: "Week 6"
linkTitle: "Week 6"
date: 2021-11-22
description: >
  **(22.11.2021 - 28.11.2021)**


  We are still looking for the final library for pdf to text conversion. We also further specify our system requirements.
---


### 23 Nov
* Minyi got the Tika to run locally by packing it into a Docker image. We are still discussing the text extraction library we'll use.
* Suraj checked the Allen Institute website for PDF to HTML conversion. [PaperToHtml](https://papertohtml.org/paper?id=e50f7020327f8a1ed61f3a4f76ab3c2b7cc394f2) is very powerful and can display headings, paragraphs as well as find the abstract and references. The downside is the time that it takes to do so (around 2-3mins) plus additional limits such as file size and possibly website traffic.
* To make it easier to post on the blog, Minyi plans to make it generated using [hexo](https://hexo.io/) framework.

### 24 Nov
* Bart created an interactive Google Jamboard for the team to create together a MoSCoW requirement list

### 27 Nov
* Suraj found an alternative method for extracting text from .pdf files. It requires that the .pdf is firstly converted into .png format and then Optical Image Recognition (OCR) is used. Unfortunately, this method is significantly slower than others and does not handle mathematical formulas very well. [More info](#pdf-extraction-using-ocr)

### 28 Nov
The new markdown-generated hexo blog is up and running thanks to Harry. The theme should be changed from default, so we will discuss which one to choose during nexy meeting. Available themes are shown [here](https://hexo.io/themes/).

### PDF extraction using OCR
Another approach to extracting text from a research paper would be to convert it into separate images for each page and apply a process known as OCR which stands for Optical Character Recognition. This step looks for characters in the image and generates the content of the paper. If a user wants to analyse a paper from many years ago, they may not have a PDF file but instead a scanned copy of the pages. OCR can be applied to the images allowing the text to be extracted.

If the uploaded file is a PDF, then each page needs to be converted into an image. We have installed [Poppler Utils](https://poppler.freedesktop.org/) which is a set of tools to handle PDFs. A Python library, pdf2image, uses the tools to convert a PDF into images. It returns a list of PIL Image objects representing a page from the PDF file.
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

The next stage is to apply the OCR process for which we are using the Python library pytesseract to extract the text on each image. We iterate through each image in the directory and use the `image_to_string()` method which returns the content for that particular page. The content of all pages is concatenated together.
```python
import pytesseract

content = ""

for img_filename in os.listdir("pdf_images"):
    content += pytesseract.image_to_string(f"pdf_images/{img_filename}")
```

Applying OCR to each image is very slow. Some pages can be processed in less than 10s while others take a few minutes. We will mainly use this process with scanned images where there is no PDF version of the original paper.

### MoSCoW Requirement List
This is the 1st version of MoSCoW requirements list. Upon mutual agreement between team members and our client the requirements list can be changed.
![](/2021/group6/images/MOSCOW.jpg)
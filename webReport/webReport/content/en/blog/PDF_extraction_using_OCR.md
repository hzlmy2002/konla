---
title: "PDF extraction using OCR"
linkTitle: "PDF extraction using OCR"
date: 2021-11-18
decription: >
---
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

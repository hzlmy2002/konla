"""
PDF text extracter using OCR (Optical Character Recognition)
Referenceds:
PDF to images: https://stdworkflow.com/272/say-goodbye-to-copy-paste-python-implements-pdf-to-text
Pytesseract OCR: https://nanonets.com/blog/ocr-with-tesseract/

Convert each page of a PDF to a PNG. Then use OCR to convert to text
"""
from pdf2image import convert_from_path
import pytesseract
import os

try:
    from tqdm import tqdm
except ImportError:
    pass

def save_images(images_obj, IMAGES_DIR):
    pass

def getReferences(content):
    print("### References ###")
    ref_section_index = content.lower().find("references")
    if ref_section_index != -1:
        print(content[ref_section_index:])


def saveContent(content):
    # Open in WB to write UTF8 encoded text
    with open("pdf_text_output.txt", "wb") as file:
        content_split = content.split("\n")
        for line in content_split:
            # Check line has content
            if len(line) > 0:
                try:
                    encoded_line = (line + "\n").encode("utf8")
                    file.write(encoded_line)
                except Exception:
                    pass


def displayMetaData(metadata):
    print("### METADATA ###")
    for meta in metadata:
        print(f"{meta}\t{metadata[meta]}")


paper_filename = "../shapes.pdf"

# Converts to PDF images
images = convert_from_path(paper_filename)
for i, img in enumerate(images):
    img_filename = 'page' + str(i) +'.png'

    # Save pages as images in the pdf
    img.save(img_filename, 'PNG')

saveContent(content)

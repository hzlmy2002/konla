""" PDF text extracter using pdgtotext """
import pdftotext
import os


def save_content(content):
    # Open in WB to write UTF8 encoded text
    with open("pdf_text_output.txt", "wb") as file:
        content_split = content.split("\n")
        for line in content_split:
            # Check line has content
            if len(line) > 0:
                try:
                    encoded_line = (line + "\n").encode("utf8")
                    file.write(encoded_line)
                except Exception as e:
                    pass


paper_filename = "../../shapes.pdf"

with open(paper_filename, "rb") as f:
    pdf = pdftotext.PDF(f)

content = "\n".join(pdf)

save_content(content)

---
title: "Week 5"
linkTitle: "Week 5"
date: 2021-11-16
description: >
  **(16.11.2021 - 21.11.2021)**


  This week we are researching libraries that will be used for the project, in particular methods for PDF to text extraction.
---

### 16 Nov
Suraj tested some of python PDF libraries. He tried PyPDF2, but it read most of the papers quite poorly.
However, he also found a different Java-based server with Apache called tika. **[Tika](https://tika.apache.org/)** is surprisingly good for text extraction and can work with different file formats as well. Although, the choice of the tool is to be discussed, Tika is a strong candidate for the task. Further insights, [here](#pdf-extraction-using-tika)

### 23 Nov
Our project partner suggested looking at the [**Poppler utilities**](https://poppler.freedesktop.org/).They include a linux command line program - pdftotext - that extracts the text, and there seems to be a Python version [poppler-utils](https://pypi.org/project/poppler-utils/). We should now compare the results of pdf parsing by Poppler to Tika. Poppler has a slight advantage as it doesn't need Java server to work.

### 6 Dec
We shared our main GitHub repository with Lacibus.

### PDF-Extraction using Tika
Our application begins by extracting text from an uploaded PDF. Text is difficult to extract from a PDF as it isn't stored in a standard encoding format, such as Unicode, but as text elements that are drawn at certain positions in the page, which is affected by the page layout. However, there are tools within Python libraries that make the process easy, but not necessarily perfectly accurate.

One such tool is Tika which is written in Java. It can extract content from various file types and use its automatic document type detection to fetch the corresponding parser if a PDF file is given. The Python library connects to the external Java program which then communicates with an Apache server where the PDF is processed. This means Java Runtime needs to be installed on the machine.

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

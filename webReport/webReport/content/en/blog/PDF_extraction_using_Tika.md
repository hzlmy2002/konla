---
title: "PDF extraction using Tika"
linkTitle: "PDF extraction using Tika"
date: 2021-11-15
description: >
---
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

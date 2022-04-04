---
title: "Paper Processor (NLP features)"
linkTitle: "Paper Processor (NLP features)"
weight: 4
date: 2022-4-01
description: >
  Implementation of the Paper Processor
---
Paper processor is the abstracted object which represents the paper contents. It also abstracted the methods that analyze the paper contents by using NLP techniques.
It supports the following features:

- Object constructor(Text extraction, metadata reading, text tokenize, nlp model loading)
- Whole summarisation
- Partial summarisation
- Calculate word frequency
- References extraction
- Calculate metrics

### Object Constructor
The code for the object constructor is as follows:
```python
def __init__(self,path:str) -> None:
      text = self.preprocessText(PDFHelper.pdf2text(path))
      self.metadata = PDFHelper.getMetaData(path)
      self.nlpTRF = spacy.load("en_core_web_trf")
      self.doc = self.nlpTRF(text)
```
The text extraction and most of the metadata reading is done by the PDFHelper class, which we will describe in the later post. The nlp model loading is done by the spacy library, and the model tokeinizes the text.
The author field is extracted from the text by using the name entity feature provided by the nlp model. We will read the first several consecutive person name entities in the text, and that's the authors of the paper.

### Whole summarisation
DONE BY BART.

### Partial summarisation
DONE BY BART.

### Calculate word frequency
Before calculating the word frequency, some meanless words(e.g. punctuation, space) are removed. If the lemma feature is enabled in the nlp model, we can use the lemma of the word instead of the word itself. If the ignorecase feature is enabled in the nlp model, we will convert all of them into lower case. If both are enabled, we will use the lemma.

Then the word will be added to a list, and we will use Counter object to count their occurrence. The first 100 words will be reserved and returned as result.

### References extraction
We will first use the Matcher feature provided by spaCy, which is like a enhanced version of the regular expression. This will crop the region of all the references.

We will then split them into lines, and check the sequences number of each references. In this way, we can further divide the references region into references.

### Calculate metrics
We first count the total word number, and divide them by the reading speaking speed.
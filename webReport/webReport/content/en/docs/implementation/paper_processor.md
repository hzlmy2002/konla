---
title: "Paper Processor (NLP features)"
linkTitle: "Paper Processor (NLP features)"
weight: 4
date: 2022-4-01
description: >
  Implementation of the Paper Processor
---
PaperProcessor directory contains all the code associated with processing and analysis of texts. The PaperProcessor.py file includes a PaperProcessor object class which is used for managing all of the other files in the directory. The PaperProcessor object is created during execution of mainThread in startView.py, in other words after the file is uploaded and the analysis starts.

```
./PaperProcessor/
├─ PDFHelper
│  ├─ PDFHelper.py
|  └─ __init__.py
│
├─ PaperProcessor.py
├─ __init__.py
├─ authors.py
├─ refs.py
├─ sections.py
├─ summary.py
└─ wordFrequency.py

```
Paper processor is the abstracted object which represents the paper contents. It also abstracts the methods that analyze the paper contents by using NLP techniques.
It supports the following features:

- Object construction (Text extraction, metadata reading, text tokenization, model loading)
- Whole summarisation
- Partial summarisation
- Section and subsection region extraction (not a standalone feature, but used in partial summarisation)
- Calculate word frequency for keyword extraction
- References extraction
- Compute text metrics

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
The author field is extracted from the text by using the name entity feature provided by the spacy model. We will read the first several consecutive person name entities in the text, and that's the authors of the paper.

The methods of the PaperProcessor reflect the backend API and are used to return corresponding results. The next subsections describe each of the features in more detail.

### Whole summarisation
Whole Paper Summarization is done with the use of Summarizer object in **summary.py**. 

It performs extractive summarization on spacy `doc` (preprocessed text). Firstly, the relative frequency of words in the document is computed. Whitespaces, numbers, stopwords and punctuation marks are ignored. Next, each sentence is given a score which is the sum of relative frequencies of its words. The function returns top `WHOLE_SUMMARY_LENGTH` sentences, where `WHOLE_SUMMARY_LENGTH` is the class attribute of Summarizer and defaults to `10`.

**Note**: More info on why this specific method was used can be found in Research Section

### Section and subsection region extraction
Although section extraction is not a feature that can be directly called from an API, it is used by other features such as partial summarization. By section extraction we mean extracting the titles of sections and subsections of the documents and the text regions under that particular headings.

Section Extraction can work efficiently under the following assumptions:
*	section and subsection titles are clearly separated from main paragraph text
*	section and subsection titles are within a single line
*	section and subsection titles follow standard numerical ordering: 1, 1.1, 1.2, … etc. or 1., 1.1., 1.2., … etc.
*	section and subsection titles follow writing standards, i.e. they are either capitalised or uppercase (stopwords can be lowercase)

Section Extraction is performed in `sections.py` in a following order:
1.	Spacy `Matcher` object uses several patterns to distinguish section and subsection titles (the patterns are based on assumptions above)
2.	A round of checking of matches is performed, letter case is taken into account and possible reference section is excluded as there is no point in summarising references
3.	Multiple patterns can match to same or overlapping text regions. Therefore, another stage is the removal of duplicates and overlap between matches. If there is an overlap between two matches, the one that starts earlier is used, and the second one is discarded. If two matches start at the same position, longest match is used, shorter is discarded.
4.	By iterating over a list with section titles, start tokens and end tokens, section range is computed for each of the section and subsection match. Furthermore, if a section contains several subsections, its range is computed with regards to the next section, i.e. it includes the text range from each of its subsections. For example, section “2” incudes the combined text range of “2.1”, “2.2”, “2.3”, … up to the start of section “3”. The last section is cut off at reference start if reference match was found, otherwise it continues till the end of the text.


### Partial summarisation
Partial Summarization is performed similarly to whole paper summarization, but the calculation of sentence scores and extraction of sentences is performed for each section separately. Another difference is that it returns an ordered dictionary, where the keys are the section and subsection titles and values are summarised contents of their text regions. Each region summary is made up of `SEGMENT_SUMMARY_LENGTH` sentences, where `SEGMENT_SUMMARY_LENGTH` is the class attribute of Summarizer and defaults to `10`.

### Calculate word frequency
Before calculating the word frequency, some meaningless words (e.g. punctuation, space) are removed. If the `lemma` option is enabled in the nlp model, we can use the lemma of the word instead of the word itself. If the `ignorecase` option is enabled in the nlp model, we will convert all of them into lower case. If both are enabled, the result is the same if only `lemma` option is chosen as lemma by default lemmatizes words to lowercase base words.

Then the word will be added to a list, and we will use Counter object to count their occurrence. The first `100` words will be reserved and returned as result.

### References extraction
We first use the Matcher feature provided by spaCy, which is like a enhanced version of the regular expression. This crops the region of all the references.

We then split them into lines, and check the sequences number of each references. In this way, we can further divide the references region into references.

### Computation of text metrics
We first count the total word number, and divide them by the reading and speaking speed.

**Reading Speed**

We assumed an average rate for conversational speech which is about 140 words per minute, according to Tools for Clear Speech between 110-150wpm [1].

**Speaking Speed**

We assumed an average rate of reading time of 238wpm for researchers according to the study by Marc Brysbaert from Ghent University in Belgium whose work calculated an average reading speed based on 190 of research studies conducted between 1901 and 2019, collectively involving 17,887 participants [2]. 


**References**

[1] Speaking Rate [Internet]. [cited 2022 Mar 27]. Available from: https://tfcs.baruch.cuny.edu/speaking-rate/

[2] Most Comprehensive Review To Date Finds The Average Person’s Reading Speed Is Slower Than Previously Thought – Research Digest [Internet]. [cited 2022 Mar 27]. Available from: https://digest.bps.org.uk/2019/06/13/most-comprehensive-review-to-date-suggests-the-average-persons-reading-speed-is-slower-than-commonly-thought/


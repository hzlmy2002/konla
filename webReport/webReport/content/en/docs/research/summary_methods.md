---
title: "Text Summarization Methods"
linkTitle: "Text Summarization Methods"
weight: 4
date: 2022-4-01
description: >
  There are many ways to approach text summarization, but only few could work well in our setting. This section explores the most popular methods of text summarization and explains our design choices for this task.
---

### Text Summarization Background
One of our key system requirements was to develop whole and partial (segment) summarisation features. Summarization is a difficult task in general, but in our system setting it had to face several additional problems including:
* **specialist language**: research papers often use more sophisticated language and vocabulary; some words will not be included in the language model
* **versatility of the topics**: our system is supposed to work for any research paper and that means dealing with different domain of studies
* **pdf plain text analysis**: the input to NLP tasks is not perfect as it was gained through pdf-to-text conversion; some noise is unavoidable and it may be visible in the final analysis result
* **limited computing resources**: some text summarisation methods require a lot of computing power, it is important that we try to use less heavy-duty methods to make the development easier and generally increase service responsivess. We don't want our users to wait too long for the result.

### Classification of Text Summarization Methods
*Classification based on Research Paper "Using K-Means and Variable Neighborhood Search for Automatic Summarization of Scientific Articles" by Akhmetov, Iskander & Mladenovic, Nenad & Mussabayev, Rustam. (2021)*

[1] We can classify text summarization methods based on:
###### Input
* single-document: single document is used
* multi-document: multiple documents are used in input

###### Output
* extractive: extracts the most relevant sentences based on some form of sentence scoring. The sentences are in their original form, hence the output may lack smoothness.
* abstractive: generates new text based on input, it uses Natural Language Generative (NLG) models

###### Content
* Informative: the text captures the all the necessary information from the text, so that there is no need to read the whole text
* Indicative: the summary shows a 'teaser' of the text that can either motivate or discourage a person to read it

In our setting, we are looking for **single-document informative** summarisation method. We experimented with both extractive and abstractive summarisation methods and in the next section we'll describe these in more detail.

### Extractive Summarization Methods

#### Bag of Words (BoW) Summarisation
```python
from collections import OrderedDict

def summary_extractive(self, doc, n=5):
    """
    Extracts n best scoring sentences based on the sum of relative frequencies
    of keywords appearing in each sentence.
    Parameters:
    doc (spacy doc object): Spacy doc object containing tokenised text
    n (int): Number of sentences to extract
    Returns:
    str: Concatanated n best scoring sentences in order
    """
    # STEP 1. Frequency Table
    keywords = dict()
    num_tks = 0
    for tk in doc: 
        if not any([tk.is_space, tk.like_num, tk.is_stop, tk.is_punct, tk.is_digit, tk.text in ['\\n', '\n', '.']]):
            num_tks += 1
            tk = tk.lower_
            if tk in keywords.keys():
                keywords[tk] += 1
            else:
                keywords[tk] = 1
    # STEP 2: Change dictionary values to relative frequency
    for key, value in keywords.items():
        keywords[key] = value / num_tks
    # STEP 3: Score sentences based on the keywords and their relative frequency
    sentences = []
    for sent in doc.sents:
        sent_score = 0
        for tk in sent:
            tk = tk.lower_
            if tk in keywords.keys():
                sent_score += keywords[tk]
        sentences.append((sent_score, sent))
    # STEP 4: get n sentences with highest scores
    sentences.sort(key=lambda item: item[0], reverse=True)
    best_sents = [item[1].text for item in sentences[:n]]
    return " ".join(best_sents)
```

**Note:** Similar output can be acquired by using **scikit-learn (sklearn)** CountVectorizer, but it requires preprocessing and inputting text as `str`
```python
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
# potential argument min_df (minimal document frequency)
# max_df to specify maximum document frequency
# can be absolute value or proportion of documents, popular 0.85
count_vector = vectorizer.fit_transform(sentences) 
vector.to_array() 
# returns an array of vectors representing each sentence 
# in terms of the number of occurences of words in them
```
This method is fast and produces average summary results.

#### TF-IDF
**TF-IDF (Term Frequency-Inverse Document Frequency)** is often used by search engines for scoring and ranking websites according to user queries.

Term Frequency `tf(f,d)` is the relative frequency of term `t` within document `d` (although there are other ways to define it: boolean frequency, term frequency adjusted for document length, logarithmically scaled frequency and others)

`tf(t, d) = f(t,d) / sum`
(to handle possible ZeroDivisionError, we often add `1` to the sum)

Inverse Document Frequency `idf(t,D)` is a measure of how much information the word provides, i.e. if it is common or rare across all documents. It is logarithmically scaled inverse fraction of the documents that contains the word (obtained by dividing the total number of documents by the number of documents containing the term and then taking logarithm of that quotient) [2].

`idf(t, D) = log(N, |{d in D such that t in d}|)`

To use it for single-document summarization we treat sentences as documents and individual tokens as terms.

Pros: 
* easy and computationally cheap

Cons: 
* does not take context into account
* can suffer from the 'curse of dimensionality', i.e. with growing number of dimensions, the available data becomes sparse and often unreliable [3].

#### TextRank / PyTextRank
[TextRank](https://spacy.io/universe/project/spacy-pytextrank) is a graph-based algorithm for extractive and unsupervised text summarisation. Vector representation is computed for each sentence.
After that similarities between the sentences are calculated and stored in a matrix which is later converted into a graph. The graph consists of sentences as vertices and similarity scores (from 0 to 1) as edges to rank the sentences. The final summary is formed by concatenation of `n` top ranked sentences.
```python
import spacy
import pytextrank
from icecream import ic  # we used ic for printing and debugging purposes
# Loading and adding text rank to pipeline
nlp_with_textrank = spacy.load("en_core_web_trf")
nlp_with_textrank.add_pipe("textrank")
doc = nlp_with_textrank(text)
# Creating summary
tr = doc._.textrank
summary = ""
for sent in tr.summary(limit_phrases=100, limit_sentences=10):
    summary += ic(sent).text
print(summary)
```
Again, we are operating on matrices, so the larger the text, the more resources we will need to calculate the similarity matrix and create a corresponding graph.

##  Feature Based Extractive Summarization Methods
Feature Based Summarisation methods aim to extract sentences based on different features. There are different algorithms that take various features into account. Below are 2 examples. 

#### PyTeaser Library
Each sentences is ranked by using four criteria:
1. relevance to the title
2. relevance to keywords in this article
3. position of the sentence
4. length of the sentence

Pros:
- takes into account different criteria than in previously described algorithms

Cons:
- needs title as parameter, difficult to extract from pure text from .pdf with high accuracy
- produces 5 sentences at most

#### Luhn's Algorithm [4] (using sumy library)
* Selects sentences based on word and phrase frequency, and their position (earlier=higher)

Pros:
* Useful for technical document and article summaries
* Good when frequent words are present
* Easy to set up using `sumy` library in python (but it's an additional dependency)

Cons:
* Requires text preprocessing, namely removal of stopwords and stemming (easy)
* Low accuracy

```python
# Example use of Luhn's Algorithm with sumy and nltk library
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
import nltk
nltk.download() # all
parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LuhnSummarizer()
summary = summarizer(parser.document, number_of_sentences=5)
```

## Abstractive Summarisation Methods

Abstractive Summarisation Methods are mostly based on generative models, models that generate new text by paraphrasing original one. We used [huggingface](https://huggingface.co/) platform for testing different generative models. 

In the code below we attempted using **HuggingFace** models for summarisation. 

This is a difficult task as the models have an upper limit of tokens (usually 1024) from which a single summary can be generated. This means that for longer texts the text has to be split in chunks of max 1024 tokens. Then summaries are generated for each of the chunks. We can then concatenate the resulting summaries to create one or repeat the process until we receive a summary of desired length. 
The advantage of this approach is that the contents of the chunk are well paraphrased and create a smooth text, but at the same time only the content of the chunk is being taken into account and not the whole text.
For research papers that are usually much larger than 1024 tokens, using pure abstractive summarisation will not yield best results. Furthermore, it will be highly inefficient in terms of speed. Combination of extractive and abstractive summarisation can improve speed slightly, but the result will still be dependent on the size of the chunks and their positioning, for example summarising chunk within one topic/section will yield better results than a chunk that includes two different sections of the paper. There is yet another issue that can emerge. Generating summaries from too small chunks can result in words or sentences being repeated until the desired summary length is obtained creating an unusable partial summary.

```python
# transformers is a Hugging Face package with pretrained models for NLP tasks
from transformers import pipeline 
# in keyword parameter mode we can type string code for any available pretrained model
# including 'gpt-2', 't5' and many others.
summarizer = pipeline("summarization", mode="<here_input_model_name>")
"""
Define a function that takes in a text of given length n, a model and a ratio, 
and generates a summary using given model such that the ratio 
of length of the summary to the length of original text
is approximately `ratio` or lower
"""
MAX_CHUNK_SIZE = 1000 # in tokens, the max is 1024, but we want to keep a buffer
MIN_SUMMARY_SIZE = 20
SUMMARY_DEVIATION = 20

class SummaryGenerator:
    
    def __init__(self):
        self.chunk_size = MAX_CHUNK_SIZE
        
    def generate_summary(self, doc, ratio: float):
        if ratio > 1 or ratio < 0:
            raise ValueError("ratio parameter should be between 0 and 1")
        chunks = self.chunkify(doc)
        for chunk in chunks:
            s = len(chunk.split(" "))
            print(f"{s} - {chunk}")
        max_length = int(self.chunk_size*ratio + SUMMARY_DEVIATION) # 120
        min_length = int(self.chunk_size*ratio - SUMMARY_DEVIATION) # 20
        # main chunks
        summaries = summarizer(chunks[:-1], max_length=max_length, min_length=min_length, do_sample=False)
        new_string = "".join([item["summary_text"] for item in summaries])
        # last chunk is usually smaller and thus ignored in this example
        return new_string
        
    def chunkify(self, doc):
        """Splits the doc into chunks of size less or equal to max_chunk 
        keeping content of each sentence within same chunk"""
        max_chunk = 500
        current_chunk = 0
        current_chunk_length = 0
        chunks = []
        for sent in doc.sents:
            if len(chunks) == current_chunk + 1:
                l = len(sent)
                if current_chunk_length + l <= max_chunk:
                    chunks[current_chunk] += sent.text
                    current_chunk_length += l
                else: # exceeded limit, move to next chunk
                    current_chunk += 1
                    chunks.append(sent.text)
                    current_chunk_length = l
            else: # first chunk appended
                chunks.append(sent.text)
                current_chunk_length = len(sent)
        return chunks
    
sg = SummaryGenerator()
summary = sg.generate_summary(doc, ratio=0.2)
# Possible Warning: Your max_length is set to 220.0, but your 
# input_length is only 19. You might consider decreasing max_length manually, 
# e.g. summarizer('...', max_length=9)
```

### Mixed Approach
In some situations summarisation that combines both extractive and abstractive techniques is recommended. We can either start by extracting the most important sentences, combining them and generating a summary based on them or we can generate a summary of the whole text and extract the most important sentences from this summary. Either way, because we are using heavy generative models this process is still very slow and requires much more computing power than we have available.

## Evaluation and Choice of Summarisation Method
The evaluation of summarisation methods is a difficult task. There are several statistical metrics that are commonly used to measure the accuracy of the summaries. Most of them are reference-based, meaning that they compare the produced summary with a reference summary created by human. One of such metric is called ROUGE. It calculates the similarity between the summary and reference by comparing the number of repeating n-grams in both text. This metric unfortunately has a bias towards extractive methods because if the right sentences are extracted they have exact same phrases as the original text.

Due to performance issues and time constraints, we decided to incorporate the basic extractive summarisation method based on relative keyword frequency scoring for our whole and partial summarisation features.


### References
[1] Akhmetov, Iskander & Mladenovic, Nenad & Mussabayev, Rustam. (2021). Using K-Means and Variable Neighborhood Search for Automatic Summarization of Scientific Articles

[2] tf–idf. Wikipedia [Internet]. 2022 [cited 2022 Mar 27]. Available from: https://en.wikipedia.org/w/index.php?title=Tf%E2%80%93idf&oldid=1071253989

[3] Curse of dimensionality. In: Wikipedia [Internet]. 2022 [cited 2022 Mar 28]. Available from: https://en.wikipedia.org/w/index.php?title=Curse_of_dimensionality&oldid=1069844794

[4] Luhn’s Heuristic Method for text summarization [Internet]. OpenGenus IQ: Computing Expertise & Legacy. 2019 [cited 2022 Apr 3]. Available from: https://iq.opengenus.org/luhns-heuristic-method-for-text-summarization/
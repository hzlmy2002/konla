---
title: "Choice of NLP libraries"
linkTitle: "Choice of NLP Libraries"
weight: 2
date: 2022-4-01
description: >
  In this section we compare Python NLP libraries and explain our final choice.
---

To implement the features of the system it is important to use an appropriate NLP library.
There are several Python NLP libraries available, yet not every library fits well to our deliverable idea. This section shows the research we did on available NLP libraries and discusses the differences between them to explain the final choice.

### Natural Language ToolKit (NLTK)

**Description**

**NLTK** is one of the most popular and powerful NLP libraries available open source. It contains text processing libraries for tokenization, parsing, classification, stemming, tagging and semantic reasoning [1]. It gives the user the greatest choice of algorithms used for different tasks as well as supports many 3rd party libraries. It is mostly use in education and research. One of the most important drawbacks of NLTK is the fact that it is slow, hence it is not the best choice for production. Also, its models have no integrated word vectors.

**Summary**

Pros:
* the greatest range of algorithms, and approaches for NLP methods
* many 3rd party extensions

Cons:
* quite slow compared to other libraries
* nltk sentencizer splits text by sentences without analysis of semantic structure
* no integrated word vectors

### Gensim

**Gensim** is another Python NLP library. It is designed primarily to process raw, unstructure texts using unsupervised machine learning algorithms [2]. Gensim offers limited number of algorithms, but it gives great performance in return. Gensim's tools often are not enough to handle all NLP tasks in production, so it is usually combined with NLTK pipeline.

Pros:
* great performance
* handles large datasets and processes data streams

Cons:
* has very limited choice of algorithms and functions
* it is not enough to provide full NLP pipeline

### SpaCy
**SpaCy** is a relatively new Python NLP library. Similarly to NLTK it provides full NLP pipeline with many additional features. Unlike NLTK, it's state-of-the-art solution which chooses the best possible algorithm for given task for the user, limiting the flexibility of use [3]. It is very popular in production as it is the fastest NLP framework available and it follows good Python OOP programming practices. It is easy to use and has great documentation for developers.

**Summary**

Pros:
* fastest NLP framework
* easy to use and with good documentation
* in-built language models with word vectors

Cons:
* offers less flexibility, chooses best algorithms for the user


### Other Libraries
Other libraries such as TextBlog, CoreNLP, Polyglot or Pattern offer less features and are generally slower. Therefore, we did not include them in this comparison.

### Final Choice

Our final choice was **spaCy** due to its performance and adaptability to producing software rather than doing research. It contains all the necessary tools in a single dependency and with a single language model it is able to perform a vast range of analysis task. For the system it may be complemented with **sklearn** methods for better results.

Note: It's important to mention that all of these libraries were taken into account at development stage when programming system features. In the end, the most important factor was the performance of the system, so our team tried to minimise required dependencies and maximise the speed, thereby choosing spaCy implementations.

### References

[1] Comparison of Top 6 Python NLP Libraries [Internet]. KDnuggets. [cited 2022 Apr 5]. Available from: https://www.kdnuggets.com/comparison-of-top-6-python-nlp-libraries.html/

[2] Gensim: topic modelling for humans [Internet]. [cited 2022 Apr 5]. Available from: https://radimrehurek.com/gensim/intro.html

[3] 8 best Python NLP libraries [Internet]. Sunscrapers. 2018 [cited 2022 Apr 5]. Available from: https://sunscrapers.com/blog/8-best-python-natural-language-processing-nlp

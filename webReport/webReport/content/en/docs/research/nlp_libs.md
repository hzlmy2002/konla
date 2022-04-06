---
title: "Choice of NLP libraries"
linkTitle: "Choice of NLP Libraries"
weight: 2
date: 2022-4-01
description: >
  In this section, we compare Python NLP libraries and explain our final choice.
---

To implement the features of the system it is important to use an appropriate NLP library.
There are several Python NLP libraries available, yet not every library fits well to our deliverable idea. This section shows the research we did on available NLP libraries and discusses the differences between them to explain the final choice.

### Natural Language ToolKit (NLTK)

**Description**

**NLTK** is one of the most popular and powerful NLP libraries that is open-source. It contains text processing libraries for tokenisation, parsing, classification, stemming, tagging and semantic reasoning [1]. It gives users the greatest choice of algorithms used for different tasks, as well as supports many 3rd party libraries. It is mostly used in education and research. One of the most important drawbacks of NLTK is the fact that it is slow, hence it is not the best choice for production. Also, its models have no integrated word vectors.

**Summary**

Pros:
* The greatest range of algorithms, and approaches for NLP methods
* Many 3rd party extensions

Cons:
* Quite slow compared to other libraries
* NLTK sentencizer splits text by sentences without analysis of the semantic structure
* No integrated word vectors

### Gensim

**Gensim** is another Python NLP library. It is designed primarily to process raw, unstructured texts using unsupervised machine learning algorithms [2]. Gensim offers a limited number of algorithms, but it has great performance in return. Gensim's tools often are not enough to handle all NLP tasks in production, so it is usually combined with an NLTK pipeline.

Pros:
* Great performance
* Handles large datasets and processes data streams

Cons:
* Has very limited choice of algorithms and functions
* It is not enough to provide a full NLP pipeline

### SpaCy
**SpaCy** is a relatively new Python NLP library. Similarly to NLTK, it provides a full NLP pipeline with many additional features. Unlike NLTK, its state-of-the-art solution chooses the best possible algorithm for a given task, limiting the flexibility of use [3]. It is very popular in production as it is the fastest NLP framework available and it follows good Python OOP programming practices. It is easy to use and has great documentation for developers.

**Summary**

Pros:
* Fastest NLP framework
* Easy to use and with good documentation
* In-built language models with word vectors

Cons:
* Offers less flexibility, chooses best algorithms for the user

### Other Libraries
Other libraries such as TextBlog, CoreNLP, Polyglot or Pattern offer fewer features and are generally slower. Therefore, we did not include them in this comparison.

### Final Choice

Our final choice was **spaCy** due to its performance and adaptability to producing software rather than doing research. It contains all the necessary tools in a single dependency and, with a single language model, it is able to perform a vast range of analysis tasks. spaCy can be complemented with **sklearn** methods for better results.

*Note: It's important to mention that all of these libraries were taken into account at development stage when programming system features. In the end, the most important factor was the performance of the system, so our team tried to minimise required dependencies and maximise the speed, thereby choosing spaCy implementations.*

### References

[1] Comparison of Top 6 Python NLP Libraries [Internet]. KDnuggets. [cited 2022 Apr 5]. Available from: https://www.kdnuggets.com/comparison-of-top-6-python-nlp-libraries.html/

[2] Gensim: topic modelling for humans [Internet]. [cited 2022 Apr 5]. Available from: https://radimrehurek.com/gensim/intro.html

[3] 8 best Python NLP libraries [Internet]. Sunscrapers. 2018 [cited 2022 Apr 5]. Available from: https://sunscrapers.com/blog/8-best-python-natural-language-processing-nlp

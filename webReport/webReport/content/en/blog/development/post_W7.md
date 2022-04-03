---
title: "Week 7"
linkTitle: "Week 7"
date: 2021-11-29
description: >
  **(29.11.2021 - 05.12.2021)**


  This week our aim is to get the pdf-to-text extraction working, set up the project repo and work to finalise project requirements.
---

### 29 Nov, Group Meeting
* Reviewed the MoSCoW list, slight change to original, [see more](#new-moscow-list)
* Established tasks for this week

### 30 Nov
Minyi found yet another method for pdf-to-text extraction. First, use [**libreoffice**](https://www.libreoffice.org/) to convert pdf to doc and then use [**python-docx**](https://python-docx.readthedocs.io/en/latest/) library to read from docx file. This is a sophisticated way, so we may need to revisit the earlier ideas. Libreoffice cmd for converting doc do docx is:

`unoconv -d document --format=docx filename.doc`

This method was later discarded. [View Update](#5-dec)


### 1 Dec
We created a GitHub repository for the project. For now, it will contain all of our experiments.

### 5 Dec
Unfortunately, we later found out that reading the text from docx is recognised and divided to small portions, text blobs. The poblem with libreoffice is formatting. Libreoffice tries to keep the original formatting. Keeping the formatting is difficult to handle (read) during analysis, but at the same time it can give useful information, such as the headings. Generally, using this method makes analysis of text and sentences significantly harder and less efficient. We will discard this method and revisit Poppler and Tika. Maybe combining these two will yield better results.

### New MoSCoW List
![](/2021/group6/images/MOSCOW2.png)

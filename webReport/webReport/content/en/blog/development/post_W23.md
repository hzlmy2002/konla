---
title: "Week 23"
linkTitle: "Week 23"
date: 2022-03-21
description: >
  **(21.03.2022 - 27.03.2022)**


  This week we are focusing on integration between frontend and the backend and fixing some issues, so that the system will be ready for deployment.
---

### 21 Mar
* whole and partial summarization, basic extractive methods
* code cleaning

### 22 Mar
* More options for viewing components in frontend

### 23 Mar
* Used flake8 to remove violations
* Added summarization to api
* Implemented to frontend

### 24 Mar
* Documentation writing
* User Manual
* Deployment Guide

### 24 Mar
* Suraj has finished the analysis features display in frontend. [See here](#analysis-features-content)

### 27 Mar
* This is the end of Term 2.

### Analysis Features Content
Each analysis feature has a different way of representing its content, so we will showcase how each one displays the data. The images use placeholder text, such as [Lorem Ipsum](https://www.lipsum.com/), in places where the actual analysis content would be placed.

![Whole Summary](/2021/group6/images/analysis_features/whole_summary.png "Whole Summary")
The whole summary is just a single block of text.

![Partial Summary](/2021/group6/images/analysis_features/partial_summary.png "Partial Summary")
The partial summary is divided into each section's summary.

![Keyword Extraction](/2021/group6/images/analysis_features/keywords_extraction.png "Keyword Extraction")
Keyword extraction is shown in a table that has an index, the keyword, and its frequency. Users can also change the number of rows displayed up to a maximum of 100. There are also toggles for the two parameters: ignore case and extract lemma. When selected, the backend sends a new list of keywords and the table is updated

![References Extraction](/2021/group6/images/analysis_features/refs_extraction.png "References Extraction")
Each reference is shown on its own line separated by a divider. We have included the index for each reference, which is displayed above it.

![Metadata Extraction](/2021/group6/images/analysis_features/metadata_extraction.png "Metadata Extraction")
Metadata consists of the title of the paper, an optional subheading, any additional data the extraction process retrieved, and the list of authors. The default order of the authors is the same as the one in the paper, but users have the option to sort them alphabetically.

![Metrics](/2021/group6/images/analysis_features/metrics.png "Metrics")
The metrics of the paper calculated are the number of words, reading time and speaking time.
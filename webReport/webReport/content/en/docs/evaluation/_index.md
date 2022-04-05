
---
title: "Evaluation"
linkTitle: "Evaluation"
weight: 8
date: 2022-4-01
description: >
  Summary of achievements, evaluation of deliverables and future work
---

Contents:
* [Summary of Achievements](#summary-of-achievements)
* [Critical Evaluation of the Project](#critical-evaluation-of-the-project)
* [Possible Improvements and Future Work](#possible-improvements--future-work)

## Summary of achievements

### MoSCoW List Revisited
| ID | Requirement                                                     | Priority | State |
|---:|-----------------------------------------------------------------|:--------:|:-----:|
|  1 |The user can upload a PDF paper from local machine for analysis  |   MUST   |   ✓   |
|  2 |The user can upload a PDF paper from a URL link for analysis     |   MUST   |   ✓   |
|  3 |The system must have an web-based user interface where the file can be uploaded and where the results of text analysis can be displayed                                         |   MUST   |   ✓   |
|  4 |The text analysis must include whole paper summarization         |   MUST   |   ✓   |
|  5 |The text analysis must include partial (segment) summarization (preferably summaries of different sections and/or subsections)                                                    |   MUST   |   ✓   |
|  6 |The text analysis must include keyword extraction                |   MUST   |   ✓   |
|  7 |The text analysis should calculate and display research paper metrics such as number of words, reading & speaking time                                                          |  SHOULD  |   ✓   |
|  8 |Extract the metadata of the paper (eg. Year published, volume, issue numbers)                                                               |  SHOULD  |   ✓   |
|  9 |The system should show full list of authors                      |  SHOULD  |   ✓   |
| 10 |The system should be able to run locally on different OSs        |  SHOULD  |   ✓   |
| 11 |The system should extract, organise and display the references   |  SHOULD  |   ✓   |
| 12 |Sort the list of authors by name or original order               |  COULD   |   ✓   |
| 13 |The system could allow upload of a OCR scanned paper if in PDF   |  COULD   |   ✓   |
| 14 |Process multiple papers simultaneously (equivalent to provide service to multiple users at once)                                                                  |  COULD   |   ✓   |
| 15 |Perform several text analysis features simultaneously for one uploaded file                                                                   |  COULD   |   ✓   |
| 16 |The system recognizes URL links, which user can click on         |  COULD   |   ✗   |
| 17 |Export metadata into a database (eg. .bib file for Latex)        |  COULD   |   ✗   |

**Key functionalities (MUST+SHOULD): 100% (11/11)**

**Optional functionalities (COULD): 66% (4/6)**

**Overall functionalities: 88% (15/17)**

#### Non-functional requirements revisited

| ID | Requirement                                                     | Priority | Evaluation / Measurement |
|---:|-----------------------------------------------------------------|:--------:|--------------------------|
|  1 | Documentation: the system must have proper in-code and external documentation                                                          |   MUST   |KONLA is delivered with highly detailed documentation, including user manual, deployment guide, API endpoints document, legal statement                             |
|  2 | Extensibility: the system must be designed in a way that allows it to be easily extended in future development (adding features etc.)                                                                  |   MUST   |KONLA is easily extensible. Adding new functions follows three steps: 1) creating a new processing method in PaperProcessor, 2) writing an access API endpoint for it and saving it in cache, 3) implementing Vue component to display this particular result. All these parts have similarity to current functionalities, adding features is fast and easy.
|  3 | Usability: the user interface must be intuitive to maximise user productivity, user manual must be written                                                                |   MUST   |Although User Manual is available and the UI is intuitive and demands no previous training or acquaintance. There are some usability issues mentioned in Known Bug List |
|  4 | Open source: the system should be designed as to be published as an open-source project, i.e. the code should be comprehensible to the wider public                                                       |  SHOULD  | Full documentation and in-code comments are in place. Our project partner said they are sufficient to understand the technology behind the project. The license has been specified to allow making project open source.
|  5 | Performance: the system should come to a compromise between its accuracy, efficiency and speed, in order to satisfy its users following usability requirement.                                       |  SHOULD  | We chose simpler and faster methods for the most demanding functionalities, so that the user does not have to wait too long. Accuracy differs depending on the type of paper and its content, but can be further improved in general.
|  6 | Deployment: the final prototype could be deployed online        |  COULD   | The project has been successfully deployed online using MS Azure services. Because of its dependencies it uses a significant portion of available CPU, thereby it may be slower than when running locally.

### Known Bug / Issue List
| ID | Bug / Issue Description                                                   | Priority | Possible Fix |
|---:|---------------------------------------------------------------------------|----------|--------------|
|  1 | No error is shown when user enters an invalid URL                         |   Low    | Catch the error in frontend and display it |
|  2 | Choosing lemmatization (lemma) checkbox in keyword extraction result box by default ignores the letter case which is toggable by another button | Low | This may need some clarification in interface or a slight change in UI design |
|  3 | For segments which consist of many mathematical formulas there is a bias towards extracting sentences with numbers | Medium | Partially ignore math formulas at text preprocessing stage for clean-up OR give lower score to sentences with higher number of mathematical formulas for extraction | 

### Individual Contribution Table
| Work package            | Bart  | Suraj | Minyi |
|-------------------------|:-----:|:-----:|:-----:|
|Client Liaison           |  70%  |    0% |  30%  |
|HCI Requirement analysis |  40%  |   32% |  28%  |
|Research & Experiments   |  34%  |   33% |  33%  |
|UI & UX Design           |   0%  |  100% |   0%  |
|API                      |   0%  |    5% |  95%  |
|System Architecture      |   5%  |    5% |  90%  |
|Backend                  |   5%  |    5% |  90%  |
|Frontend                 |   0%  |   95% |   5%  |
|NLP                      |  80%  |    0% |  20%  |
|Deployment               |   0%  |    0% | 100%  |
|Testing                  |  33%  |   33% |  34%  |
|Documentation            |  70%  |   10% |  20%  |
|Report Website           |  60%  |   10% |  30%  |
|Slides & Presentation    |  55%  |    5% |  40%  |
|Video Editing            |   5%  |    5% |  90%  |
|**Overall contribution** |**33%**|**33%**|**34%**|
|Main Roles               |Client Liaison, NLP Researcher, Documentation Editor |Frontend Development, UI/UX Design, Blog Writer|Backend Development, tech leader, platform design and integration|


## Critical evaluation of the project
* User interface / user experience (if applicable)
* Functionality
* Stability
* Efficiency
* Compatibility
* Maintainability
* Project management

## Possible Improvements & Future Work
One of the most difficult decisions during the design of KONLA was the choice between accuracy and performance. This trade-off significantly limited our capabilities of producing a system that could be both fast and accurate. 
The performance is dependent on the file size, language model and the algorithms behind the text analysis tasks. 
The accuracy is dependent on the text analysis model and algorithms, but it is also limited by the noise in data. The PDF to text conversion works well in simple, formatted texts including standard characters, while richly formatted research papers with mathematical equations generate a lot of noise in the data making it more difficult to derive useful insights.

Another important factor is the language model itself. The more general it is the worse the results can be for papers that include texts in a very specific domain. Ideally, the model should be fine-tuned for analysing research papers from a specific domain of knowledge. While this method requires a lot of domain-specific data for training, it can be rewarding in terms of system accuracy.

Here are some general suggestions on how to improve the existing system:
1.	Make the analysis tasks and model domain specific
2.	Experiment with other summarization algorithms to increase accuracy
3.	Implement new features such as image extraction, search tool, multiple paper analysis, similar paper detection, saving analysis results in a database etc.

As the project is well constructed, it is easy to expand its capabilities. In fact, new frontend or new backend can be easily fitted to existing solutions. The backend API version 1 can be copied and improved creating a newer version, for example under “api/v2” endpoint.

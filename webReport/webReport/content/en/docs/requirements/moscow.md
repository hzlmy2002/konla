---
title: "MoSCoW requirement list"
linkTitle: "MoSCoW requirement list"
weight: 5
date: 2022-4-01
description: >
---
After further discussion with our client, we reached an agreement on which requirements the system should cover. We created a MoSCoW list for the functional and non-functional requirements of the system.

### Functional Requirements 

MUST HAVE:
- The user can upload a PDF paper from local machine for analysis
- The user can upload a PDF paper from a URL link for analysis
- The system must have an web-based user interface where the file can be uploaded and where the results of text analysis can be displayed
- The text analysis must include whole paper summarization
- The text analysis must include partial (segment) summarization (preferably summaries of different sections and subsections)
- The text analysis must include keyword extraction

SHOULD HAVE:
- The text analysis should calculate and display research paper metrics such as number of words, reading & speaking time
- Extract the metadata of the paper (eg. Year published, volume, issue numbers)
- The system should show full list of authors
- The system should be able to run locally on different OSs
- The system should extract, organise and display the references

COULD HAVE:
- Sort the list of authors by name or original order
- The system could allow upload of a OCR scanned paper if in PDF
- Process multiple papers simultaneously (equivalent to provide service to multiple users at once)
- Perform several text analysis features simultaneously for one uploaded file
- The system recognizes URL links, which user can click on
- Export metadata into a database (eg. .bib file for Latex)

WON’T HAVE:
- The system won’t store the document files in a database
- The system won’t perform similar paper detection
- The system won’t allow to share the paper analysis results with a URL-link

### Non-functional requirements

MUST HAVE:
- Documentation: the system must have proper in-code and external documentation
- Extensibility: the system must be designed in a way that allows it to be easily extended in future development (adding features etc.)
- Usability: the user interface must be intuitive to maximise user productivity, user manual must be written

SHOULD HAVE:
- Open source: the system should be designed as to be published as an open-source project, i.e. the code should be comprehensible to the wider public
- Performance: the system should come to a compromise between its accuracy, efficiency and speed, in order to satisfy its users following usability requirement

COULD HAVE:
- Deployment: the final prototype could be deployed online

*Note: The MoSCoW requirement list changed throughout the project upon mutual agreement between the team and the project partner. Changes were made to prioritise specific features or discard the less important or less feasible ones.

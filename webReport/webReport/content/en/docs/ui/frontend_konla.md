---
title: "Frontend of KONLA"
linkTitle: "Frontend of KONLA"
weight: 4
date: 2022-4-02
---
This section covers the UI/UX design of our final web application.
***
#### Upload and Analysis process
Here, we will show the process of uploading a paper and the analysis page while the backend processes the paper.

![](/2021/group6/images/frontend/upload_v2.png)

The upload page has been rearranged to have the analysis feature selection at the top. We have added a search input that lets users enter a URL of a research paper online. The drag-and-drop file section has remained the same.

***

The analysis page has been completely redesigned and now shows the analysis of all implemented features. Here are the different states of this page.

![](/2021/group6/images/frontend/analysis_start_failed_v2.png)

If any issues occurred when starting the analysis process, the page will let users know by showing an error message at the top of the page.

![](/2021/group6/images/frontend/analysis_loading_v2.png)

We have made the frontend asynchronous, so while the analysis takes place in the backend, each feature will be in a loading state until it completes.

![](/2021/group6/images/frontend/analysis_completed_v2.png)

As features complete, the tab for selecting them goes green, highlighting to the user that its content is ready.

![](/2021/group6/images/frontend/analysis_error_v2.png)

If the backend sends any errors for a particular feature, its tab will go red with a warning icon. Users can click on the tab to view the list of errors.

***

#### Analysis Features Content

Here, we will show how each feature displays its content. We have used placeholder text in places where the actual analysis content would be placed.

![](/2021/group6/images/analysis_features/whole_summary.png)

The whole summarisation is just a single block of text.

![](/2021/group6/images/analysis_features/partial_summary.png)

The partial summary is divided into individual summaries of each section with the heading above.

![](/2021/group6/images/analysis_features/keywords_extraction.png)

Keyword extraction is shown in a table with headings for an index, the keyword, and its frequency. Users can also change how many rows are displayed using the numerical input, up to a maximum of 100. There are also toggles for the two parameters: ignore case and extract lemma. When selected, the backend sends a new list of keywords, matching the requested format, and the table is updated.

![](/2021/group6/images/analysis_features/refs_extraction.png)

Each reference is shown on its own line separated by a divider. We have included the index for each reference above it.

![](/2021/group6/images/analysis_features/metadata_extraction.png)

Metadata consists of the title of the paper, an optional subheading, any additional data the extraction process retrieved, and the list of authors. The default order of the authors is the same as written in the paper, but users have the option to sort them alphabetically or reverse alphabetically.

![](/2021/group6/images/analysis_features/metrics.png)

The metrics of the paper calculated are the number of words, reading time and speaking time. They are shown in their own containers with the metrics data centered in a large font.

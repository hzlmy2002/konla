---
title: "Weeks 24-25"
linkTitle: "Weeks 24-25"
date: 2022-03-28
description: >
  **(28.03.2022 - 06.04.2022)**


  During weeks 31 and 32, we finalised our deliverables.
---


### Deadlines

| Task                                    | Date                |
|-----------------------------------------|---------------------|
| Code Handover to Client                 | 04-04-2022  2:00pm  |
| Submission of Deliverables to Moodle    | 06-04-2022  4:00pm  |
| Submission of Ind. Report to Moodle     | 06-04-2022  4:00pm  |
| Assessment Meeting                      | 08-04-2022 11:00am  |


### 31 Mar
* Added unittests for backend analysis tasks

### 1 Apr
* Working on report website
* dev blog

### Frontend - Version 2
The frontend has been updated to a newer version with more features being added. This version focuses on asynchronisation which allows the frontend to communicate with the backend in real-time. The backend and frontend exchange data using JSON. Requests are sent to specific endpoints and when they respond, the UI updates to render the data.

![Upload page](/2021/group6/images/frontend/upload_v2.png "Upload page")

The upload page has been rearranged to have the analysis feature selection at the top. We have added a search box that users can use to enter a URL of a research paper to analyse. The drag-and-drop file section remains the same.

The analysis page has been completely redesigned and can now show the analysis of all features. Here are the different states of this page.

![Analysis failed to start state](/2021/group6/images/frontend/analysis_start_failed_v2.png "Analysis failed to start state")

The analysis page sends a request to start the analysis process on the backend. If any issues occurred and the process couldn't be started, the frontend will let users know by showing an error message at the top of the page.

![Analysis loading state](/2021/group6/images/frontend/analysis_loading_v2.png "Analysis loading state")

In version 1 of the frontend, users would have to wait for all analysis to be completed before being sent to the analysis page which would then show all features at once. This meant features that were completed would be inaccessible to users until all were completed.

By implementing asynchronisation, users are taken to the analysis page as soon as they have uploaded a paper or URL. Now users will see the features they selected in a loading state as they wait for them to be completed.

![Analysis completed state](/2021/group6/images/frontend/analysis_completed_v2.png "Analysis completed state")

As soon as any feature is completed, its tab will go green and the loading icon is hidden. The image above shows some features are still being processed, but others have finished. Users can now click on completed features and see the analysis data while they wait for the rest of the features to be completed.

![Analysis error state](/2021/group6/images/frontend/analysis_error_v2.png "Analysis error state")

Sometimes, an error can occur during the analysis of a particular feature, for example in this case whole paper summarisation. Users will be alerted by seeing a red tab and an info icon. When clicking on this tab, they will see a list of errors sent from the backend describing the problem.


### Achievements


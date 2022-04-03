---
title: "Week 3"
linkTitle: "Week 3"
date: 2021-11-01
description: >
  **(01.11.2021 - 07.11.2021)**


  This week we continue HCI stage of the project, discovering and specifying usecases and requirements for our system.
---

### Week Summary 
Our project is to make a platform that can help researchers to read papers.
We created a survey that can be used to collect inputs from researchers, but it seems there are some legal issues when we tried to let our tutor spread the survey. As our tutor suggested, we can arrange meetings with them to interview them and to learn what the researchers require from the application. Minyi got one input from his supervisor, Dr Maria. She suggested we can make a tool that can build the dependency tree of the references or detect similar papers (semantic similarly). Furthermore, we can extract metadata from some interesting papers into a database that can be exported.

### Tasks
* [x] Work on HCI Report (due 10 Nov)
* [x] Create Persona 1
* [x] Create Persona 2
* [x] Finish Interactive Wireframe

### 1 Nov, Personas & Sketches
* Created new [Personas](#persona)
* New improved versions of personas are now available on Google Drive.
* New sketches were added for discussion on group meeting

### 1 Nov, Web Framework Discussion
* Flask vs Django, https://hackr.io/blog/flask-vs-django, important takeaway: Django although its high ability to scale, is not suitable for projects with constantly changing requirements, it is however good for large complex sites
* Decided on using Flask for the 1st prototype version
* Shared Google Drive with our client

### 4 Nov, Group Meeting
* Received more suggestiongs for summarization from our cohort
* Collaborated on interactive whiteboard to create 1st version of [MoSCoW Requirement List](#moscow-requirement-list)
* Showed progress on [Figma Mockup](#figma-mockups)

### 7-8 Nov
* Updated Persona 1 & 2
* Finished [Mockups](#figma-mockups)
* requirements stage 2 Part added to HCI report

### Persona
We have created our first virtual persona: Dr Robert Jarvis, who is a medical researcher. We are ready to create the second persona which will be based on the inputs collected from the survey. Hopefully, we can have more progress by next week.
![](/2021/group6/images/hci/Persona1.png)
![](/2021/group6/images/hci/Persona2.png)

### Initial Sketches
We began our design process with a few sketches of how the system would look. It allowed us to come up with core features that would be shown to the client to be discussed. By drawing the first sketches on paper, it enabled us to focus on generating key ideas instead of worrying about the exact layout of all elements.

![Sketch1](/2021/group6/images/hci/prototype/sketch1.jpg "Sketch 1 of research application")

**Sketch 1** contains the sections: Upload, Sidebar, Figures, and About of the application.
The Sidebar is how the user will navigate the application once they have uploaded a paper. It provides buttons to go to different areas of the app.

![Sketch2](/2021/group6/images/hci/prototype/sketch2.jpg "Sketch 2 of research application")

We also drew two more sections: Read and References. The About Section is continued here, but in the actual application, the About section would be scrollable, allowing the user to access the rest of it.



### Figma Mockups
After the initial sketches, we started designing some mockups for the application. The mockups would show how the features from the hand drawings would appear to a user using the application. We created a mockup for each section of the application using [draw.io](https://draw.io/). We also copied all the mockup designs into a mockup design platform, [Figma](https://www.figma.com/), where we could add transitions for all the buttons, allowing us to simulate how a user might interact with the application. The interactive version can be found [here](https://www.figma.com/proto/4Vaj580SXIfbNgF7qDAYxQ/Research-App-Mockup?node-id=19%3A35&scaling=contain&page-id=0%3A1&starting-point-node-id=19%3A35).

![Upload section](/2021/group6/images/hci/prototype/Upload_Section.png "Upload section")

The Upload Section is where the user uploads a paper. The mockup shows a drag-and-drop area as that might be one method of uploading a file. Other methods include: manual file selection and retrieving a paper from a URL.

![About section](/2021/group6/images/hci/prototype/About_Section.png "About section")

The About Section highlights the metadata from the paper. Author names are displayed comma-separated which can be sorted alphabetically or in how they appear in the paper. Metrics is data calculated on the text from the paper.

![Read section](/2021/group6/images/hci/prototype/Read_Section.png "Read section")

The Read Section is where the user can read the contents of the paper. Headings and paragraphs are extracted from the file and shown in a custom style. The abstract is put into its own section.

![Figures section](/2021/group6/images/hci/prototype/Figures_Section.png "Figures section")

The Figures section is where images from the paper are shown. The user can cycle through the figures in the order they appear in the paper. A title and summary are provided for each image.

![References section](/2021/group6/images/hci/prototype/References_Section.png "References section")

References are extracted from the paper and displayed in a list.

### MoSCoW Requirement List
We arranged a meeting and used an interactive board to create an initial version of the MoSCoW requirement list. MoSCoW stands for Must-have, Should-have, Could-have, and Would-have. The list of tasks separated into these sections allow us to prioritise certain features over others. We plan to implement the most important requirements first from the Must-have section and then move to those in the subsequent areas. It also allows us to see the future potential of the project by discussing features that we may not implement in time, but would complete the system in the Would-have section.

![MOSCOW Requirements](/2021/group6/images/MOSCOW.jpg "MOSCOW Requirements")
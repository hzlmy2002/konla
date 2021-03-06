---
title: "Weeks 16-17"
linkTitle: "Weeks 16-17"
date: 2022-01-31
description: >
  **(31.01.2022 - 13.02.2022)**

  
  [Description]
---


### 2-4 Feb
* Updated flask to support API
* Started working on Vue application
* Harry designed the API structure, 50%
* npm was added

### 4-8 Feb
* updated frequency counter
* enabled vue hot encoding

### 9-11
* Drag and drop pdf
* Analysis feature selection post
* Reference recognition (13 Feb improved rules)

### Revised Project Structure & Clean-up
We have done our first presentation a week ago, and after that, we decided to clean our repository. A new structure has been designed like this.
![New Structure](/2021/group6/images/new_structure.jpg "New Structure")

Here, "Konla" is the root directory of our repository, and folder "src/" will store our source code. We will put our documentations inside "/doc" folder. "build" directory will store our completed and deployment ready programs.

The "src/" folder is the most important one. Inside it, there are three folders which are used to store the code of frontend, backend and configurations separately. We decided to use Vue3 as our frontend framework and Flask as the backend framework, and both of them will be packed into a docker container. Inside the "apps/" folder, we will put our own libraries which is responsible for the text summarization and pdf extraction here. Thus, flask can invoke them very easily. This design makes sure every part is isolated and won't impact others if it has been changed.

![Structure](/2021/group6/images/docker_structure.png "Docker Structure")

As you can see above, Flask will act like a router to route the user request and invoke the corresponding libraries. Nginx will serve the user requests and pass them to the flask through wsgi. Everything will run inside docker, to make sure our program can be deployed in any environments.

---
title: "Choice of Web Framework"
linkTitle: "Choice of Web Framework"
weight: 5
date: 2022-4-01
description: >
   In this section we explain our initial choice of web framework and why we decided to change it in the middle of the project. 
---

### Initial Choice: Flask vs Django

During the technology research stage of the project, our team discussed both **Flask** and **Django** as webframeworks for our system. The team was already familiar with Flask to some extent. We knew that Flask is an easy-to-use, lightweight framework compared to Django, and that it may be easier to get the first version of the system built on it. At the same time, Django is not the best option when the project requirements change dynamically [1]. That is why we chose Flask as our initial web framework for the project.

### Change in Web Framework
The first prototype version of the system that we demonstrated during industry showcase used Flask for the backend. However since then we started to observe several disadvantages of using this web framework. One of the main flaws was that our application became to scale and we needed to add new plugins to Flask application for cookie and session management, security, etc. Although Flask itself is easy to learn, its plugins documentation were not so clear, thereby we faced a blocker in the development. Therefore, we decided that it is time to change to **Django**. The requirements were already set and the project direction was clear so we could focus on building a scalable web application using Django. Changing from Flask to Django did not take a lot of time, as there are many similarities between them. Moreover, Django did not require any external plugins to support our desired functionalities. Session management, security and native Redis support are all built-in in Django application already unlike in Flask. This crucial decision allowed us to overcome the problems in application development, increase the overall stability of the system, scale it and prepare it well for deployment.

### References
[1] Flask vs Django in 2022: Which Framework to Choose? [Internet]. Hackr.io. [cited 2022 Apr 4]. Available from: https://hackr.io/blog/flask-vs-django

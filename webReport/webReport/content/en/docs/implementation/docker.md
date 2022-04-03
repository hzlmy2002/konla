---
title: "Docker Container"
linkTitle: "Docker Container"
weight: 3
date: 2022-4-01
description: >
  Implementation of the docker container
---
The docker container runs and manages everything like magic but in fact it's extremly simple. We run everything inside one docker container, so that there must have one master process that starts all the other process. The master process is supervisord, which is a daemon process that similar to "init" or "systemd" in Linux. The master process will supervise all the other processes, and it will restart them if they are crashed. When we run the docker container in detached mode, the docker container will start the supervisord and put the entire container to the background. Inside the container, Django, nginx and redis will all be started. 

During the building process of the docker container, the Dockerfile will do the following stuffs:
- Install the required packages
- Copy the entire repository to the docker container
- Install the python dependencies and download the spaCy model
- Build the frontend Vue.js application and copy the files to the static directory(/var/www/html) of Nginx
- Set the permissions of the some directories
- Copy the configuration files to the right places
- (if in detached mode) Start the supervisord

This can also be done by docker-compose, though we did not use that way. The reason why we did not use docker-compose is some of the communications between the different parts are through unix socket, which increases the difficulty to do inter container communication. Sharing the unix socket requires bind mount a same volumn for all the containers. Single container also makes stuffs simpler.
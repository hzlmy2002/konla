---
title: "Backend API Server"
linkTitle: "Backend API Server"
weight: 2
date: 2022-4-01
description: >
  Implementation of the backend API server
---

The backend API server uses one very famous framework called "Django", which allows us to develop a good web server very quickly. Meanwhile, it provides lots of features such as **session management**, **supporting of Redis database**. The implementation can be summarized as the following.

### Abstracted Paper object: Paper Processor
Paper processor is an object which contains the paper text, tokenized text, paper's metadata and the NLP model itself. It provides several class methods which wraps our implementations of the all the NLP and non NLP features. This makes sure the backend API server does not need to care about how to implement the features that we want, and the API server can invoke the Paper processor's methods to get the desired result. This is a kind of separation of concerns that allows us to modularize the whole backend.

### Accepting user uploaded pdf File
When the user tries to upload a pdf file to the server, the server will first save the pdf file into a temporary folder (/tmp in our implementation). Meanwhile, the api server will do two things to keep track of the uploaded paper. First, it will calculate the sha256 of the pdf file, as it's identifier, then it will save it's file name. These two attributes will be save to the Django Request object's session dictionary. The session mechanism is implemented by Django framework itself. As long as the user did not close his browser, the Request object will always have the same session dictionary.

### Accepting user submitted paper URL
The implementation of this way is almost the same as direct paper uploading, except the backend needs to download the paper from the URL. Once the paper has been downloaded, it will be saved to the temporary folder. The following processes are the same as the previous method.

### Authentication
As mentioned before, the Request object's session dictionary keeps the checksum (identifier) and the file name, so that we can always know who uploads what. To separate the user's data, the checksum has been used as the "prefix" of the keys for the Redis database that stores the papers processing status and final results. As a result, if the request comes with the session cookie implemented by Django, we can always find the correct data in the Redis database.

The association looks like:
```
request cookie -> session dictionary -> checksum (identifier) -> Redis database key prefix -> paper processing status and final results
```

### Asynchronized Tasks execution
This is most complicated part of our backend implementation. After user selects his desired features and click the start button, the backend will start to process the paper. In order to make the backend asynchronizely, the backend should send the acknowledgement to the frontend that it receives the tasks request right after the user click the start button. Furthermore, when the backend is processing the paper and does not get the result, it should also be able to reply to the frontend that it is still unfinished. This means the processing of the paper cannot block other requests, thus, the backend need to run these tasks in separate threads.

In order to improve the performance, the backend should not do duplicated works, such as loading the NLP model and the tokenize the text multiple times, thus, they should share the same paper processor object which already has them. They way that we finally used is:

1. The backend will spawn one new thread when the user clicked the start button. This thread will create a paper processor object which will read the metadata, tokenize the text, and load the NLP model. Meanwhile, the enabled features table will be saved into Redis database with prefix(checksum)+"_"+featureTable as the key. Furthermore, the status of system initialization will be set to 0 (in progress) in the Redis database.
2. When the paper processor object has been created, this thread will spawn several new threads, where each threads will corresponding to one enabled features. Let's say they are tasks, and the paper processor object will be passed to these tasks through function arguments, as well as the Redis database key prefix(checksum). Then the threads will be activated and run the tasks. At this stage, the status of the system initialization will be set to 1 (completed) in the Redis database.
3. When these threads are activated and the tasks are running, their tasks' status will be set to 0. When they are completed, the results will be write to the Redis database with prefix(checksum)+"_"+featureName as the key, and the status will be set to 1.
4. each task runs in one thread. As we already wrap the implementation of all the features into the paper processor object's methods, we can simply call the methods to get the desired results. After we get the results, we can save them to the Redis database with prefix(checksum)+"_"+featureName as the key.
5. When the frontend is requesting one or more results, the backend will check the Redis database to see if the results are ready. If they are, the backend will return the results to the frontend. Otherwise, the backend will send the "in progress" to the frontend indicates the results are not ready yet, with an empty result. The status is indicated in "status" section of the response.

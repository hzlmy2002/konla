---
title: "System Architecture"
linkTitle: "System Architecture"
weight: 1
date: 2022-4-01
---

The researchers can use their browser to use our Konla app, where the Vue.js app will be loaded to their browser. They can upload and select the features they want to enable. After click the start button, the frontend will sent the requests to the backend. When the backend received these requests, it will spawn several threads to run all the tasks parallelly. After clicked start button, the frontend will keep querying the data from the backend, and if the corresponding task is still in progress, the frontend will show a loading icon. All the threads will save their intermediate data, status and the final result into the redis database. The redis database will be checked if the server receives requests. If one task is done, the frontend will show the result while keep other features in progress status. This makes sure some time consuming tasks will not prevent the researchers from checking some quick results after they are completed.

![](/2021/group6/images/system_architecture.png)

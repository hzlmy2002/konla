---
title: "Unit & Integration Tests"
linkTitle: "Unit & Integration Tests"
weight: 2
date: 2022-4-01
description: >
---
This is done by using the django.test that is base on unittest.
To ensure the correctness of the result, we added unit tests to the backend API server. The testing will be carried on a example paper. The paper will first be downloaded from its URL, and pass to the testing object. It will be extracted text at first, and then tokenize the text. After that, we will test the all the features except the references extraction, summarisation. 

The integration test is done manually. We uploaded multiple different papers by different way and check whether we get a desired result or not. The cookie issue has been discovered and fixed in this stage.
---
title: "Testing strategy"
linkTitle: "Testing strategy"
weight: 1
date: 2022-4-01
description: >
---
As the output for NLP model is not fixed and unpredictable, it's unrealistic to test the features which are related to NLP model by using unit test, and we did those tests manually. For example, it's not possible to provide a very precise result of the references and this can only be verified manually.

We use unit test (django.test) to test other parts.
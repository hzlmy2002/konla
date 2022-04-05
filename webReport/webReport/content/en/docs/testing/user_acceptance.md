---
title: "User acceptance testing"
linkTitle: "User acceptance testing"
weight: 3
date: 2022-4-01
description: >
---
|Test Case|Result|Feedback|
|---------|------|--------|
| Uploading a paper through file uploading|Pass|Works well|
| Uploading a paper through URL|Pass|Could add validations to the URL|
| Start the analysis| Pass|Works well, shows a warning if no features were selected|
| General analysis result page|Pass|Works well, the progress icon looks good|
|Whole summarisation|Pass|Mostly works well|
|Patrial summarisation|Pass|The summary by section looks good|
|Word frequency|Pass|If both ignore case and lemma have been enabled, only result for lemma has been displayed.(It's a feature, should be explained further)|
|References Extraction|Pass|Works well|
|Metadata extraction|Pass|Some information will missing sometimes(This depends on the file itself, should be explained)|
|Metrics|Pass|Works well|
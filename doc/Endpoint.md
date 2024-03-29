<!-- COMP0016-Team6-Minyi Lei, Suraj Kothari-->
# API 

## Project Documents
1. [README.md](../readme.md)
2. [Deployment Guide](DeploymentGuide.md)
3. [User Manual](UserManual.md)
4. [Docs](KONLA_Documentation.pdf)
5. API

## Endpoint

```
https://konla.thinktank007.com/api/v1/
```

## Structure
```
|--- endpoint(/api/v1/)
         |--- upload
         |       |--- binary
         |       |--- url
         |       |--- start
         |
         |--- summarisation 
         |          |--- whole
         |          |--- partial
         |
         |--- keywords
         |
         |--- info
	 |	|--- refs
	 |	|--- metadata
	 |	|--- metrics
         |
         |--- images
```

### Upload (binary&url)

**Endpoint**: /api/v1/upload

**Description**: The upload api is used for uploading binaries like pdf or images. The user can also submit an url so that the server can download and analyse it. 

**Methods**: POST for binary, GET for url

**Parameters**:

* None

**Request**:

* binary: POST the content directly, endpoint is /api/v1/upload/binary

* url: GET request. Using http parameter with key "link=". E.g. "/api/v1/upload/url?link=https://ucl.ac.uk/cs/shapes.pdf". Endpoint is /api/v1/upload/url.

**Response**: 

```json
{
    "current_status": 1, # -1 means incomplete, 0 means failed, 1 means completed and success
    "errors": [],
    "messages": [],
    "result": {
    	"sha256": "5c061a8549a38daee917491da054ad37c3edf8dd06656c5e0743a1f4dfb42f5a",
    	"text": "content of the paper"
    }
}
```

### Upload (start)

**Endpoint**: /api/v1/upload/start

**Description**: After uploading the paper, the backend needs to know which functionalities will be activated, cookie should contain session id

**Methods**: POST (in html form)

**Parameters** (For all the following parameters they are all either 0 or 1,where 0 represents disabled and 1 represents enabled):

* whole: Control whether enable whole summarisation
* partial: Control whether enable partial summarisation
* keywords: Control whether enable keywords extraction
* refs: Control whether enable references extraction
* metadata: Control whether enable meta data extraction
* metrics: Control whether enable metrics calculation

**Request**:

Request body:

```
whole=1&partial=1&keywords=1&refs=1&metadata=1&metrics=1
```

**Response**:

```json
{
    "current_status": 1,
    "errors": [],
    "messages": [],
    "result": {}
}
```

### Whole Summarisation

**Endpoint**:/api/v1/summarisation/whole

**Description**: The whole summarisation function is used to get summarised paper.

**Methods**: GET

**Parameters**:

* ~~None~~

**Request**:

* Access this endpoint directly with cookie that contains session id.

**Response**:

```json
{
	"current_status": 1,
 	"errors": [],
    	"messages": [],
    	"result": {
    		"whole_summarisation": "Whole summarised paper content"
    	}
}
```



### Partial Summarisation

**Endpoint**: /api/v1/summarisation/partial

**Parameters**:

* TBC

**Description**: The partial summarisation function is used to summarise the paragraphs of the paper.

**Methods**: GET

**Request**: 

* TBC

**Response**:

```json
{
	"current_status": 1,
 	"errors": [],
    	"messages": [],
    	"result": {
    		"partial_summarisation": {"section1 title":"summarized text for section1","section2 title":"summarized text for section2"}
    	}
}
```

### Keywords Extraction

**Endpoint**: /api/v1/keywords

**Description**: This api return a list of most frequent keywords with their occurrences.

**Methods**: GET

**Parameters**:

* max: int. This parameter indicates the max number of most frequent key words, should within [1,100]. Default value is 100.
* ignorecase: int. The default value is 0. This parameter indicates whether ignore uppercase. 0 represents not ignore, 1 represents ignore
* extractlemma: int. The default value is 0. This parameter indicates whether extract the lemmas instead of exact words. 0 represents disable, 1 represents enable.

**Request**:

* get https://konla.thinktank007.com/api/v1/keywords?max=10&ignorecase=0&extractlemma=0

**Response**:

```
{
	"current_status": 1,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"keywords": {"Hello": 10, "World": 6, "KONLA": 3}
    	}
}
```

## Information

### References

**Endpoint**: /api/v1/info/refs

**Description**: This API returns the information of extracted references in the paper.

**Methods**: GET

**Parameters**:

* None

**Request**:

* get https://konla.thinktank007.com/api/v1/info/refs

**Response**:

```
{
	"current_status": 1,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"refs": ["ref1", "ref2"]
    	}
    }
}
```

### Metadata

**Endpoint**: /api/v1/info/metadata

**Description**: This API returns the metadata from the paper. This includes authors, title, and other file information

**Methods**: GET

**Parameters**:

* None

**Request**:

* get https://konla.thinktank007.com/api/v1/info/metadata

**Response**:

```
{
	"current_status": 1,
    	"errors": [],
    	"messages": [],
    	"result": {
    		
    		"metadata": {
			"authors": ["Nikhil Parasaram", "Earl T. Barr", "Sergey Mechtaev"],
    			"creator": "Appligent AppendPDF Pro 5.5", 
    			"producer": "pdfTeX-1.40.21; modified using iText® 7.1.16 ©2000-2021 iText Group NV (IEEE; licensed version)", 
    			"subject": "IEEE Transactions on Software Engineering; ;PP;99;10.1109/TSE.2021.3124323", 
    			"title": "Title Of Research Paper"
    		},
    	}
}
```

### Metrics

**Endpoint**: /api/v1/info/metrics

**Description**: This API returns the metrics calculated from the text. This includes character count, word count, reading and speaking times.

**Methods**: GET

**Parameters**:

* None

**Request**:

* get https://konla.thinktank007.com/api/v1/info/metrics

**Response**:

```
{
	"current_status": 1,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"metrics": {
    			"wordCount": 1920,
    			"readingTime": 120,
    			"speakingTime": 243
    		}
    	}
}
```



### Images

**Endpoint**:/api/v1/images

**Description**: Return the list of urls that contain the images from the pdf

**Methods**: GET

**Parameters**:

* TBC

**Request**:

TBC

**Response**:

```
TBC
```




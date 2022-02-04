# Api Manual 

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
         |--- summarization 
         |          |--- whole
         |          |--- partial
         |
         |--- keyword
         |
         |--- info
         |
         |--- images
         |
         |--- status
                |--- process
```

### Upload (binary&url)

**Endpoint**: /api/v1/upload

**Description**: The upload api is used for uploading binaries like pdf or images. The user can also submit an url so that the server can download and analyze it. 

**Methods**: POST

**Parameters**:

* None

**Request**:

* binary: POST the content directly, endpoint is /api/v1/upload/binary

* url: Using html form with key "url=". E.g. "url=https://ucl.ac.uk/cs/shapes.pdf". Endpoint is /api/v1/upload/url.

**Response**: 

```json
{
    "success":true,
    "errors":[],
    "messages":[],
    "result":{
    	"sha256":"5c061a8549a38daee917491da054ad37c3edf8dd06656c5e0743a1f4dfb42f5a",
    	"text":"content of the paper"
    }
}
```

### Upload (start)

**Endpoint**: /api/v1/upload/start

**Description**: After uploading the paper, the backend needs to know which functionalities will be activated, cookie should contain session id

**Methods**: POST (in html form)

**Parameters** (For all the following parameters they are all either 0 or 1,where 0 represents disabled and 1 represents enabled):

* whole: Control whether enable whole summarization
* partial: Control whether enable partial summarization
* keyword: Control whether enable keyword extraction
* refs: Control whether enable references extraction
* meta: Control whether enable meta data extraction
* metrics: Control whether enable metrics calculation

**Request**:

Request body:

```
whole=1&partial=1&keyword=1&refs=1&meta=1&metrics=1
```

**Response**:

```json
{
    "success":true,
    "errors":[],
    "messages":[],
    "result":{}
}
```





### Whole Summarization

**Endpoint**:/api/v1/summarization/whole

**Description**: The whole summarization function is used to get summarized paper.

**Methods**: GET

**Parameters**:

* ~~None~~

**Request**:

* Access this endpoint directly with cookie that contains session id.

**Response**:

```json
{
	"success":true,
    "errors":[],
    "messages":[],
    "result":{
    	"summarization":"Summarized paper content"
    }
}
```



### Partial Summarization

**Endpoint**: /api/v1/summarization/partial

**Parameters**:

* TBC

**Description**: The partial summarization function is used to summarize the paragraphs of the paper.

**Methods**: GET

**Request**: 

* TBC

**Response**:

```
TBC
```

### Keyword Extraction

**Endpoint**: /api/v1/keyword

**Description**: This api return a list of most frequent keywords with their occurrences.

**Methods**: GET

**Parameters**:

* max: int. This parameter indicates the max number of most frequent key words
* ignorecase: int. The default value is 0. This parameter indicates whether ignore uppercase. 0 represents not ignore, 1 represents ignore
* extractlemma: int. The default value is 0. This parameter indicates whether extract the lemmas instead of exact words. 0 represents disable, 1 represents ignore.

**Request**:

* get https://konla.thinktank007.com/api/v1/keyword?max=10&ignorecase=0&extractlemma=0

**Response**:

```
{
	"success":true,
    "errors":[],
    "messages":[],
    "result":{
    	"keywords":{"A":10,"b":6,"C":"3"}
    }
}
```

### Information

**Endpoint**: /api/v1/info

**Description**: This api returns the information of the paper and the pdf file. Note, if one feature has not been enabled, this api will return an empty value

**Methods**: GET

**Parameters**:

* None

**Request**:

* get https://konla.thinktank007.com/api/v1/info
* Enabled Features: references, meta data, metrics (all)

**Response**:

```
{
	"success":true,
    "errors":[],
    "messages":[],
    "result":{
    	"refs":["ref1","ref2"],
    	"metadata":{
    				"Author": "Nikhil Parasaram; Earl T. Barr; Sergey Mechtaev", 
    				"Creator": "Appligent AppendPDF Pro 5.5", 
    				"Producer": "pdfTeX-1.40.21; modified using iText® 7.1.16 ©2000-2021 iText Group NV (IEEE; licensed version)", 
    				"Subject": "IEEE Transactions on Software Engineering; ;PP;99;10.1109/TSE.2021.3124323", 
    				"Title": "Trident: Controlling Side Effects in Automated Program Repair"
    				},
    	"authors":["Nikhil Parasaram", "Earl T. Barr", "Sergey Mechtaev"],
    	"metrics":{
    		"wordcount":1920,
    		"readingtime":"120", # unit: seconds
    		"speakingtime":"243"
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

### Status (process)

**Endpoint**: /api/v1/status/process

**Description**: Return the status of each task, where 0 represents not completed and 1 represents completed. -1 represents feature not enabled.

**Methods**: GET

**Parameters**:

* None

**Request**:

* get  https://konla.thinktank007.com/api/v1/info/process
* Disabled partial summarization

**Response**:

```
{
	"success":true,
    "errors":[],
    "messages":[],
    "result":{
    	"whole":0,
    	"partial":-1,
    	"keyword":1,
    	"refs":1,
    	"meta":1,
    	"metrics":1,
    	# TBC: images
    }
}
```






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
         |
         |--- summarization 
         |          |--- whole
         |          |--- partial
         |
         |--- keyword
         |
         |--- info
                |--- metadata
                |--- author
                |--- refs
                |--- metrics
                |--- images
```

### Upload 

**Endpoint**: /api/v1/upload

**Parameters**: 

   * ~~None~~

**Description**: The upload api is used for uploading binaries like pdf or images. The user can also submit an url so that the server can download and analyze it. 

**Methods**: POST

**Request**:

* binary: POST the content directly, endpoint is /api/v1/upload/binary

* url: Using http form with key "url=". E.g. "url=https://ucl.ac.uk/cs/shapes.pdf". Endpoint is /api/v1/upload/url.

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



### Whole Summarization

**Endpoint**:/api/v1/summarization/whole

**Parameters**:

* ~~None~~

**Description**: The whole summarization function is used to get summarized paper.

**Methods**: GET

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

**Parameters**:

* max: int. This parameter indicates the max number of most frequent key words
* ignorecase: int. The default value is 0. This parameter indicates whether ignore uppercase. 0 represents not ignore, 1 represents ignore
* extractlemma: int. The default value is 0. This parameter indicates whether extract the lemmas instead of exact words. 0 represents disable, 1 represents ignore.

**Description**: This api return a list of most frequent keywords with their occurrences.

**Methods**: GET

**Request**:

* get https://konla.thinktank007.com/api/v2/keyword?max=10&ignorecase=0&extractlemma=0

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




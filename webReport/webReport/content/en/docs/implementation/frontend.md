---
title: "Frontend (Vue.js app)"
linkTitle: "Frontend (Vue.js app)"
weight: 1
date: 2022-4-01
description: >
  Implementation of the Frontend
---

## Frontend Structure
The frontend follows a standard Vue 3 web application structure generated by vue-cli. The current user interface folder is located in src/frontend/vue-web-app.
```
./vue-web-app/src
├─ components
│  ├─ ErrorContent.vue
│  ├─ Footer.vue
│  ├─ Header.vue
│  ├─ KeywordsContent.vue
│  ├─ LoadingIcon.vue
│  ├─ MetadataContent.vue
│  ├─ MetricsContent.vue
│  ├─ PartialContent.vue
│  ├─ RefsContent.vue
|  └─ WholeContent.vue
│
├─ router
|  └─ index.js
│
├─ views
|  ├─ Upload.vue
|  └─ Analysis.vue
│
├─ App.vue
└─ main.js
```

The app is created in **main.js** and mounted to the “#app” div specified in index.html which is found in the vue-web-app/public directory.
The **index.js** in src/router maps the endpoints to the corresponding views (“/” for Upload.vue and “/analysis” for Analysis.vue). The views use templated components for displaying different parts of the webpage, resulting in a Single Page Application (SPA).

The user interface consists of two views:
* An upload view (Upload.vue), which is the default page when the service is accessed
* An analysis view (Analysis.vue), which is visible once the research paper has been uploaded and analysis features are selected

The upload view stores the selected features as a JS object and receives a research paper in PDF format or as a URL of one online. The PDF is sent to the backend as a binary object, while the URL is sent as a parameter in the fetch request. After the user clicks on “Analyse Paper” and input validation passes, the Analysis view is shown which sends a request to start the analysis process. Once it receives a confirmation that the process has been started, it continuously sends requests for the results of each feature to the backend. As soon as it receives a particular feature, the analysis tab is changed to green to mark it as completed and its content is now accessible.

## Useful Commands and Frontend Configuration
You can test the frontend on its own by opening a terminal, changing the directory to konla/src/frontend/vue-web-app and using the npm commands below.

| Command       | Description                              |
|-------------  |------------------------------------------|
|`npm install`  |Project setup                             |
|`npm run serve`|Compiles and hot-reloads for development  |
|`npm run build`|Compiles and minifies for production      |
|`npm run lint` |Lints and fixes files                     |

**Customization**

For frontend project customization, see the Vue Configuration Reference.

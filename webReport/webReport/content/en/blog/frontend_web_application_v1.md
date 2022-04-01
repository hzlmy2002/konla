---
title: "Frontend - Version 1"
linkTitle: "Frontend - Version 1"
date: 2022-01-15
description: >
---

We created a web application that can analyse research papers. In this version, the webpages are rendered on the server-side using Flask's template engine Jinja2. This allows the server to embed content received from the analysis processes into the HTML file that is then sent to the client. We designed the user interface to be similar to the initial sketches and mockups, but the current version still lacks a few features.

![Upload page](/images/frontend/upload1_v1.png "Upload page")

The upload page is where the user is able to upload a research paper. They can upload PDFs and image files (PNG or JPG) of a scanned paper. The user can click the *browse* link to open a file explorer dialog or they can simply drag the file into the dotted area.

![Upload page after selecting paper](/images/frontend/upload2_v1.png "Upload page after selecting paper")

Once they have selected their paper, a section to select the analysis tools is displayed. The user must select at least 1 of the options and can then click the **Analyse Paper** button to begin the process.

![Analysis page - Extracted text from PDF](/images/frontend/analysis_text_v1.png "Analysis page - Extracted text from PDF")

Once the server has finished processing all the analysis, the *analysis.html* file is sent to the client. The screenshot above shows a demo version as not all analysis features have been implemented yet. The section on the left has tabs for each analysis feature. For the demo, we are showing the *extracted text* and *keywords extracted* tabs only, but in later versions, these will be based on what the user has chosen on the upload page.

The *extracted text* tab's background is orange to indicate it is selected and that the data shown on the right corresponds to this tab. We have shown the raw text that is extracted from the PDF. Since it can't be shown in a presentable way, we may not show it to the user in future versions and only use it for analysis on the server instead.

![Analysis page - Keywords extraction](/images/frontend/analysis_keywords_v1.png "Analysis page - Keywords extraction")

The *keywords extraction* section has a table with the keyword and its frequency. The original data from the analysis tool is a Python list which we iterate through and embed into the HTML table elements.

For example, let's assume the analysis tool returned this list of keywords and their frequency.
```python
keywords_extracted = [["Hello", 50], ["World", 24], ["Code", 12], ["AI", 3]]
```

We then use Jinja2 to iterate through the list, select each item and insert it into the respective columns using the *&#123;&#123; data &#125;&#125;* syntax.
```html
<tbody>
  {% for keyword in keywords_frequencies %}
  <tr>
      <th scope="row">{{loop.index0}}</th>
      <td>{{keyword[0]}}</td>
      <td class="frequence-val">{{keyword[1]}}</td>
  </tr>
  {% endfor %}
</tbody>
```

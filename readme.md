<!-- COMP0016-Team6-Bartosz Grabek -->

# KONLA

KONLA (Knowledge Organisation through Natural Language Analysis) is being developed as part of the COMP0016 Systems Engineering module at UCL. It aims to provide an effective and easy to use software solution that helps with conducting research, in particular shortening the time and effort of finding relevant research papers.

## Features
 - whole text summarization
 - partial (segment) text summarization
 - extraction and display of metadata
 - keyword extraction
 - extraction and organisation of references
 - computation of text metrics (reading time, speaking time)

## Documentation
 1. README
 2. [Deployment Guide](doc/DeploymentGuide.md)
 3. [User Manual](doc/UserManual.md)
 4. [Docs](doc/KONLA_Documentation.pdf)
 5. [API](doc/Endpoint.md)

## Dependencies 
*(all are installed using Dockerfile, Docker running Ubuntu:20.04)*
### Tools
* poppler-utils
* python3
* python3-pip
* supervisor
* npm
* redis
* nginx
* en_core_web_trf (language model installed with spacy)
### Python Libraries (described in requirements.txt)
* PyPDF2==1.26.0
* spacy==3.2.0
* redis==4.1.4
* django==4.0.2
* requests==2.27.1
* django-cors-headers==3.11.0
* uwsgi==2.0.20

## Running the project locally
To run the project locally, download or clone the project from the repositoy. To run, you will need to have docker installed on your machine. Navigate to the project folder, open the terminal and follow these steps to start the production server locally:
##### Step 1 Build the docker image
`docker build -t konla .`
##### Step 2 Run the server using the safe port 443
`docker run -p 443:443 -d konla`
##### Step 3 Open the browser and try out the app
Open your browser and navigate to https://127.0.0.1

You should see the application interface. You now can use the UI or the underlying API to analyse your research papers.

**Note:** Some browsers may block the website due to security issues. For example, Google Chrome may show a message "Your connection is not private", but you can still click "Advanced" and then on the label "Proceed to 127.0.0.1 (unsafe)" to use the app.
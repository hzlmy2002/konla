# KONLA

KONLA (Knowledge Organisation through Natural Language Analysis) is being developed as part of the COMP0016 Systems Engineering module at UCL. It aims to provide an effective and easy to use software solution that helps with conducting research, in particular shortening the time and effort of finding relevant research papers.

## Documentation
 - [Development Notes](doc/dev_notes.md)
 - [API Endpoints](doc/Endpoint.md)
 - [Project Google Drive](https://drive.google.com/drive/folders/1JDZ8SehDyxVgiEWYiUXllecXl8tfoHbY?usp=sharing)

## Features
 - whole text summarization
 - partial (segment) text summarization
 - extraction and display of metadata
 - keyword extraction
 - organisation of references

## Running the project locally
To run the project locally, download or clone the project from the repositoy. To run, you will need to have docker installed on your machine. Navigate to the project folder, open the terminal and follow these steps to start the production server locally:
##### Step 1 Build the docker image
`docker build -t konla .`
##### Step 2 Run the server using the safe port 443
`docker build -p 443:443 -d`
##### Step 3 Open the browser and try out the app
Open your browser and navigate to https://127.0.0.1

You should see the application interface. You now can use the UI or the underlying API to analyse your research papers.

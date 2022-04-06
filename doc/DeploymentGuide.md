# Deployment Guide

## Project Documents
1. [README.md](../readme.md)
2. Deployment Guide
3. [User Manual](UserManual.md)
4. [Docs](KONLA_Documentation.pdf)
5. [API](Endpoint.md)

## Running the project locally

#### What you will need
* Docker installed (https://docs.docker.com/get-docker/)
* Python

#### Setup
Firstly, download project .zip folder and unpack it in desired directory or clone the project from the GitHub repository.

To run the webserver, you will need to have **Docker** installed on your machine. Navigate to the project folder, open the terminal and follow these steps to start the server locally:
##### Step 1 Build the docker image
`docker build -t konla .`
**Note:** this may take some time depending on your machine and internet connection
##### Step 2 Run the server using the safe port 443
`docker run -p 443:443 -d konla`
##### Step 3 Open the browser, navigate to https://127.0.0.1

**Note:** Some browsers may block the website due to security issues. For example, Google Chrome may show a messag "Your connection is not private", but you can still click "Advanced" and then on the label "Proceed to 127.0.0.1 (unsafe)" to use the app.

![Overcoming browser block](images/browser.png)

You should be able to see the application interface now and use the UI or the underlying API to analyse your research papers. For information on how to use KONLA, read [User Manual](UserManual.md).

##### Using project locally again
If you want to run the webserver again and did not remove the docker image from the first build, you can skip step 1 and follow steps 2 and 3 only.

## Deploying the project online
The step are very similar to deploy the project locally, except the user needs to replace the certificate and the keys in **CERT** directory with their owns. **The name of the certificate should be EXACTLY "konla.pem", and the name of the key should be EXACTLY "konla.key".** We recommended to use Cloudflare's origin certificate so that there is no need renew the certificate. If not, the whole container should be rebuild every time when the certificate needs to be renewed.

After the certificate and the key have been replaced, follow the steps in "Running the project locally". You can access the service through its domain name.

## How to stop running Docker container?
In terminal, type `docker ps` to view running docker containers, record the hash value of the running container you want to stop and type `docker kill <hash>` where `<hash>` is the hash of the container you want to stop. 
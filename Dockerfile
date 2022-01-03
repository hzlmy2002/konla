FROM ubuntu:20.04

RUN apt update && \
	apt install -y poppler-utils python3 python3-pip 

COPY . /konla

RUN python3 -m pip install -r /konla/requirements.txt

EXPOSE 8080


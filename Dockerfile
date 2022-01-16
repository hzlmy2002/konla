FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8
ENV TZ="Europe/London"

RUN apt update && \
	apt install -y poppler-utils python3 python3-pip openjdk-17-jre-headless supervisor

COPY . /konla

RUN python3 -m pip install -r /konla/requirements.txt
RUN python3 -m spacy download en_core_web_trf

EXPOSE 8080


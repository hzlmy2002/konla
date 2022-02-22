FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8
ENV TZ="Europe/London"
ENV CHOKIDAR_USEPOLLING=true

RUN apt update && \
	apt install -y poppler-utils python3 python3-pip supervisor npm redis

COPY . /konla

RUN python3 -m pip install -r /konla/requirements.txt
RUN python3 -m spacy download en_core_web_lg
RUN python3 -m spacy download en_core_web_trf
RUN python3 -m pip install pytesseract
RUN apt install tesseract-ocr -y

RUN mkdir -p /var/log/supervisor

COPY ./configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]

EXPOSE 8000
EXPOSE 5000



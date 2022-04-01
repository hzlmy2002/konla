# Copyright (c) Minyi Lei 2022
# The Dockerfile and the configuration files under configs/ are solely designed and written by Minyi Lei
# All rights reserved

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8
ENV TZ="Europe/London"


RUN apt update && \
	apt install -y poppler-utils python3 python3-pip supervisor npm redis nginx

COPY . /konla

RUN python3 -m pip install -r /konla/requirements.txt
RUN python3 -m spacy download en_core_web_trf

RUN mkdir -p /var/log/supervisor

WORKDIR /konla/src/frontend/vue-web-app
RUN npm install --save-dev
RUN npm run build
RUN cp -r /konla/src/frontend/vue-web-app/dist/* /var/www/html

RUN chmod 755 /konla && chown www-data.www-data -R /konla
RUN chmod 700 /konla/CERT && chown root.root -R /konla/CERT

COPY ./configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./configs/nginx.conf /etc/nginx/nginx.conf

CMD ["/usr/bin/supervisord"]

EXPOSE 443

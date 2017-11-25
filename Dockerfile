FROM python:2.7-alpine
MAINTAINER Robert Paul

WORKDIR /usr/src/app

RUN apk add --no-cache curl

RUN curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

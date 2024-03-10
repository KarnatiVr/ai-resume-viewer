FROM python:3.11.5-alpine3.17
LABEL maintainer="venkat.com"

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY /requirements.txt requirements.txt
RUN pip install -r requirements.txt 

USER root

COPY . . 


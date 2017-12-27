FROM python:3.6.4-alpine

COPY . /app

RUN cd /app && pip install .

WORKDIR /tmp
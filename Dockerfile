FROM python:3

RUN mkdir /tmp/etl
COPY /files /tmp/etl
RUN python -m pip install --upgrade pip

EXPOSE 8080
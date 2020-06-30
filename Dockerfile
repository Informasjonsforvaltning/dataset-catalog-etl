FROM python:3

RUN mkdir /etl
COPY /files /etl
RUN python -m pip install --upgrade pip

EXPOSE 8080

ENTRYPOINT exec ["echo", "Running... "]
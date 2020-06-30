FROM python:3

RUN mkdir /etl
COPY /files /etl
WORKDIR /etl
RUN python -m pip install --upgrade pip

EXPOSE 8080

CMD ["echo", "Running... "]
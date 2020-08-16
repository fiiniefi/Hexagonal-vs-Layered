FROM python:3.8.2-slim

ENV APP_DIR=/code

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && rm -rf ~/.cache/pip

WORKDIR /code
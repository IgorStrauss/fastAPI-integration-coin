FROM python:3.10.7-slim-buster

#setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# timezone env with default
ENV TZ America/Sao_Paulo
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /app/
ENV pythonpath=/app

# install python dependencies in /.venv
COPY requirements.txt /app/

# install container dependencies
RUN apt-get update -yy \
    && apt-get install -yy libpq-dev git \
    && apt-get install -yy python3-pip \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .


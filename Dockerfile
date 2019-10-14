# Pull Python image within Alpine Linux
FROM python:3.7-alpine
MAINTAINER Alican Donmez - alicandonmez90@gmail.com

# Utilize Python Efficient in Docker Container
ENV PYTHONUNBUFFERED 1

# Install Python Dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /requirements.txt

# Create Working Directory
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create User
RUN adduser -D appuser
USER appuser

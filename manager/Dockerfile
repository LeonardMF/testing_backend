FROM python:3.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /app

COPY . /app
RUN ["python", "setup.py", "install"]
RUN ["pip", "install", "-r", "requirements.txt"]

WORKDIR /app/manager
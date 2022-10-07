FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /drf-reduce-url

COPY requirements.txt /drf-reduce-url
RUN pip install -r requirements.txt

COPY . /drf-reduce-url
EXPOSE 8000
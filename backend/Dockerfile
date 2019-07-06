FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
RUN pip install djangorestframework
RUN pip install django-cors-headers
ADD . /backend/
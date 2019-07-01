FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
ADD requirements.txt /backend/
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install -r requirements.txt
ADD . /backend/
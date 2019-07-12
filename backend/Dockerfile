FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend
ADD requirements.txt /backend
RUN pip install -r requirements.txt
RUN pip3 install psycopg2-binary
RUN pip3 install django psycopg2
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
RUN pip3 install --upgrade setuptools
RUN pip3 install djangorestframework
RUN pip3 install django-cors-headers
RUN pip3 install dj_database_url

ADD . /backend/
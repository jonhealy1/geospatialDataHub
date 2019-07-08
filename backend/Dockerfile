FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend
# ADD requirements.txt /backend
# RUN pip install -r requirements.txt
RUN pip3 install psycopg2-binary
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
RUN pip3 install --upgrade setuptools
RUN pip3 install djangorestframework
RUN pip3 install django-cors-headers

ADD . /backend/
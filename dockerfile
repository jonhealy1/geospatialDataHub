FROM python:3


ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY wait-for-postgres.sh /code/
#POSTGRES
RUN pip3 install psycopg2-binary
#GDAL
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
#NUMPY --> FOR WINDOWS
RUN pip install numpy

RUN pip install -r requirements.txt

ADD . /code/
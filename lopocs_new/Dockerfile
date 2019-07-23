FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /lopocs
WORKDIR /lopocs
ADD . /lopocs

RUN pip3 install wheel
RUN pip3 install psycopg2-binary

RUN apt-get update &&\
    apt-get install -y apt-utils gcc libpython-dev python-dev binutils libproj-dev gdal-bin libgdal-dev libyaml-dev libpdal-dev pdal libpdal-plugin-python
    
RUN pip3 install pyproj
#RUN pip3 install PyYAML
RUN pip3 install pyyaml
RUN pip3 install setuptools
#RUN pip3 install virtualenv
#RUN virtualenv -p /usr/bin/python3 venv
#RUN source venv/bin/activate
RUN pip3 install 'numpy==1.14.3'
# RUN pip3 install GDAL
RUN pip3 install -e .

ADD . /lopocs/
# ENV PYTHONUNBUFFERED 1

# RUN mkdir /backend



# WORKDIR /backend
# ADD requirements.txt /backend
# RUN pip install -r requirements.txt
# RUN pip3 install psycopg2-binary
# RUN pip3 install django psycopg2
# RUN apt-get update &&\
#     apt-get install -y binutils libproj-dev gdal-bin
# RUN pip3 install --upgrade setuptools
# RUN pip3 install djangorestframework
# RUN pip3 install django-cors-headers
# RUN pip3 install dj_database_url

# ADD . /backend/
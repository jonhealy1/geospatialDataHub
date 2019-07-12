# geoSpatialDataHub

## Getting Started
* Clone this project to your machine
* $ cd geospatialDataHub
* $ docker-compose build
* $ docker-compose up
* navigate to: localhost:8080
* make sure to scroll down page

## Built With
* [Django REST Framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs
* [Vue.js](https://vuejs.org/) - The Progressive JavaScript Framework
* [SQLite](https://www.sqlite.org/index.html) - Database
* [ArcGIS](https://developers.arcgis.com/javascript/latest/sample-code/layers-pointcloud-portal/index.html) - ArcGIS

## Running DB in separate container
* $ docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
* $ docker inspect postgis
* Copy down Gateway address - put it into HOST field down below
* Edit settings.py

DATABASES = {
   "default": {
       "ENGINE": "django.contrib.gis.db.backends.postgis",
       "NAME": "gis",
       "USER": "user001",
       "PASSWORD": "123456789",
       "HOST": "172.17.0.1",
       "PORT": "5432",
   }
}  

* $ docker-compose down
* $ docker-compose build
* $ docker-compose up
* $ docker-compose run web python3 manage.py makemigrations
* $ docker-compose run web python3 manage.py migrate
* $ docker-compose run web python3 manage.py createsuperuser
* navigate to localhost:8000/admin - log in
* navigate to localhost:8080

* To remove container: 
* $ docker container rm -f postgis
**geospatialDataHub project**


## Set Up

<a href="https://www.youtube.com/playlist?list=PL7amXK4vKqATa_KrfQ3_tEF_ywAgAqWeJ"> Seed tutorial</a> 

<a href="https://postgis.net/install/"> Install postGIS</a> 

## Setting up DB

Create a User if you don't have one in Postgres. Create a Database in Postgres and then change the User and Database name fields in settings.py. Create extensions in your database. Start Postgres cli.

```
# CREATE DATABASE geodjangoseries;
# \c geodjangoseries;
# CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;
```

## Installing Requirements
```
pip install -r requirements.txt
```

## Sync and Running application
```
python manage.py migrate
python manage.py runserver
on browser: localhost:8000
```

## Usage

```
python manage.py createsuperuser
```

If you go to localhost:8000/admin after creating a superuser you can place events and geometric shapes on the map with some popup information. 

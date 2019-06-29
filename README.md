# geospatialDataHub

https://docs.djangoproject.com/en/2.2/intro/tutorial01/

https://docs.djangoproject.com/en/2.2/ref/contrib/gis/tutorial/

install PostGIS

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'geodjango',
         'USER': 'geo',
    },
}

Need to start a posgres databse with the name 'geodjango' and change the user to your username.
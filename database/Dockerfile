# FROM postgres:11
# MAINTAINER Mike Dillon <mike@appropriate.io>

# ENV POSTGIS_MAJOR 2.5
# ENV POSTGIS_VERSION 2.5.2+dfsg-1~exp1.pgdg90+1
# ENV POSTGRES_USER=gisuser
# ENV POSTGRES_PASS=password
# ENV POSTGRES_DBNAME=gis

# RUN apt-get update \
#       && apt-cache showpkg postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
#       && apt-get install -y --no-install-recommends \
#            postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION \
#            postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts=$POSTGIS_VERSION \
#            postgis=$POSTGIS_VERSION \
#       && rm -rf /var/lib/apt/lists/*

# RUN mkdir -p /docker-entrypoint-initdb.d
# COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh
# COPY ./update-postgis.sh /usr/local/bin

FROM kartoza/postgis
VOLUME “/data”
ENV POSTGRES_USER=gisuser
ENV POSTGRES_PASS=password
ENV POSTGRES_DBNAME=gis
EXPOSE 5432
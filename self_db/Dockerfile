# example Dockerfile for https://docs.docker.com/engine/examples/postgresql_service/
 
 
FROM ubuntu:latest
 
RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
# RUN  dpkg-divert --local --rename --add /sbin/initctl
# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
#RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt bionic-pgdg main" >> /etc/apt/sources.list
# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.3``.
#RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
#RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
#RUN  dpkg-divert --local --rename --add /sbin/initctl
RUN apt-get -y update; apt-get -y install gnupg2 wget ca-certificates rpl pwgen

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get clean
RUN apt-get autoclean
RUN apt-get install synaptic; apt-get update
RUN apt-get update; apt-get upgrade; apt-get install -y libproj12 postgresql-client-11 postgresql-common postgresql-11 postgresql-11-postgis-2.5 postgresql-11-postgis-2.5-scripts postgresql-11-pgrouting netcat

#RUN apt-get update; apt-get upgrade; apt-get install -y libproj12 postgresql-client-9.3 postgresql-common postgresql-9.3 postgresql-9.3-postgis-2.1 postgresql-9.3-postgis-2.1-scripts postgresql-11-pgrouting netcat
# Install ``python-software-properties``, ``software-properties-common`` and PostgreSQL 9.3
#  There are some warnings (in red) that show up during the build. You can hide
#  them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive
# RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3
# RUN apt-get -u dist-upgrade
# RUN apt-get upgrade

# RUN add-apt-repository ppa:ubuntugis/ppa && apt-get update
# #RUN apt-add-repository ppa:ubuntugis/ubuntugis-unstable
# RUN apt-get update && apt-get -f install -y postgresql-9.3-postgis-2.1 postgresql-9.3-postgis-2.1-scripts
# ADD postgres.conf /etc/supervisor/conf.d/postgres.conf
# RUN apt-get -f install 
# RUN dpkg --configure -a
# RUN apt-get -f install
# RUN apt-get -u dist-upgrade
# RUN apt-get -o Debug::pkgProblemResolver=yes dist-upgrade

# # Note: The official Debian and Ubuntu images automatically ``apt-get clean``
# # after each ``apt-get``
 
# # Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.3`` package when it was ``apt-get installed``
# USER postgres
 
# # Create a PostgreSQL role named ``postgresondocker`` with ``postgresondocker`` as the password and
# # then create a database `postgresondocker` owned by the ``postgresondocker`` role.
# # Note: here we use ``&&\`` to run commands one after the other - the ``\``
# #       allows the RUN command to span multiple lines.
# RUN    /etc/init.d/postgresql start &&\
#     psql --command "CREATE USER postgresondocker WITH SUPERUSER PASSWORD 'postgresondocker';" &&\
#     createdb -O postgresondocker postgresondocker
 
# # Adjust PostgreSQL configuration so that remote connections to the
# # database are possible.
# RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/11/main/pg_hba.conf
 
# # And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
# RUN echo "listen_addresses='*'" >> /etc/postgresql/11/main/postgresql.conf
 
# Expose the PostgreSQL port
EXPOSE 5432
 
# # Add VOLUMEs to allow backup of config, logs and databases
# VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
 
# # Set the default command to run when starting the container
# CMD ["/usr/lib/postgresql/11/bin/postgres", "-D", "/var/lib/postgresql/11/main", "-c", "config_file=/etc/postgresql/11/main/postgresql.conf"]
# #CMD ["/usr/lib/postgresql/11/bin/postgres"]
# Run any additional tasks here that are too tedious to put in
# this dockerfile directly.
ADD env-data.sh /env-data.sh
ADD setup.sh /setup.sh
RUN chmod +x /setup.sh
RUN /setup.sh

# We will run any commands in this when the container starts
ADD docker-entrypoint.sh /docker-entrypoint.sh
ADD setup-conf.sh /
ADD setup-database.sh /
ADD setup-pg_hba.sh /
ADD setup-replication.sh /
ADD setup-ssl.sh /
ADD setup-user.sh /
# ADD postgresql.conf /tmp/postgresql.conf
RUN chmod +x /docker-entrypoint.sh

RUN wget -O pointcloud.tar.gz "https://github.com/pgpointcloud/pointcloud/archive/master.tar.gz" \
	&& apt-get install -y autoconf gcc git-core g++ zlib1g-dev libxml2-dev libpq-dev postgresql-server-dev-11 \
    && mkdir -p /usr/src/pointcloud \
    && tar \
       --extract \
       --file pointcloud.tar.gz \
       --directory /usr/src/pointcloud \
       --strip-components 1 \
   #&& rm pointcloud.tar.gz \
   && cd /usr/src/pointcloud \
   && ./autogen.sh \
   && ./configure \
   && make \
   && make install

RUN apt-get update; apt-get install -y git build-essential cmake make postgresql-server-dev-9.6

RUN git clone https://github.com/Oslandia/pgmorton

RUN cd pgmorton && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install

#RUN sudo -u postgres psql
#RUN psql -d lopocs -c 'create extension postgis'

ENTRYPOINT /docker-entrypoint.sh
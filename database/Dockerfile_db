FROM library/postgres
COPY init.sql /docker-entrypoint-initdb.d/

# set up to default passwords ( only for dev )
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB docker

FROM postgres:13.3
ENV POSTGRES_PASSWORD postuserpassword
ENV POSTGRES_USER post@user.com
ENV POSTGRES_DB testdb
ENV PGDATA /var/lib/postgresql/data/pgdata
EXPOSE 5432

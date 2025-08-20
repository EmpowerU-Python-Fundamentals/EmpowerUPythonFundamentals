#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


#if [ "$DEBUG" != "True" ]
#then
#    uv run manage.py collectstatic --no-input
#fi

echo "Collecting static files..."
uv run manage.py collectstatic --no-input

uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py createsuperuser --noinput

exec "$@"
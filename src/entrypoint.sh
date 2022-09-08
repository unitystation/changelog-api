#!/bin/sh

if [ -n "$DB_NAME" ] && [ "$DB_NAME" = "postgres" ]
then
    echo "Waiting for postgres..."

    if [ -z "$DB_HOST" ]
    then host="db"
    else host="$DB_HOST"
    fi

    if [ -z "$DB_PORT" ]
    then port="5432"
    else port="$DB_PORT"
    fi

    while ! nc -z $host $port; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

# flush all data in the database
#python manage.py flush --no-input

# takes ORM models and makes the sql statements, we shouldn't need to do this since we're committing the migrations
python manage.py makemigrations --noinput

# applies migrations and creates/updates/deletes tables
python manage.py migrate --noinput

# collects static files
python manage.py collectstatic --no-input

exec "$@"
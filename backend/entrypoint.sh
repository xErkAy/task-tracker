#!/bin/bash

until pg_isready -d "$DB_NAME" -h "$DB_HOST" -p 5432 -U "$DB_USER"; do
    echo "$(date) - waiting for postgres"
    sleep 5
done

function run_server() {
    if [ "$DEBUG" = "true" ]; then
        python manage.py runserver 0.0.0.0:8000
    else
        gunicorn --access-logfile - \
            ${GUNICORN_OPTS:---preload --workers 4 --timeout 300 --keep-alive 55} \
            --bind unix:/run/gunicorn.sock \
            project.wsgi:application
    fi
}


yes yes | python manage.py collectstatic && python manage.py migrate && run_server

#!/usr/bin/env bash

set -o errexit  # stop on errors

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server on port $PORT..."
exec gunicorn horilla.wsgi:application --bind 0.0.0.0:$PORT
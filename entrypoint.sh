#!/usr/bin/env bash

echo "Applying migrations..."
python manage.py migrate --noinput || exit 1

echo "Collecting static files..."
python manage.py collectstatic --noinput || exit 1

echo "Starting server..."
gunicorn horilla.wsgi:application --bind 0.0.0.0:$PORT
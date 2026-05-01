#!/usr/bin/env bash

echo "Applying migrations..."
python manage.py migrate --noinput || exit 1

echo "Starting server on port $PORT..."
gunicorn horilla.wsgi:application --bind 0.0.0.0:${PORT:-8000}
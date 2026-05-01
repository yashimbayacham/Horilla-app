#!/usr/bin/env bash

echo "Starting app..."

echo "Running migrations..."
python3 manage.py migrate || exit 1

echo "Collecting static files..."
python3 manage.py collectstatic --noinput || exit 1

echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:8000 horilla.wsgi:application
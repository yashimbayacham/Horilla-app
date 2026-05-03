#!/usr/bin/env bash
set -o errexit

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput || true

echo "Starting server..."
exec gunicorn horilla.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120
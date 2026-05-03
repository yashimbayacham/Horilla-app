#!/usr/bin/env bash
set -o errexit

echo "Running migrations (safe mode)..."

# Run fast migrations first
python manage.py migrate --noinput

# Skip the slow apscheduler migration
python manage.py migrate django_apscheduler 0005 --fake || true

echo "Collecting static files..."
python manage.py collectstatic --noinput || true

echo "Starting server..."
exec gunicorn horilla.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120
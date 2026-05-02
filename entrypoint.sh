#!/usr/bin/env bash
set -o errexit

echo "Making migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Creating superuser if not exists..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
import os

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
EOF

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec gunicorn horilla.wsgi:application --bind 0.0.0.0:$PORT
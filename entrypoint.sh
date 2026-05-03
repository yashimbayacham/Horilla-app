#!/usr/bin/env bash
set -o errexit

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username="yashimbayacham").exists():
    User.objects.create_superuser("yashimbayacham", "yashimbayacham@proton.me", "40RTY5EVEn%")
EOF

echo "Collecting static files..."
python manage.py collectstatic --noinput || true

echo "Starting server..."
exec gunicorn horilla.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3 \
    --timeout 120
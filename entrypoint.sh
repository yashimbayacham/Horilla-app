#!/usr/bin/env bash

echo "Starting app..."

python3 manage.py migrate
python3 manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 horilla.wsgi:application
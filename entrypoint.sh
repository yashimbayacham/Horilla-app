#!/usr/bin/env bash
exec gunicorn horilla.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120
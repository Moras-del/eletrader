#!/bin/bash
python3 manage.py makemigrations --settings eletrader.settings.pro
python3 manage.py migrate --settings eletrader.settings.pro
python3 manage.py collectstatic --settings eletrader.settings.pro --noinput
gunicorn --env DJANGO_SETTINGS_MODULE=eletrader.settings.pro eletrader.wsgi:application --bind 0.0.0.0:8000
